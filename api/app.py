# api/app.py
from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/api")
def hello():
    return {"message": "Hello from API!"}


@app.route("/upload", methods=["POST"])
def upload_video():
    if "video" not in request.files:
        return {"message": "No video file provided"}, 400
    video = request.files["video"]
    video_path = os.path.join("data/video/", video.filename)
    video.save(video_path)
    # ここで異常検出処理を行う
    # result = detect_anomalies(video_path)
    return {"message": "Video uploaded and processed successfully"}


def detect_anomalies(video_path):
    # ここに異常検出モデルのコードを実装
    # 例: OpenCVを使って動画を解析し、異常を検出する
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
