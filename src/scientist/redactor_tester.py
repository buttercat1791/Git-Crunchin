from editor.redactor import Redactor


def test_redactor(transcript_path: str, edited_path: str):
    transcript_file = open(transcript_path, 'r')
    transcript = transcript_file.read()

    redactor = Redactor()
    edited_text = redactor.remove_ads(transcript)

    edited_file = open(edited_path, 'w')
    edited_file.write(edited_text)
