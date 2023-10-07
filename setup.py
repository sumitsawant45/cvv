from setuptools import setup, find_packages
import os
from typing import List
from pathlib import Path

def get_req(filepath:str)->List[str]:
    req=[]
    req=Path(filepath)
    req=[re.replace("\n","") for re in req]
    return req

setup(
    name='prac',
    version="0.1.0",
    description="this is practise project",
    author='sumit',
    author_email='sumitnsawant822@gmail.com',
    install_req=get_req("requirenment.txt"),
    packages=find_packages()
)

