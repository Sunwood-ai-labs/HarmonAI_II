# main.py
import os
from pathlib import Path
from .harmon_ai import HarmonAI
from art import *
from termcolor import colored
from loguru import logger
import sys
from .utils import load_config, load_file_content, copy_cicd_file_if_missing, config_preview

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<8}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def main():

    config_path = os.path.expanduser("./.harmon_ai/config.yml")
    config = load_config(config_path, os.path.join(Path(__file__).parent, "templates/config.example.yml"))

    tprint("-- HarmonAI --")
    config_preview(config)

    output_dir = config['output_dir']
    os.makedirs(output_dir, exist_ok=True)

    important_message = load_file_content(
        os.path.join(output_dir, config['important_message_file']),
        "templates/important_template.md"
    )
    sections_content = load_file_content(
        os.path.join(output_dir, config['sections_content_file']),
        "templates/sections_template.md"
    )

    # CICDファイルを確認してコピー
    copy_cicd_file_if_missing(config, output_dir)

    # HarmonAIの使用例
    readme_template = HarmonAI.run(config)

    output_path = os.path.join(output_dir, config['output_file'])
    with open(output_path, "w", encoding="utf8") as file:
        file.write(readme_template)

    logger.success("READMEファイルが生成されました：{}", output_path)
    tprint("!! successfully !!")

if __name__ == "__main__":
    main()
