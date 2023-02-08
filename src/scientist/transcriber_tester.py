import os
from pathlib import Path
from scribe.transcriber import Transcriber


def test_transcriber(pod_path: str, trans_path: str):
    """Test transcription code using sample data.

    Args:
        pod_path (str): The path to the sample podcast directory. Can be absolute or relative.
        trans_path (str): The path to output the transcriptions. Can be absolute or relative.
    """
    transcriber = Transcriber()

    # Find absolute paths of target directories.
    podcasts = Path(pod_path).resolve()
    transcriptions = Path(trans_path).resolve()
    
    # Confirm that we have the right directory path by printing the files.
    print('\nPODCAST FILES\n')
    print(podcasts.name)
    for file in podcasts.iterdir():
        print(f'|  {file.name}')
    
    # Change CWD to the directory containing the podcast files.
    os.chdir(podcasts)
    print(f'\nChanged directory to {os.getcwd()}\n')
    
    # Transcribe one file.
    freaking_cast = next(podcasts.iterdir())
    content = transcriber.transcribe(freaking_cast.name)
    transcriptions.write_text(content["text"])
    print('\nTRANSCRIBED FILES\n')
    print(freaking_cast)
