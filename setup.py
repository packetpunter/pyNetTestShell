from setuptools import setup, find_packages
from importlib import resources as r
import os

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

data_path = os.path.join(os.path.dirname(__file__), 'src','config', 'Config.yml')

with open(data_path) as config_file:
    from yaml import safe_load
    config = safe_load(config_file)

setup(
    name=config['tester']['name'],
    version=config['tester']['version'],
    description=config['tester']['description'],
    long_description=readme,
    author='John Bell',
    author_email='blue@jbell.xyz',
    url='https://github.com/packetpunter/pyNetTestShell',
    license=license,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data = {"": ["*.yml"]},
    include_package_data=True,
    install_requires= [
        'PyYAML'
    ],
    setup_requires = [
        "PyYAML"
    ]
)
