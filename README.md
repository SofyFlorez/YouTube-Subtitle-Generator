# YouTube Transcript Fetcher

This Python script uses the youtube_transcript_api library to fetch and write transcripts and subtitles for YouTube videos. Its main functionality includes fetching the transcript in a base language, translating it to a target language (if possible), and then writing both the transcripts and subtitles in the specified languages.


## Dependencies


- [youtube_transcript_api:](https://github.com/jdepoix/youtube-transcript-api) A Python library to fetch YouTube transcripts.
## Usage

1. To proceed with the setup, please ensure that all the necessary dependencies are installed. If not, kindly install them before proceeding with the installation process.

```bash
pip install youtube-transcript-api
```

2. Replace the `video_id`, `base_language`, and `target_language` variables in the `main` function with your desired values.

3. Run the script:

```bash
python script_name.py
```

4. The script will retrieve the original language transcript, translate it (if possible) to the target language, and generate subtitles.

5. The subtitles and transcripts will be saved in a directory named "transcripts".
   
## Note

* Make sure that the video's base language is available, otherwise, the script will notify you.

* Translation depends on transcript translatability. Script notifies if not translatable.

## Example

Suppose you have a video with ID '4wGrB4FE2FY' and want English subtitles based on Spanish transcript.

```python
def main():
    video_id = 'NN6PVtoqTiY'
    base_language = 'es'
    target_language = 'en'

    fetch_and_write_transcript(video_id, base_language, target_language)

if __name__ == "__main__":
    main()
```

Integrating this script into your video production workflow can help you in adding multilingual subtitles to your YouTube videos with ease. This will make your videos more accessible and help you reach a wider audience. You are free to modify the script as per your specific needs or add it to your existing video processing pipeline.

## Functions

`fetch_and_write_transcript(video_id, base_language, target_language)`

The function consists of four steps as follows:
1. Retrieving the transcript of a YouTube video in its original language.
2. Saving the transcript in a text file.
3. Translating the transcript to a target language (if available) and storing it in a text file.
4. Generating subtitles in the target language and saving them in a WebVTT file.

`write_transcript(language, text)`

* Writes the provided transcript text to a text file in the "transcripts" directory.

`write_subtitles(language, subtitles)`

* Writes the provided subtitles text to a WebVTT file in the "transcripts" directory.

`main()`

* Defines the main parameters (video ID, base language, target language).
* Calls fetch_and_write_transcript with the specified parameters.
