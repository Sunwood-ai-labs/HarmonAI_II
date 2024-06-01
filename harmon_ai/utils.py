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

def copy_cicd_file_if_missing(config):
    cicd_file_path = Path(config.get('cicd_file_path', './.harmon_ai/publish-to-pypi.yml'))
    template_path = Path(__file__).parent / config.get('cicd_template_path', 'templates/publish-to-pypi.yml')
    if not cicd_file_path.exists():
        if not cicd_file_path.parent.exists():
            os.makedirs(cicd_file_path.parent)
        shutil.copy(template_path, cicd_file_path)
        logger.info("CICDファイルがテンプレートからコピーされました：{}", cicd_file_path)

def config_preview(config):
    for key, value in config.items():
        logger.info("{}：{}", key.replace('_', ' ').capitalize(), value)
