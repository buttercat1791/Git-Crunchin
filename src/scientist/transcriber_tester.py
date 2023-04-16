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
    transcripts = Path(trans_path).resolve()
    
    # Confirm that we have the right directory path by printing the files.
    print('\nPODCAST FILES\n')
    print(podcasts.name)
    for file in podcasts.iterdir():
        print(f'|  {file.name}')

    # Create the output directory if needed.
    if not transcripts.exists() or not transcripts.is_dir():
        transcripts.mkdir()
    
    # Change CWD to the directory containing the podcast files.
    os.chdir(podcasts)
    print(f'\nChanged directory to {os.getcwd()}\n')
    
    # Transcribe one file.
    freaking_cast = next(podcasts.iterdir())
    content = transcriber.transcribe(freaking_cast.name)

    # Create the output file.
    output = transcripts.joinpath(freaking_cast.name).with_suffix('.txt')
    output.write_text(content['text'])

    # Print the names of the completed files.
    print('\nGENERATED FILES\n')
    print(f'{transcripts.parent.name}/{transcripts.name}')
    print(f'|  {output.name}')

