import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="textminer-prozzzzxcv",
    version="0.1.0",
    author="Student",
    author_email="student@example.com",
    description="고급 텍스트 분석을 위한 Python 패키지",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/textminer-pro",
    project_urls={
        "Bug Tracker": "https://github.com/username/textminer-pro/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "nltk>=3.6.0",
        "scikit-learn>=0.24.0",
        "langdetect>=1.0.9",
        "numpy>=1.19.0",
    ],
    keywords="nlp, text mining, text analysis, keyword extraction, summarization, language detection",
)
