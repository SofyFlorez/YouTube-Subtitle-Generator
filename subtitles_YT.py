from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, WebVTTFormatter


def fetch_and_write_transcript(video_id, base_language, target_language):
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    base_transcript_obj = transcripts.find_transcript([base_language])

    if not base_transcript_obj:
        print(f"Transcript in {base_language} not found for video {video_id}")
        return

    base_transcript = base_transcript_obj.fetch()

    # Write base language transcript
    base_text_formatter = TextFormatter()
    base_text = base_text_formatter.format_transcript(base_transcript)
    write_transcript(base_language, base_text)

    # Translate to target language
    if base_transcript_obj.is_translatable:
        target_transcript = base_transcript_obj.translate(target_language).fetch()
    else:
        print(f"Cannot translate transcript to {target_language}")
        return

    # Write target language transcript
    target_text = base_text_formatter.format_transcript(target_transcript)
    write_transcript(target_language, target_text)

    # Write subtitles in target language
    webvtt_formatter = WebVTTFormatter()
    target_subs = webvtt_formatter.format_transcript(target_transcript)
    write_subtitles(target_language, target_subs)


def write_transcript(language, text):
    print(f"Writing {language} Transcript ...", end="")
    with open(f"transcripts/{language}_transcript.txt", "w") as file:
        file.write(text)
    print("Done!")


def write_subtitles(language, subtitles):
    print(f"Writing {language} Subtitles ...", end="")
    with open(f"transcripts/{language}_subs.vtt", "w") as file:
        file.write(subtitles)
    print("Done!")


def main():
    video_id = 'Enter the YouTube video ID'
    base_language = 'es'
    target_language = 'en'

    fetch_and_write_transcript(video_id, base_language, target_language)


if __name__ == "__main__":
    main()
