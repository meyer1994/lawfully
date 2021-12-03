from setuptools import find_packages, setup

setup(
    name='lawfully',
    version='0.0.1',
    description='Declarative interface to test HTTP endpoints',
    url='https://github.com/meyer1994/lawfully',
    download_url='https://github.com/meyer1994/lawfully/archive/0.0.1.tar.gz',
    author='João Vicente Meyer',
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='http test unit pydantic declarative',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    python_requires='>=3.6',
)
