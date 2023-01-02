from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='net-test',
    version='2.0a0',
    description='A cli app to test the network',
    long_description=readme,
    author='John Bell',
    author_email='blue@jbell.xyz',
    url='https://github.com/packetpunter/pyNetTestShell',
    license=license,
    packages=find_packages(),
    install_requires= [
        'pandas',
        'PyYAML',
        'dnspython',
        'speedtest-cli'
    ],
    setup_requires = [
        "PyYAML",
        "pandas",
        "dnspython",
        "speedtest-cli"
    ]
)
