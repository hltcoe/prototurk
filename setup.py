from setuptools import setup


if __name__ == '__main__':
    setup(
        name="murkle",
        version='0.1.0',
        description="",

        packages=[
            'murkle',
        ],
        include_package_data=True,

        scripts=['scripts/murkle-server.py'],
        setup_requires=[],
        tests_require=[],
        install_requires=[
            'bottle',
        ],

        license="BSD",
        maintainer="Craig Harman",
        maintainer_email="craig@craigharman.net",
    )
