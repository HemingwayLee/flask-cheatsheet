import os
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
ytt_api = YouTubeTranscriptApi()

@app.route('/')
def hello_world():
    return 'Hello, World 2'

@app.route('/cc/get/')
def get_cc():
    video_id = request.args.get('video_id')
    language = request.args.get('language', 'en')
    
    if not video_id:
        return jsonify({'error': 'video_id parameter is required'}), 400
    
    try:
        fetched_transcript = ytt_api.fetch(video_id, languages=[language])
        return jsonify({'transcript': fetched_transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

