from setuptools import setup

setup(
    name='snapshotanalyzer',
    version='0.1',
    author='James Anderson',
    author_email="jaa2404@hotmail.com",
    description='SnapshotAnalyzer is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/jim5824/snapshotanalyzer',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points= '''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)