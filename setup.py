import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcloud",
    version="0.0.1",
    author="Author Name",
    author_email="example@domain.com",
    description="Google Cloud Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devendrapratap/g-cloud",
    dependency_links=["https://github.com/devendrapratap/g-cloud.git"],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)