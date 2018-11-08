from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='apitaxcore',
    packages=find_packages(),  # this must be the same as the name above
    version='3.0.9',
    description='Provides utilities and integration code which may be useful when developing various drivers for use within the Apitax framework.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/ShawnClake/Apitax',  # use the URL to the github repo
    keywords=['restful', 'api', 'commandtax', 'scriptax'],  # arbitrary keywords
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'python_dateutil == 2.6.0',
        'typing == 3.5.2.2',
        'xmltodict',
        'requests',
    ],
)
