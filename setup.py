from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """
    This function will provide the list of requirements
    """
    requirement_list=[]
    try:
        with open('file_path','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    
    return requirement_list

setup(
    name="MLProject2",
    version="0.0.1",
    description="ML end to end application package",
    author="Sunny Ghangas",
    author_email="sunnyghangas098@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)