# MP3 to MIDI Converter - Backend Server

This is the FastAPI backend for the MP3 to MIDI converter application. It uses a deep learning model to transcribe audio files into MIDI.

## Prerequisites

-   **Python 3.8+**
-   **FFmpeg** (Recommended): Required for processing MP3 files. If not installed, only WAV files will work.
    -   Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your system PATH.

## Setup

1.  **Navigate to the server directory:**
    ```bash
    cd AudioToMidi_server
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```
    -   **Windows (Command Prompt):**
        ```cmd
        .\venv\Scripts\activate.bat
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This may take a few minutes as it downloads large packages like PyTorch.*

## Running the Server

Ensure your virtual environment is activated, then run:

```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`.

## API Documentation

Once the server is running, you can view the interactive API documentation at:
-   **Swagger UI:** `http://localhost:8000/docs`
-   **ReDoc:** `http://localhost:8000/redoc`

## Project Structure

-   `app/`: Main application code.
    -   `api/`: API route definitions.
    -   `core/`: Configuration settings.
    -   `services/`: Business logic (audio transcription).
    -   `utils/`: Utility functions.
-   `requirements.txt`: List of Python dependencies.
