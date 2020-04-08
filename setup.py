# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_climberalex", # the name that you will install via pip
    version="1.2",
    author="Alex Kaiser",
    author_email="climberalex@email.com",
    description="Package with usefull Helper functions. check_null, df_splits",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Lord-Kanzler/lambdata13",
    #keywords="",
    packages=find_packages() # ["lambdata13"]
)