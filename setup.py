from setuptools import setup

setup(
    name="test_command",
    version="0.0",
    py__modeules=["test_command"],
    install_requires=[
        "Click",
    ],
    entry_points='''
    [console_scripts]
    test_command=test_command:cli
    ''',
)
