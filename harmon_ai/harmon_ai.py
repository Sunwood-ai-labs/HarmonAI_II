import os

class HarmonAI:
    @staticmethod
    def generate_readme(
        repo_name,
        owner_name,
        package_name,
        icon_url,
        title,
        subtitle,
        important_message,
        sections_content,
        website_url,
        github_url, 
        twitter_url,
        blog_url
    ):
        with open(os.path.join(os.path.dirname(__file__), "templates", "readme_template.md"), "r", encoding="utf8") as file:
            template = file.read()

        badge_template = HarmonAI.generate_badges(repo_name, owner_name, package_name)
        sns_badges = HarmonAI.generate_sns_badges(website_url, github_url, twitter_url, blog_url)

        template = template.replace("{repo_name}", repo_name)
        template = template.replace("{owner_name}", owner_name)
        template = template.replace("{package_name}", package_name)
        template = template.replace("{icon_url}", icon_url)
        template = template.replace("{title}", title)
        template = template.replace("{subtitle}", subtitle)
        template = template.replace("{badges}", badge_template)
        template = template.replace("{important_message}", important_message)
        template = template.replace("{sections_content}", sections_content)
        template = template.replace("{sns_badges}", sns_badges)

        return template

    @staticmethod
    def generate_badges(repo_name, owner_name, package_name):
        with open(os.path.join(os.path.dirname(__file__), "templates", "badges_template.md"), "r", encoding="utf8") as file:
            template = file.read()

        template = template.replace("{repo_name}", repo_name)
        template = template.replace("{owner_name}", owner_name)
        template = template.replace("{package_name}", package_name)

        return template

    @staticmethod
    def generate_sns_badges(website_url, github_url, twitter_url, blog_url):
        with open(os.path.join(os.path.dirname(__file__), "templates", "sns_template.md"), "r", encoding="utf8") as file:
            template = file.read()

        template = template.replace("{website_url}", website_url)
        template = template.replace("{github_url}", github_url)
        template = template.replace("{twitter_url}", twitter_url)
        template = template.replace("{blog_url}", blog_url)

        return template