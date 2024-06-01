import os
from pathlib import Path
from .utils import load_config, load_file_content, copy_cicd_file_if_missing, config_preview
from art import tprint

class HarmonAI:
    def __init__(self):
        config_path = os.path.expanduser("./.harmon_ai/config.yml")
        self.config = load_config(config_path, os.path.join(Path(__file__).parent, "templates/config.example.yml"))

        tprint("-- HarmonAI --")
        config_preview(self.config)

        output_dir = self.config['harmon_ai']['development']['output_dir']
        os.makedirs(output_dir, exist_ok=True)

        self.important_message = load_file_content(
            os.path.join(output_dir, self.config['harmon_ai']['product']['important_message_file']),
            "templates/important_template.md"
        )
        self.sections_content = load_file_content(
            os.path.join(output_dir, self.config['harmon_ai']['product']['sections_content_file']),
            "templates/sections_template.md"
        )

        # CICDファイルを確認してコピー
        copy_cicd_file_if_missing(self.config, output_dir)

    @staticmethod
    def load_template(template_name):
        """指定されたテンプレート名でテンプレートファイルを読み込む"""
        template_path = os.path.join(os.path.dirname(__file__), "templates", f"{template_name}.md")
        with open(template_path, "r", encoding="utf8") as file:
            return file.read()

    def run(self):
        template = self.load_template("readme_template")
        badge_template = self.generate_badges()
        sns_badges = self.generate_sns_badges()

        template = template.replace("{repo_name}", self.config['harmon_ai']['environment']['repo_name'])
        template = template.replace("{owner_name}", self.config['harmon_ai']['environment']['owner_name'])
        template = template.replace("{package_name}", self.config['harmon_ai']['environment']['package_name'])
        template = template.replace("{icon_url}", self.config['harmon_ai']['environment']['icon_url'])
        template = template.replace("{title}", self.config['harmon_ai']['environment']['title'])
        template = template.replace("{subtitle}", self.config['harmon_ai']['environment']['subtitle'])
        template = template.replace("{badges}", badge_template)
        template = template.replace("{important_message}", self.important_message)
        template = template.replace("{sections_content}", self.sections_content)
        template = template.replace("{sns_badges}", sns_badges)

        output_path = os.path.join(self.config['harmon_ai']['development']['output_dir'], self.config['harmon_ai']['product']['output_file'])
        with open(output_path, "w", encoding="utf8") as file:
            file.write(template)

    def generate_badges(self):
        template = self.load_template("badges_template")
        template = template.replace("{repo_name}", self.config['harmon_ai']['environment']['repo_name'])
        template = template.replace("{owner_name}", self.config['harmon_ai']['environment']['owner_name'])
        template = template.replace("{package_name}", self.config['harmon_ai']['environment']['package_name'])
        return template

    def generate_sns_badges(self):
        template = self.load_template("sns_template")
        template = template.replace("{website_url}", self.config['harmon_ai']['environment']['website_url'])
        template = template.replace("{github_url}", self.config['harmon_ai']['environment']['github_url'])
        template = template.replace("{twitter_url}", self.config['harmon_ai']['environment']['twitter_url'])
        template = template.replace("{blog_url}", self.config['harmon_ai']['environment']['blog_url'])
        return template