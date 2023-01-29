from collections.abc import Callable
from multiprocessing import Pool
from multiprocessing.pool import AsyncResult
from typing import List
import whisper


# TODO: Add error handling.
# TODO: Add per-file progress tracking.
class Transcriber:
    model = None
    completed_files: List[str] = []
    requested_files: List[str] = []

    def __init__(self, whisper_model: str = "base.en"):
        self.model = whisper.load_model(whisper_model)

    def transcribe(self, filename: str) -> str:
        """Transcribe a single audio file from the given filename.

        Args:
            filename (str): The path to the audio file.

        Returns:
            str: The full transcribed text.
        """
        self.requested_files.append(filename)
        transcription = self.model.transcribe(filename)
        self.completed_files.append(filename)
        return transcription

    def transcribe_many(
        self,
        filenames: List[str],
        callback: Callable[[str], None],
        num_processes: int = 4
    ) -> AsyncResult:
        """Transcribes many audio files in parallel, passing each transcription to the callback
        function as it finishes.

        Args:
            filenames (List[str]): A list of filepaths to audio files.
            callback (Callable[[str], None]): The function to be executed when a transcription is
            finished. Should accept a single string containing the full transcript.
            num_processes (int, optional): The max number of processes to run simultaneously.
            Defaults to 4.

        Returns:
            AsyncResult: Indicates when all the input files have been transcribed.
        """
        with Pool(num_processes) as pool:
            return pool.apply_async(self.transcribe, args = filenames, callback = callback)
