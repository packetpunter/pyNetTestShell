with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
import yaml
with open ("src/Config.yml", "r") as config_file:
    config = config_file.read()

setup(
    name=config['shell']['slug'],
    version=config['shell']['version'],
    description=config['shell']['description'],
    long_description=readme,
    author='John Bell',
    author_email='blue@jbell.xyz',
    url='https://github.com/packetpunter/pyNetTestShell',
    license=license,
    packages=find_packages()
)
