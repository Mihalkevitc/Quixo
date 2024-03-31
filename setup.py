from setuptools import setup, find_packages

setup(
    name='Quixo',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.25.1',
        'flask==1.1.2',
        'numpy==1.21.0',
        'matplotlib==3.4.2',
    ]
    # ,
    # entry_points={
    #     'console_scripts': [
    #         'my_project=my_project.main:main',
    #     ],
    # },
)
