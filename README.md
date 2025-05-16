# Basic Python package that prints 'hello world' and can be built as a wheel.

## Installation

To build the wheel file, run:

```
python3 setup.py bdist_wheel
```

## Usage

After installing the package, you can use it as follows:

```
python3
>>> from helloworldpkg import print_hello_world
>>> print_hello_world()
hello world
```
