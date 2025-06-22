

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="letgo_edge",
    version="0.1.0",
    description="Modular, phase-based AI orchestration engine (LetGo/Edge) by Perceive AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bradley Sheats",
    author_email="bradley.sheats88@gmail.com",
    url="https://perceiveai.com",
    packages=find_packages(),
    install_requires=required,
    python_requires=">=3.7",
    include_package_data=True,
    license="MIT",  # Or "Apache-2.0" or custom
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Source": "https://github.com/PerceiveAI/letgo_edge",  # Update as needed
        "Tracker": "https://github.com/PerceiveAI/letgo_edge/issues",
    },
)