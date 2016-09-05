from setuptools import setup

setup(
    name='scripts',
    version='0.1.dev0',
    packages=['scripts'],
    license='The Unlicense',
    long_description='Management tools and scripts',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-pep8'
    ]
)
