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
    packages=setuptools.find_packages(),
    install_requires=['google-cloud==0.34.0','google-cloud-datastore==1.7.0','google-cloud-pubsub==0.35.4'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)