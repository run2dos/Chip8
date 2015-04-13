try:
    from  setuptools import setuptools
except ImportError:
    from distutils.core import setup

setuptools.setup(
    name="Chip8",
    version="0.1.0",

    author="Kevin McGee",
    author_email="run2dos@gmail.com",

    description="An emulation of the Chip8 interpreter.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
