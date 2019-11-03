from os import path
from setuptools import setup


if __name__ == '__main__':
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='prototurk',
        version='0.2.1',
        description='Simple server for rapidly prototyping Mechanical Turk interfaces',
        long_description=long_description,
        long_description_content_type='text/x-rst',

        packages=[
            'prototurk',
        ],
        include_package_data=True,

        scripts=['scripts/prototurk'],
        setup_requires=[],
        tests_require=[],
        install_requires=[
            'bottle',
            'bs4',
        ],

        url='https://github.com/hltcoe/prototurk',
        license='BSD',
        maintainer='Craig Harman',
        maintainer_email='craig@craigharman.net',
    )
