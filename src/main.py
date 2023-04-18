from arg_handler import parse_runtime_args
from scientist.transcriber_tester import *
from scientist.redactor_tester import *


def main():
    print("Hello, Crunchers!")
    parse_runtime_args()

    # Assume we're running in the repo root for pathing.
    # test_transcriber('./podcasts', './podcasts/transcripts')
    test_redactor(
        './podcasts/transcripts/BackToSchoolExtravaganza.txt',
        './podcasts/transcripts/BackToSchoolExtravaganza_edited.txt'
    )


if __name__ == "__main__":
    main()
