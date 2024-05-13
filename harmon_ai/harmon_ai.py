import os

class harmon_ai:
    @staticmethod
    def generate_readme(repo_name, owner_name, package_name, icon_url, title, subtitle, important_message, sections_content):
        with open(os.path.join(os.path.dirname(__file__), "templates", "readme_template.md"), "r") as file:
            template = file.read()

        badge_template = harmon_ai.generate_badges(repo_name, owner_name, package_name)

        template = template.replace("{repo_name}", repo_name)
        template = template.replace("{owner_name}", owner_name)
        template = template.replace("{package_name}", package_name)
        template = template.replace("{icon_url}", icon_url)
        template = template.replace("{title}", title)
        template = template.replace("{subtitle}", subtitle)
        template = template.replace("{badges}", badge_template)
        template = template.replace("{important_message}", important_message)
        template = template.replace("{sections_content}", sections_content)

        return template

    @staticmethod
    def generate_badges(repo_name, owner_name, package_name):
        with open(os.path.join(os.path.dirname(__file__), "templates", "badges_template.md"), "r") as file:
            template = file.read()

        template = template.replace("{repo_name}", repo_name)
        template = template.replace("{owner_name}", owner_name)
        template = template.replace("{package_name}", package_name)

        return template