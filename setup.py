from setuptools import setup, find_packages

setup(
    name='k9data',
    version='0.1.dev0',
    packages=find_packages(),
    include_package_data=True,
    license='The Unlicense',
    long_description='K9 data analytics',
    install_requires=[
        'Click',
        'pandas',
        'Flask'
    ],
    entry_points='''
        [console_scripts]
        read_data=k9data.read_data:cli
    ''',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-pep8'
    ]
)
