from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_req = [req.strip() for req in f.read().split('\n')]
install_req = [req for req in install_req if req and req[0] != '#']

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
     name='starfm',
     version='0.0.1.1',
     description='STARFM for Python',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/gluck3/starfm.git',
     license='MIT',
     packages=find_packages(),
     py_modules=['starfm'],
     install_requires=install_req,
     python_requires=">=3.8",
     setup_requires=['setuptools'],
)
