from setuptools import setup

setup(
    name='k9data',
    version='0.1.dev0',
    packages=[
        'k9data',
        'k9data.common'
    ],
    license='The Unlicense',
    long_description='K9 data analytics',
    install_requires=[
        'pandas',
        'flask'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-pep8'
    ]
)
