# filename: fetch_youtube_subtitle.py

import youtube_transcript_api

def fetch_and_save_subtitle(video_id, file_name):
    transcript_list = youtube_transcript_api.YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['en'])
    with open(file_name, 'w') as f:
        for item in transcript.fetch():
            f.write("{}\n".format(item['text']))

fetch_and_save_subtitle('_5ecgEXLoCA', 'output.txt')