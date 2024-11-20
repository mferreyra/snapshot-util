from setuptools import setup, find_packages

PACKAGE_NAME = "snapshot"
VERSION = "0.1" 
DESCRIPTION = "A simple python app to monitor your system/server. Outputs snapshots of system state to json file and stdout"
LONG_DESCRIPTION = open("README.md").read()
AUTHOR = "Matias Ferreyra"
EMAIL = "mferreyra82@gmail.com"
GITHUB_URL = "https://github.com/mferreyra/snapshot-util"

setup(
        name=PACKAGE_NAME, 
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url=GITLAB_URL,
        packages=find_packages(),
        install_requires=[
        "psutil",
        ],
        keywords=['python', 'primer paquete'],
        classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
