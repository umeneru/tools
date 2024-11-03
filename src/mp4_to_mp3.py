import os
from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(mp4_path, mp3_path):
    # MP4ファイルを読み込む
    video = VideoFileClip(mp4_path)
    
    # オーディオを抽出し、MP3形式で保存
    video.audio.write_audiofile(mp3_path)

    # 終了処理
    video.close()
    print(f"変換が完了しました: {mp3_path}")



dir_path = "output/kyatto"

output_dir_path = "output/kyatto_mp3"

os.makedirs(output_dir_path, exist_ok=True)

for file_name in os.listdir(dir_path):
    mp4_path = os.path.join(dir_path, file_name)
    
    mp3_path = os.path.join(output_dir_path, file_name.replace(".mp4", ".mp3"))

    convert_mp4_to_mp3(mp4_path, mp3_path)
    


