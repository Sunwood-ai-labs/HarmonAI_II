# main.py
import sys
from .harmon_ai import HarmonAI
from loguru import logger
import os

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
    harmon_ai = HarmonAI()
    harmon_ai.run()
    logger.success("READMEファイルが生成されました：{}", os.path.join(harmon_ai.config['harmon_ai']['development']['output_dir'], harmon_ai.config['harmon_ai']['product']['output_file']))

if __name__ == "__main__":
    main()