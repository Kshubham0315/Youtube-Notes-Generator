import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    # Regex se video id extract karna
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    return None

def get_transcript_from_url(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t["text"] for t in transcript])
        return text
    except Exception as e:
        return str(e)
