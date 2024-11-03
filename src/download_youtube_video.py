import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(url, save_path="."):
    try:
        # YouTubeオブジェクトを生成
        yt = YouTube(url, on_progress_callback = on_progress)
        
        # 最も高い解像度のストリームを取得し、MP4形式でダウンロード
        stream = yt.streams.get_highest_resolution()
        
        # 動画をダウンロードして保存
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# # YouTubeのURLを指定してダウンロードを実行
# youtube_url = "https://www.youtube.com/watch?v=_oQ6SXzzOao"
# download_youtube_video(youtube_url, save_path="output")

output_dir_path = "output/kyatto"

urls = [
    "https://youtu.be/mX9-2Z_A7oY",
    "https://youtu.be/d7sLNGUfbgY",
    "https://youtu.be/lKP9Ysbb7us",
    "https://youtu.be/nueSpQLBdJ8",
    "https://youtu.be/BqftENqrgkw",
    "https://youtu.be/q8jE-xPd_oQ",
    "https://youtu.be/e2NIjUeLoqg",
    "https://youtu.be/qAABwnWqFCI",
    "https://youtu.be/sqC_ZJqb2d0",
    "https://youtu.be/EJ-AEvikvP4",
    "https://youtu.be/lGXQBxn5DXY",
    "https://youtu.be/3WeHSCHep1E",
    "https://youtu.be/ObAytXXLNOs",
    "https://youtu.be/NiWTzNshEjE",
    "https://youtu.be/bdtIYxT7AAE",
    "https://youtu.be/p8Tse641yc8",
    "https://youtu.be/IYcouUdz5bU",
    "https://youtu.be/4f3DwC8XYK8",
    "https://youtu.be/-Bu-RcELUsk",
    "https://youtu.be/uD4ixE5TFvs",
    "https://youtu.be/l18f4SmS0_k",
    "https://youtu.be/_oQ6SXzzOao",
    "https://youtu.be/EWyXPHpYpIo",
    "https://youtu.be/VKvB5ibj8tQ",
    "https://youtu.be/SRjLVdNyPRE",
    "https://youtu.be/d1MlmAHprP0",
    "https://youtu.be/q0VTjcbZuuY"
]

# ディレクトリを作成
os.makedirs(output_dir_path, exist_ok=True)

# YouTubeのURLを指定してダウンロードを実行
for url in urls:
    download_youtube_video(url=url, save_path=output_dir_path)
