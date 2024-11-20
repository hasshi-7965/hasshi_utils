import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hasshi_utils",
    version="0.1.0",
    author="hashimoto7965@gmail.com",
    author_email="hashimoto7965@gmail.com",
    description="my utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasshi-7965/hasshi_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
    },
    python_requires='>=3.6',
)