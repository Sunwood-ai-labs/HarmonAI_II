from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="harmon_ai",
    version="1.4.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any dependencies here
        'pyyaml',
        'loguru'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "harmon-ai = harmon_ai.cli:main"
        ]
    },
    url="https://github.com/your_username/gaiah",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)