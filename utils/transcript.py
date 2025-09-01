from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    video_id = None
    if "v=" in video_url:  # Normal YouTube link
        video_id = video_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in video_url:  # Short YouTube link
        video_id = video_url.split("youtu.be/")[1].split("?")[0]
    
    if not video_id:
        raise ValueError("Invalid YouTube URL!")

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    text = " ".join([t['text'] for t in transcript])
    return text
