# MLエンジニアコースの最終課題
**クライアント（鉄道会社）**

線路内に人が入る異常が発生したときに検知するシステムを作って欲しいです．

**要件**

- コマンド一つで起動や終了できること
- Web上で動作させたい
- 動画を入力として線路内に人間が入ったときに異常を検出する
    - 線路はアプリケーション上から指定ができること

※みんながGPU使えるようならリアルタイムで動作することも要件にしても良いが今回は難しそう

**納品するもの**

- Dockerファイル
    - ローカルで環境構築・動作確認ができるもの
    - 基本構成は推論APIとWebアプリの2つ
- 上記の説明資料
    - .docs または .pptx
    - 背景/手法説明/モデル性能（検出精度・推論速度）などを記載すること