---
title: HarmonAI II
emoji: 🌖
colorFrom: purple
colorTo: gray
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
license: mit
---


<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/HarmonAI_II_icon.jpeg" width="100%">
<br>
<h1 align="center">HarmonAI II</h1>
<h2 align="center">
  ～AI Harmony, Infinite Possibilities～

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MakiAi/HarmonAI_II)
[![HarmonAI_II - Sunwood-ai-labs](https://img.shields.io/static/v1?label=HarmonAI_II&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/HarmonAI_II/Sunwood-ai-labs "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/HarmonAI_II/Sunwood-ai-labs?style=social)](https://github.com/HarmonAI_II/Sunwood-ai-labs)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/HarmonAI_II/Sunwood-ai-labs?style=social)](https://github.com/HarmonAI_II/Sunwood-ai-labs)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/HarmonAI_II)](https://github.com/Sunwood-ai-labs/HarmonAI_II)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/HarmonAI_II)](https://github.com/Sunwood-ai-labs/HarmonAI_II)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/HarmonAI_II?sort=date&color=red)](https://github.com/Sunwood-ai-labs/HarmonAI_II)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/HarmonAI_II?color=orange)](https://github.com/Sunwood-ai-labs/HarmonAI_II)

  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。


## 🌟 はじめに

HarmonAI IIは、AIとの調和と無限の可能性を追求するプロジェクトです。このリポジトリは、HarmonAI IIの開発テンプレートとして機能し、以下のような特長を備えています:

### 1. 開発スピードの向上
- GitHub ActionsとHugging Faceの連携による自動デプロイ
- 定型的な設定ファイル(.gitignore, .SourceSageignoreなど)の事前準備

### 2. リポジトリの品質向上
- 豊富なバッジによるプロジェクト情報の可視化
- 体系的に整えられたREADMEテンプレート
- SourceSageによるAI支援でのコミットメッセージ、リリースノート生成

このテンプレートを活用することで、リポジトリ作成時の初期コストを抑えつつ、品質と開発速度を担保することができます。AI時代の開発スタイルを先取りした、生産性の高いテンプレートとしてご利用ください。

## 🎥 デモ

HarmonAI IIのデモアプリケーションは、GitHub Actionsと連携し、自動的にデプロイされています。デモアプリを体験することで、HarmonAI IIの機能を直感的に理解することができます。

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MakiAi/HarmonAI_II)

## 🚀 使い方

### インストール
HarmonAI IIのインストール手順は以下の通りです:

1. リポジトリをクローンします: `git clone https://github.com/Sunwood-ai-labs/HarmonAI_II.git`
2. 必要な依存関係をインストールします: `pip install -r requirements.txt`

### 使用方法
HarmonAI IIの使用方法は以下の通りです:

```bash
git lfs install
git lfs track "*.png"
git lfs track "*.gif" 
git lfs track "*.jpeg"
git lfs track "*.jpg"
git lfs track "*.mp4"
```

リポジトリ名を適切に変更してください:

```bash
run: git push --force https://MakiAi:$HF_TOKEN@huggingface.co/spaces/MakiAi/HarmonAI_II main
```

harmon-ai --repo_name=HarmonAI_II --owner_name=Sunwood-ai-labs --package_name=harmon_ai --icon_url=https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/HarmonAI_II_icon.jpeg --title="Harmon AI"


### カスタマイズ
HarmonAI IIは、ユーザーのニーズに合わせてカスタマイズ可能です。設定ファイルを編集することで、プロジェクトの動作を柔軟に調整できます。

## 📝 アップデート

### v1.2.0 (2024-05-13)
- `harmon_ai`パッケージの刷新
  - `harmon_ai`クラスの実装
  - テンプレートファイルの読み込みと置換機能の追加
- コマンドラインインターフェース(CLI)の導入
  - `argparse`を使用したCLIオプションの定義
  - 生成されたREADMEファイルの出力機能の追加
- READMEテンプレートファイルの拡充
  - バッジ、重要メッセージ、README構造、セクションのテンプレートの追加
- `harmon_ai`クラスのテストケースの実装
- パッケージのセットアップ設定の更新
- PyPIへのパッケージ公開ワークフローの追加

### v1.1.0 (2024-04-24)
- フロントページの作成
- READMEの全体的な改善
- GitHub Actionsを使用したHugging Face hubへの自動シンク機能の追加
- .gitignoreと.SourceSageignoreの更新
- プロジェクト名を「HarmonAI」から「HarmonAI_II」に変更

### v1.0.0 (2024-04-20)
- 初回リリース
- 基本的な機能を実装

## 🤝 コントリビューション
HarmonAI IIへのご協力は大歓迎です！バグ報告、機能要求、プルリクエストなどを通じて、プロジェクトの改善にご協力ください。詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📄 ライセンス
HarmonAI IIは[MIT License](LICENSE)の下でリリースされています。

## 🙏 謝辞
HarmonAI IIの開発にあたり、以下の方々に感謝いたします:

- [Sunwood-ai-labs](https://github.com/Sunwood-ai-labs)チームのメンバー
- [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)プロジェクト
- [claude.ai](https://claude.ai/)チーム

引き続き、HarmonAI IIプロジェクトをよろしくお願いいたします！