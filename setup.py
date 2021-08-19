from os import path
from setuptools import setup




if __name__ == '__main__':
    version = {}
    with open('prototurk/version.py') as fp:
        exec(fp.read(), version)

    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='prototurk',
        version=version['__version__'],
        description='Simple server and script for rapidly prototyping Mechanical Turk interfaces',
        long_description=long_description,
        long_description_content_type='text/x-rst',

        packages=[
            'prototurk',
        ],
        include_package_data=True,

        scripts=[
            'scripts/prototurk',
            'scripts/prototurk-populate',
        ],
        setup_requires=[],
        tests_require=[],
        install_requires=[
            'bottle',
            'bs4',
        ],

        url='https://github.com/hltcoe/prototurk',
        classifiers=[
            'Framework :: Bottle',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 3 :: Only',
        ],
        license='BSD',
        author='Craig Harman',
        author_email='craig@craigharman.net',
    )
