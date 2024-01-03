import re
from setuptools import find_packages
from setuptools import setup


def get_version():
    filename = "arxiv2text/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_long_description():
    with open("README.md", encoding="UTF-8") as f:
        long_description = f.read()
        return long_description


version = get_version()


setup(
    name="arxiv2text",
    version="0.1.10",
    author="daniel park",
    author_email="parkminwoo1991@gmail.com",
    description="Converting PDF files to text, mainly with a focus on arXiv papers.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/dsdanielpark/arxiv2text",
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    install_requires=["beautifulsoup4", "pdfminer-six", "scikit-learn"],
    keywords="Python, Paper, Data Mining, Translation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={"console_scripts": ["arxiv2text=arxiv2text.cli:main"]},
)
