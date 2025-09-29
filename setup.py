from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #  this function return list of requirements
    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                # -e . in requ.txt is responsible for triggering setup.py
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ankit yadav",
    author_email="ankitdm@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)