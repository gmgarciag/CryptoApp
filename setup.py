from setuptools import setup

APP = ['CryptoApp.py']
DATA_FILES = ['ca-cert.pem']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'rumps', 'certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)