from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fast-templates',
    version='0.1.9',
    packages=find_packages(),
    package_data={'': ['**/*', '.env', '.gitignore']},
    url='https://github.com/pybalt/FastAPI-TemplateWizard',
    author='pybalt',
    author_email='96897286+pybalt@users.noreply.github.com',
    description='A CLI to generate FastAPI templates',
    long_description=long_description,
    install_requires=[
        'typer',
        'questionary',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        fastcli=fasttemplates.main:app
    '''
)
