from youtube_transcript_api import YouTubeTranscriptApi

video_url='https://www.youtube.com/watch?v=JMOp5n3YgLA'
video_id=video_url.split('=')[1]
print(video_id)
video_info=YouTubeTranscriptApi.get_transcript(video_id)
print('-----------------------')
for v_info in video_info:
    print(v_info)
