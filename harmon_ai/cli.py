import argparse
import os
from .harmon_ai import harmon_ai

def main():
    parser = argparse.ArgumentParser(description="GitHubリポジトリ用のREADMEテンプレートとバッジを生成します。")
    parser.add_argument("--repo_name", help="GitHubリポジトリの名前", default="your-repo")
    parser.add_argument("--owner_name", help="リポジトリオーナーのGitHubユーザー名", default="your-github-username")
    parser.add_argument("--package_name", help="パッケージの名前", default="your-package")
    parser.add_argument("--icon_url", help="READMEに表示するアイコンのURL", default="https://example.com/icon.png")
    parser.add_argument("--title", help="プロジェクトのタイトル", default="Your Project Title")
    parser.add_argument("--subtitle", help="プロジェクトのサブタイトル", default="Your Project Subtitle")
    parser.add_argument("--important_message", help="READMEに表示する重要なメッセージ", default=None)
    parser.add_argument("--sections_content", help="READMEのセクションの内容（introduction, demo, getting_started, updates, contributing, license, acknowledgements）をマークダウン形式で指定", default=None)
    parser.add_argument("--output_dir", help="生成されたREADMEファイルの出力ディレクトリ", default=".harmon_ai")
    parser.add_argument("--output_file", help="生成されたREADMEファイルの名前", default="_README_template.md")

    args = parser.parse_args()

    if args.important_message is None:
        with open(os.path.join(os.path.dirname(__file__), "templates", "important_template.md"), "r", encoding="utf8") as file:
            args.important_message = file.read()

    if args.sections_content is None:
        with open(os.path.join(os.path.dirname(__file__), "templates", "sections_template.md"), "r", encoding="utf8") as file:
            args.sections_content = file.read()

    readme_template = harmon_ai.generate_readme(
        args.repo_name,
        args.owner_name,
        args.package_name,
        args.icon_url,
        args.title,
        args.subtitle,
        args.important_message,
        args.sections_content
    )

    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, args.output_file)
    with open(output_path, "w", encoding="utf8") as file:
        file.write(readme_template)

    print(f"READMEファイルが生成されました: {output_path}")

if __name__ == "__main__":
    main()