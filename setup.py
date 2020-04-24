from setuptools import setup

setup(
    name='snapshotanalyzer3300',
    version='1.0',
    author='CA',
    author_email='ca@email.com',
    description='snapshot analyzer for ec2 aws',
    license='gpl',
    packages=['shotty'],
    url='https://github.com/albaughca/snapshotanalyzer3300',
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty.cli
    ''',

)
