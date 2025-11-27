import os
import torch
import librosa
from piano_transcription_inference import PianoTranscription, sample_rate

class AudioService:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Loading PianoTranscription model on {self.device}...")
        self.transcriber = PianoTranscription(device=self.device)
        print("Model loaded.")

    def transcribe(self, input_path: str, output_path: str):
        """
        Transcribes audio from input_path to MIDI at output_path.
        """
        # Load audio using librosa (supports WAV without ffmpeg)
        (audio, _) = librosa.load(input_path, sr=sample_rate, mono=True)

        # Transcribe
        self.transcriber.transcribe(audio, output_path)

# Initialize singleton instance
audio_service = AudioService()
