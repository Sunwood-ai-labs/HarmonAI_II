import os

class HarmonAI:
    @staticmethod
    def load_template(template_name):
        """指定されたテンプレート名でテンプレートファイルを読み込む"""
        template_path = os.path.join(os.path.dirname(__file__), "templates", f"{template_name}.md")
        with open(template_path, "r", encoding="utf8") as file:
            return file.read()

    @staticmethod
    def run(config):
        template = HarmonAI.load_template("readme_template")
        badge_template = HarmonAI.generate_badges(config['repo_name'], config['owner_name'], config['package_name'])
        sns_badges = HarmonAI.generate_sns_badges(
            config['website_url'], config['github_url'], config['twitter_url'], config['blog_url'])

        template = template.replace("{repo_name}", config['repo_name'])
        template = template.replace("{owner_name}", config['owner_name'])
        template = template.replace("{package_name}", config['package_name'])
        template = template.replace("{icon_url}", config['icon_url'])
        template = template.replace("{title}", config['title'])
        template = template.replace("{subtitle}", config['subtitle'])
        template = template.replace("{badges}", badge_template)
        template = template.replace("{important_message}", config.get('important_message', ''))
        template = template.replace("{sections_content}", config.get('sections_content', ''))
        template = template.replace("{sns_badges}", sns_badges)

        return template

    @staticmethod
    def generate_badges(repo_name, owner_name, package_name):
        template = HarmonAI.load_template("badges_template")
        template = template.replace("{repo_name}", repo_name)
        template = template.replace("{owner_name}", owner_name)
        template = template.replace("{package_name}", package_name)
        return template

    @staticmethod
    def generate_sns_badges(website_url, github_url, twitter_url, blog_url):
        template = HarmonAI.load_template("sns_template")
        template = template.replace("{website_url}", website_url)
        template = template.replace("{github_url}", github_url)
        template = template.replace("{twitter_url}", twitter_url)
        template = template.replace("{blog_url}", blog_url)
        return template
