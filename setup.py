import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='password_generator',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU GPLv3',
    packages=['password_generator'],
    install_requires=['Random-Word'],
)