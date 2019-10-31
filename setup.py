from setuptools import setup


if __name__ == '__main__':
    setup(
        name="prototurk",
        version='0.1.1',
        description="Simple server for rapidly prototyping Mechanical Turk interfaces",

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

        url="https://github.com/hltcoe/prototurk",
        license="BSD",
        maintainer="Craig Harman",
        maintainer_email="craig@craigharman.net",
    )
