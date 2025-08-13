from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="spotify-knowledge-map",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Discover surprising patterns in your Spotify listening behavior",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/spotify-knowledge-map",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/spotify-knowledge-map/issues",
        "Documentation": "https://github.com/yourusername/spotify-knowledge-map#readme",
        "Source Code": "https://github.com/yourusername/spotify-knowledge-map",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "spotify-analysis=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
        "sample_data": ["*.csv"],
        "assets": ["*.png", "*.jpg"],
    },
)
