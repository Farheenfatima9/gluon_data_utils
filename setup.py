from setuptools import setup, find_packages

setup(
    name="gluon_data_utils",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # <-- include non-code files
    package_data={"gluon_data_utils": ["reviews.jsonl"]},  # <-- declare dataset
    description="Malicious dataset loader for MXNet",
)
