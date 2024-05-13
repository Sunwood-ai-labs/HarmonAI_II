import os
import argparse
from .harmon_ai import HarmonAI
from art import *
import os
from termcolor import colored

def main():
   parser = argparse.ArgumentParser(description="GitHubリポジトリ用のREADMEテンプレートとバッジを生成します。")
   parser.add_argument("--repo_name", help="GitHubリポジトリの名前", default="Repo Name")
   parser.add_argument("--owner_name", help="リポジトリオーナーのGitHubユーザー名", default="Owner name")
   parser.add_argument("--package_name", help="パッケージの名前", default="Package Name")
   parser.add_argument("--icon_url", help="READMEに表示するアイコンのURL", default="Icon URL")
   parser.add_argument("--title", help="プロジェクトのタイトル", default="Title")
   parser.add_argument("--subtitle", help="プロジェクトのサブタイトル", default="Subtitle")
   parser.add_argument("--important_message", help="READMEに表示する重要なメッセージ", default=None)
   parser.add_argument("--sections_content", help="READMEのセクションの内容（introduction, demo, getting_started, updates, contributing, license, acknowledgements）をマークダウン形式で指定", default=None)
   parser.add_argument("--website_url", help="プロジェクトのWebサイトのURL", default="")
   parser.add_argument("--github_url", help="GitHubリポジトリのURL", default="")
   parser.add_argument("--twitter_url", help="TwitterプロフィールのURL", default="")
   parser.add_argument("--blog_url", help="公式ブログ記事のURL", default="")
   parser.add_argument("--output_dir", help="出力ディレクトリ", default=".harmon_ai")
   parser.add_argument("--output_file", help="出力ファイル名", default="_README_template.md")

   args = parser.parse_args()
   
   tprint("-- HarmonAI --")
   
   print(colored("Repository Name: ", "cyan") + colored(args.repo_name, "yellow"))
   print(colored("Owner Name: ", "cyan") + colored(args.owner_name, "yellow"))
   print(colored("Package Name: ", "cyan") + colored(args.package_name, "yellow"))
   print(colored("Icon URL: ", "cyan") + colored(args.icon_url, "yellow"))
   print(colored("Title: ", "cyan") + colored(args.title, "yellow"))
   print(colored("Subtitle: ", "cyan") + colored(args.subtitle, "yellow"))
   print(colored("Website URL: ", "cyan") + colored(args.website_url, "yellow"))
   print(colored("GitHub URL: ", "cyan") + colored(args.github_url, "yellow"))
   print(colored("Twitter URL: ", "cyan") + colored(args.twitter_url, "yellow"))
   print(colored("Blog URL: ", "cyan") + colored(args.blog_url, "yellow"))
   print(colored("Output Directory: ", "cyan") + colored(args.output_dir, "yellow"))
   print(colored("Output File: ", "cyan") + colored(args.output_file, "yellow"))
   
   if args.important_message is None:
       with open("./harmon_ai/templates/important_template.md", "r", encoding="utf8") as file:
           args.important_message = file.read()

   if args.sections_content is None:
       with open("./harmon_ai/templates/sections_template.md", "r", encoding="utf8") as file:
           args.sections_content = file.read()

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

   print(colored("READMEファイルが生成されました: ", "green") + colored(output_path, "yellow"))
   tprint("!! successfully !!")

if __name__ == "__main__":
   main()