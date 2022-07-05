from setuptools import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description : This function is goign to return the list of requirements 

    return : This function is doign to return the name of libraries required
    """
    rq_packages = []

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        rq_packages = requirement_file.readlines()
        rq_packages.remove("-e .")
        print(rq_packages)
    return rq_packages


PROJECT_NAME = 'housing-predictor'
VERSION ="0.0.3"
AUTHOR ="Mohamed Naji Aboo"
DESCRIPTION = " This is the first FSDS batch project"
PACKAGES = ['housing']

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(), # PACKAGES,
    install_requires = get_requirements_list()
)
