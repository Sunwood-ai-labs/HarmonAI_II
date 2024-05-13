import unittest
from harmon_ai import harmon_ai

class Testharmon_ai(unittest.TestCase):
    def test_generate_badges(self):
        repo_name = "test-repo"
        owner_name = "test-owner"
        package_name = "test-package"
        
        with open("harmon_ai/templates/badges_template.html", "r") as file:
            expected_output = file.read()

        expected_output = expected_output.replace("{repo_name}", repo_name)
        expected_output = expected_output.replace("{owner_name}", owner_name)
        expected_output = expected_output.replace("{package_name}", package_name)
        
        result = harmon_ai.generate_badges(repo_name, owner_name, package_name)
        self.assertEqual(result, expected_output)

    def test_generate_readme(self):
        repo_name = "test-repo"
        owner_name = "test-owner"
        package_name = "test-package"
        icon_url = "https://example.com/icon.png"
        title = "Test Title"
        subtitle = "Test Subtitle"
        important_message = "This is an important message."
        
        sections_content = '''
    ## Introduction
    This is the introduction.

    ## Demo
    This is the demo.

    ## Getting Started
    This is how to get started.

    ## Updates
    These are the updates.

    ## Contributing
    This is how to contribute.

    ## License
    This is the license.

    ## Acknowledgements
    These are the acknowledgements.
'''
        
        with open("harmon_ai/templates/readme_template.md", "r") as file:
            expected_output = file.read()

        expected_output = expected_output.replace("{repo_name}", repo_name)
        expected_output = expected_output.replace("{owner_name}", owner_name)
        expected_output = expected_output.replace("{package_name}", package_name)
        expected_output = expected_output.replace("{icon_url}", icon_url)
        expected_output = expected_output.replace("{title}", title)
        expected_output = expected_output.replace("{subtitle}", subtitle)
        expected_output = expected_output.replace("{badges}", harmon_ai.generate_badges(repo_name, owner_name, package_name))
        expected_output = expected_output.replace("{important_message}", important_message)
        expected_output = expected_output.replace("{sections_content}", sections_content)
        
        result = harmon_ai.generate_readme(repo_name, owner_name, package_name, icon_url, title, subtitle, important_message, sections_content)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()