from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    # YouTube video id nikaalne ke liye
    if "v=" in video_url:
        video_id = video_url.split("v=")[1]
    else:
        raise ValueError("Invalid YouTube URL!")
    # Transcript fetch 
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    text = " ".join([t['text'] for t in transcript])
    return text
