""" Generic setup.py template """
from setuptools import setup, find_packages


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == '__main__':
    with open('README.rst', 'r') as fh:
        LONG_DESCRIPTION = fh.read()

    setup(
        name='sudoku',
        version='0.1.0',
        author='Adam Burdett',
        description='Email aggregator',
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/x-rst',
        url='https://github.com/burdettadam/sudoku',
        license='AGPL-3.0',
        packages=find_packages(),
        install_requires=parse_requirements('requirements.txt'),
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent'
        ]
    )
