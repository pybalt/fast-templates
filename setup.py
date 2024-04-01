from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='FastAPI-TemplateWizard',
    version='0.1.5',
    packages=find_packages(),
    url='https://github.com/pybalt/FastAPI-TemplateWizard',
    author='pybalt',
    author_email='96897286+pybalt@users.noreply.github.com',
    description='A CLI to generate FastAPI templates',
    long_description=long_description,
    install_requires=[
        'typer',
        'questionary'
    ],
    entry_points='''
        [console_scripts]
        fastcli=fastapitemplatewizard.main:app
    '''
)
