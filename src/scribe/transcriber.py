from typing import List
import whisper


class Transcriber:
    model = None
    completed_files: List[str] = []
    requested_files: List[str] = []

    def __init__(self, whisper_model: str = "base.en"):
        self.model = whisper.load_model(whisper_model)

    def transcribe(self, filename: str) -> str:
        self.requested_files.append(filename)
        transcription = self.model.transcribe(filename)
        self.completed_files.append(filename)
        return transcription
