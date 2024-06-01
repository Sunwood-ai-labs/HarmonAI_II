import os
import shutil
import yaml
from .harmon_ai import HarmonAI
from art import *
from termcolor import colored
from pathlib import Path
from loguru import logger
import sys

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<8}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def load_config(file_path, default_path):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        shutil.copy(default_path, file_path)
        logger.info("設定ファイルがテンプレートから作成されました：{}", file_path)
    with open(file_path, "r", encoding='utf8') as file:
        return yaml.safe_load(file)

def load_file_content(user_file_path, default_file_path):
    user_path = Path(user_file_path)
    base_path = Path(__file__).parent
    default_path = base_path / default_file_path

    logger.debug("デフォルトパス：{}", default_path)
    logger.debug("ユーザーパス：{}... 存在する：{}", user_path, os.path.exists(user_path))
    
    if not os.path.exists(user_path):
        os.makedirs(user_path.parent, exist_ok=True)
        shutil.copy(default_path, user_path)
        logger.info("テンプレートファイルがこちらにコピーされました：{}", user_path)

    with open(user_path, "r", encoding="utf8") as file:
        return file.read()

def main():
    config_path = os.path.expanduser("./.harmon_ai/config.yml")
    default_config_path = os.path.join(Path(__file__).parent, "templates/config.example.yml")
    config = load_config(config_path, default_config_path)

    tprint("-- HarmonAI --")

    important_message = load_file_content(
        config['important_message_file'],
        "templates/important_template.md"
    )
    sections_content = load_file_content(
        config['sections_content_file'],
        "templates/sections_template.md"
    )

    logger.info("リポジトリ名：{}", config['repo_name'])
    logger.info("オーナー名：{}", config['owner_name'])
    logger.info("パッケージ名：{}", config['package_name'])
    logger.info("アイコンURL：{}", config['icon_url'])
    logger.info("プロジェクトタイトル：{}", config['title'])
    logger.info("サブタイトル：{}", config['subtitle'])
    logger.info("重要なメッセージテンプレートファイル：{}", config['important_message_file'])
    logger.info("セクション内容テンプレートファイル：{}", config['sections_content_file'])
    logger.info("プロジェクトWebサイトURL：{}", config['website_url'])
    logger.info("GitHub URL：{}", config['github_url'])
    logger.info("Twitter URL：{}", config['twitter_url'])
    logger.info("ブログURL：{}", config['blog_url'])
    logger.info("出力ディレクトリ：{}", config['output_dir'])
    logger.info("出力ファイル名：{}", config['output_file'])

    # HarmonAIの使用例
    readme_template = HarmonAI.run(
        config['repo_name'],
        config['owner_name'],
        config['package_name'],
        config['icon_url'],
        config['title'],
        config['subtitle'],
        important_message,
        sections_content,
        config['website_url'],
        config['github_url'],
        config['twitter_url'],
        config['blog_url']
    )

    output_dir = config['output_dir']
    output_file = config['output_file']
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)
    with open(output_path, "w", encoding="utf8") as file:
        file.write(readme_template)

    logger.success("READMEファイルが生成されました：{}", output_path)
    tprint("!! successfully !!")

if __name__ == "__main__":
    main()