from setuptools import find_packages,setup
from typing import List

def ret_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for requirement in requirements:
            requirement=requirement.replace("\n","")
            if requirement.startswith("-"):
                requirement=requirement[1:]
            requirements_list.append(requirement)
            
    pass

setup(
    name='ML_Project_1',
    version='0.0.1',
    author='Salman',
    author_email='[EMAIL_ADDRESS]',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)