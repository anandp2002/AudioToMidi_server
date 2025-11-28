import time
import os
import shutil
import tempfile
import traceback
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask

from app.services.audio_service import audio_service
from app.utils.file_utils import cleanup_files

router = APIRouter()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    if not file.filename.endswith(('.mp3', '.wav', '.flac', '.m4a')):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an audio file.")

    # Create temporary files for input and output
    # We use the original extension to help with file type detection if needed, though librosa is robust.
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_input:
        shutil.copyfileobj(file.file, tmp_input)
        tmp_input_path = tmp_input.name
    
    tmp_output_path = tmp_input_path + ".mid"

    try:
        # Use the service to transcribe
        start_time = time.time()
        audio_service.transcribe(tmp_input_path, tmp_output_path)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Conversion time: {duration} seconds")

        return FileResponse(
            tmp_output_path, 
            media_type="audio/midi", 
            filename=f"{os.path.splitext(file.filename)[0]}.mid",
            background=BackgroundTask(cleanup_files, tmp_input_path, tmp_output_path),
            headers={"X-Conversion-Time": str(duration)}
        )

    except Exception as e:
        traceback.print_exc()
        # Cleanup on error
        cleanup_files(tmp_input_path, tmp_output_path)
        raise HTTPException(status_code=500, detail=str(e))
