from setuptools import setup
setup(
    name='CmdCom',
    version='0.1',
    description='Package for reading panic button.',
    url='#',
    author='Matthew Raison',
    author_email='matthewraison@outlook.com',
    # license='MIT',
    packages=[
        'CmdCom',
        'CmdCom.command',
        'CmdCom.func',
        'CmdCom.option'
    ],
    zip_safe=False
)
