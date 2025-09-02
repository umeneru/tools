# 便利ツール

## 前提
- uvがインストールされていること
- ffmpegがインストールされていること

## 最初に
``` bash
cd tools
uv sync
```

## YouTube動画ダウンローダー
``` bash
uv run src/download_youtube_video.py <YouTube動画のURL>
uv run src/download_youtube_video.py -o <保存先ディレクトリ> <YouTube動画のURL>
```

