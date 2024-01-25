from setuptools import setup, find_packages

setup(
    name="CipherCraft",
    version="1.0",
    description="Python-based cryptography tool with a command-line interface",
    install_requires=[
        "click==8.1.7",
        "colorama==0.4.6",
        "iniconfig==2.0.0",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "mpmath==1.3.0",
        "numpy==1.26.2",
        "packaging==23.2",
        "pluggy==1.3.0",
        "prompt-toolkit==3.0.36",
        "Pygments==2.17.2",
        "PySimpleValidate==0.2.12",
        "pytest==7.4.3",
        "questionary==2.0.1",
        "stdiomask==0.0.6",
        "sympy==1.12",
        "wcwidth==0.2.12"
    ],
    entry_points={
        "console_scripts": [
            "ciphercraft-cli = bin.ciphercraft_cli:main"
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'assets': ['logo/logo.png'],
        'utils.Generators.files': ['logo.txt'],
        'inventory.rsa': ['*.pem'],
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
