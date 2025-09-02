"""
YouTube動画をFHD (1080p) でダウンロードするスクリプト

[実行コマンド]
python src/download_youtube_video.py <YouTube動画のURL>
python src/download_youtube_video.py -o <保存先ディレクトリ> <YouTube動画のURL>
"""
import os
import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_youtube_video(url, save_path="."):
    try:
        # YouTubeオブジェクトを生成
        yt = YouTube(url, on_progress_callback=on_progress)

        # FHD(1080p)以上の映像ストリームを取得（映像のみ）
        video_stream = (
            yt.streams
            .filter(res="1080p", file_extension="mp4", progressive=False, only_video=True)
            .order_by("fps")
            .desc()
            .first()
        )

        # 音声ストリームを取得（最高音質）
        audio_stream = (
            yt.streams
            .filter(only_audio=True, file_extension="mp4")
            .order_by("abr")
            .desc()
            .first()
        )

        if not video_stream or not audio_stream:
            raise Exception("1080p映像または音声ストリームが見つかりませんでした。")

        # 一時保存ファイル名
        base_name = yt.title.replace("/", "_").replace("\\", "_")
        video_path = os.path.join(save_path, f"{base_name}_video.mp4")
        audio_path = os.path.join(save_path, f"{base_name}_audio.mp4")
        output_path = os.path.join(save_path, f"{base_name}_1080p.mp4")

        # ダウンロード
        print(f"Downloading Video: {yt.title} ({video_stream.resolution})")
        video_stream.download(output_path=save_path, filename=f"{base_name}_video.mp4")
        print(f"Downloading Audio: {yt.title}")
        audio_stream.download(output_path=save_path, filename=f"{base_name}_audio.mp4")

        # ffmpegで結合
        print("Merging video and audio with ffmpeg...")
        cmd = f'ffmpeg -y -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{output_path}"'
        os.system(cmd)

        # 一時ファイル削除
        os.remove(video_path)
        os.remove(audio_path)

        print(f"Download completed successfully! -> {output_path}\n")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="YouTube動画をFHD (1080p) でダウンロードするスクリプト")
    parser.add_argument(
        "urls",
        nargs="+",
        help="YouTube動画のURL（複数指定可）"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="保存先ディレクトリ（デフォルト: output）"
    )
    args = parser.parse_args()

    # 保存先ディレクトリを作成
    os.makedirs(args.output, exist_ok=True)

    # 指定されたすべてのURLについて処理
    for url in args.urls:
        download_youtube_video(url=url, save_path=args.output)


if __name__ == "__main__":
    main()
