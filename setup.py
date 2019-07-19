import os
import rest_framework

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    README = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements', 'requirements-app.txt')) as f:
    requirements = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements', 'requirements-setup.txt')) as f:
    requirements_setup = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements', 'requirements-tests.txt')) as f:
    requirements_test = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements', 'requirements-aiohttp.txt')) as f:
    requirements_aiohttp = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements', 'requirements-flask.txt')) as f:
    requirements_flask = f.read()


setup(
    name=rest_framework.__title__,
    version=rest_framework.__version__,
    packages=find_packages(exclude=('tests', '*tests', '*tests*', 'docs', 'docs_theme', 'requirements')),  # We throw away from the assembly too much.
    include_package_data=True,
    test_suite='tests',  # Include tests.
    license='Apache 2.0',  # Put the license.
    description='Python Rest Framework. Box utils for easy makes rest api on python',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    tests_require=requirements_test,
    extras_require={
        'aiohttp': requirements_aiohttp,
        'flask': requirements_flask,
    },
    setup_requires=requirements_setup,
    url=rest_framework.__url__,
    author=rest_framework.__author__,
    author_email=rest_framework.__email__,
    maintainer=rest_framework.__author__,
    maintainer_email=rest_framework.__email__,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=True,
)