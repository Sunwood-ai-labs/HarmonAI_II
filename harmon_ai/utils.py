# utils.py
import os
import shutil
from pathlib import Path
from loguru import logger
import yaml

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

def copy_cicd_file_if_missing(config, output_dir):
    cicd_file_path = Path(output_dir) / config['harmon_ai']['product'].get('cicd_file_path', 'publish-to-pypi.yml')
    cicd_main_path = Path(config["harmon_ai"]["main"]["main_dir"]) /  Path(config["harmon_ai"]["product"]["github_cicd_dir"]) / config['harmon_ai']['product'].get('cicd_main_path', 'publish-to-pypi.yml')
    template_path = Path(__file__).parent / config['harmon_ai']['product'].get('cicd_template_path', 'templates/publish-to-pypi.yml')
    if not cicd_file_path.exists():
        shutil.copy(template_path, cicd_file_path)
        logger.info("[Development] CICDファイルがテンプレートからコピーされました：{}", cicd_file_path)

        # ファイルを読み込んで内容を置換
        with open(cicd_file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            content = content.replace("https://pypi.org/p/harmon_ai", f"https://pypi.org/p/{config['harmon_ai']['environment']['package_name']}")
            file.seek(0)
            file.write(content)
            file.truncate()  # 既存の内容が新しい内容より長い場合、余分な部分を削除
            logger.info(f"[Development] URLが置換されました：{cicd_file_path}")

    if not cicd_main_path.exists():
        os.makedirs(cicd_main_path.parent, exist_ok=True)
        shutil.copy(cicd_file_path, cicd_main_path)
        logger.info("[Production] CICDファイルが開発用からコピーされました：{}", cicd_main_path)

def config_preview(config):
    for key, value in config['harmon_ai']['environment'].items():
        logger.info("{}：{}", key.replace('_', ' ').capitalize(), value)