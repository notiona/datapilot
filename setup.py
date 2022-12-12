import setuptools

with open("README.md", "r", encoding = "utf-8") as fd:
    long_description = fd.read()

setuptools.setup(
    name = "datapilot",
    version = "0.0.1",
    author = "Junghoon Lee",
    author_email = "notiona@snu.ac.kr",
    description = (
        "Datapilot is an open-source, low-code "
        "data wrangling assistant library in Python"
    ),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/notiona/datapilot",
    project_urls = {
        "Bug Tracker": "https://github.com/notiona/datapilot/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "datapilot"},
    packages = setuptools.find_packages(where="datapilot"),
    python_requires = ">=3.7"
)