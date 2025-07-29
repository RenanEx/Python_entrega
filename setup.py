from setuptools import setup, find_packages

setup(
    name='SistemaUsuariosRenanAndrade',
    version='1.0.0',
    packages=find_packages(),
    author='Renan Andrade',
    description='Sistema de gerenciamento de usuários com registro e login',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'usuario-app = main:menu',
        ],
    },
    python_requires='>=3.6',
)
