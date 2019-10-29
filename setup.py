# setup.py

from setuptools import setup, find_packages

setup(
    name="coloredprinter",
    version="0.0.1",
    keywords=("colorful", "print", "style"),
    description="Make your output more colorful",
    long_description="A util to make your output more colorful!",
    license="GPL Licence",

    url="https://github.com/code4like/ColorfulPrinter",
    author="code4like",
    author_email="3129463533@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
)
