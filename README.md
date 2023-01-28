
# Git-Crunchin

For Crunch Podcast fans, created to help Ethan with his problems but who knows what else the future holds

## Projects

### Operation Transcription

Ethan:
I'm wanting to transcribe all of our episodes to put on our website. This will boost our SEO. Apparently we should've been doing it this whole time, nobody told me. Yesterday I figured out how to use Whisper (made by OpenAI, the chatGPT people) to transcribe files. I am able to manually navigate to the file in cmd and run the whisper script, which generates a text file of the audio. 1 hour of podcasting gets transcribed in about 15 minutes. Pretty neat!

I also went back and downloaded all of our back catalog from iTunes - about 330 files. I'd like to have a script that automatically moves on from one file to the next and is constantly transcribing the files in the background until they're all complete. I'd also like the text files that get generated to be placed in a separate folder. If it's possible, I'd like for the Aquinas Wealth ad and the Pilgrimage ad to be removed from the text file of each episode. I don't have all of the original mp3's so all we are working with is the episodes with dynamic insertion. 

Finally, and this might have to happen manually, I need the transcriptions uploaded to a blog post on our website, backdated to the date of the original episode, a Spotify link embedded in the post, and the episode description updated to include a link to the transcript on the website. 

MVP for the project is automatically moving from one audio file to the next and placing all the text files in a folder.
But I figured I'd give you the whole enchilada just in case it's possible.

### Setup

This project uses Python virtual environments.  For Whisper compatibility, use Python 3.8, 3.9, or 3.10.

Install all required packages by running:

```python
pip install -r requirements.txt
```

### Usage

Run the program from the repo root directory with:

```python
python ./src/main.py
```
