
from setuptools import setup, Extension, find_packages

setup(
    name="helloworldpkg",
    version="0.1.0",
    description="A simple package that prints hello world",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.6",
    ext_modules=[
        Extension(
            "helloworldpkg.dummy.dummy",
            ["helloworldpkg/dummy/dummy.c"],
        ),
    ],
)
