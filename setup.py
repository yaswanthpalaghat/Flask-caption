import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-caption",
    version="1.0",
    author="Yaswanth Sai Palaghat",
    author_email="yaswanthpalaghat@gmail.com",
    description="This is a Python library to generate captions for the images with Flask Rest-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaswanthpalaghat/Flask-caption",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)