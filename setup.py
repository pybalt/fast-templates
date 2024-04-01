from setuptools import setup, find_packages

setup(
    name='FastCLI',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/pybalt/FastCLI',
    author='Leonel B. Bravo',
    author_email='leonelbbravo@gmail.com',
    description='A CLI to generate FastAPI templates',
    install_requires=[
        'typer',
        'questionary'
    ],
    entry_points='''
        [console_scripts]
        fastcli=FastCLI.main:app
    '''
)
