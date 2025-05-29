# setup.py
from setuptools import setup, find_packages

setup(
    name='gluon_data_utils',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'gluon_data_utils': ['reviews.jsonl'],  # include dataset file
    },
    description='A simple MXNet dataset loader for reviews.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='HelpfulResearcher',
    author_email='datahelper@example.com',
    url='https://github.com/attacker123/gluon_data_utils',  # fake project
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

