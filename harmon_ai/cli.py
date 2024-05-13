import os
import argparse
from .harmon_ai import HarmonAI

def main():
    parser = argparse.ArgumentParser(description="GitHubリポジトリ用のREADMEテンプレートとバッジを生成します。")
    parser.add_argument("repo_name", help="GitHubリポジトリの名前")
    parser.add_argument("owner_name", help="リポジトリオーナーのGitHubユーザー名")
    parser.add_argument("package_name", help="パッケージの名前")
    parser.add_argument("icon_url", help="READMEに表示するアイコンのURL")
    parser.add_argument("title", help="プロジェクトのタイトル")
    parser.add_argument("subtitle", help="プロジェクトのサブタイトル")
    parser.add_argument("important_message", help="READMEに表示する重要なメッセージ")
    parser.add_argument("sections_content", help="READMEのセクションの内容（introduction, demo, getting_started, updates, contributing, license, acknowledgements）をマークダウン形式で指定")
    parser.add_argument("--website_url", help="プロジェクトのWebサイトのURL", default="")
    parser.add_argument("--github_url", help="GitHubリポジトリのURL", default="")
    parser.add_argument("--twitter_url", help="TwitterプロフィールのURL", default="")
    parser.add_argument("--blog_url", help="公式ブログ記事のURL", default="")

    args = parser.parse_args()

    readme_template = HarmonAI.generate_readme(
        args.repo_name,
        args.owner_name,
        args.package_name,
        args.icon_url,
        args.title,
        args.subtitle,
        args.important_message,
        args.sections_content,
        args.website_url,
        args.github_url,
        args.twitter_url,
        args.blog_url
    )


    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, args.output_file)
    with open(output_path, "w", encoding="utf8") as file:
        file.write(readme_template)

    print(f"READMEファイルが生成されました: {output_path}")

if __name__ == "__main__":
    main()