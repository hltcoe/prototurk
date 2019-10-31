from setuptools import setup


if __name__ == '__main__':
    setup(
        name="prototurk",
        version='0.1.0',
        description="",

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

        license="BSD",
        maintainer="Craig Harman",
        maintainer_email="craig@craigharman.net",
    )
