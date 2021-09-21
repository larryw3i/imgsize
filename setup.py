import setuptools
import re
from imgsize import *

long_description = open("README.md", "r", encoding="utf-8").read()

setuptools.setup(
    name=__appname__,
    version=__appversion__,
    author=__appauthor__,
    author_email="",
    description="Change the size of your photos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/larryw3i/imgsize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'imgsize=imgsize:simple',
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'opencv-contrib-python >= 4.5.3.56',
        'Pillow >= 8.3.0',
        'numpy >= 1.21.1',
        'appdirs >= 1.4.3'
    ],
    include_package_data = True,
)
