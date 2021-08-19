from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ssk_emart_customizations/__init__.py
from ssk_emart_customizations import __version__ as version

setup(
	name="ssk_emart_customizations",
	version=version,
	description="Ssk Emart Customizations",
	author="Promantia Business Solutions Pvt Ltd",
	author_email="rakshith.n@promantia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
