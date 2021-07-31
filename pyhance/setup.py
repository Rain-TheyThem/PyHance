import setuptools

with open("./pyhance/README.md", "r") as fhandle:
    long_description = fhandle.read()

setuptools.setup(
    name="PyHance",
    version="0.1.2",
    author="Izabella",
    description="An enhancement to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=
    "https://github.com/IzaCoder/PyHance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)