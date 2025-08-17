from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url: str) -> str:
    """
    Fetches the transcript for a given YouTube video URL.

    Args:
        video_url: The URL of the YouTube video.

    Returns:
        The transcript as a single string, or an error message.
    """
    try:
        video_id = video_url.split("v=")[1]
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
        
        transcript = " ".join([snippet.text for snippet in transcript_list.snippets])
        return transcript
    except Exception as e:
        return f"Error fetching transcript: {e}"
