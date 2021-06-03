import io
import os
import re
import setuptools

def read(path):
    file_path = os.path.join(os.path.dirname(__file__), *path.split('/'))
    return io.open(file_path, encoding='utf-8').read()

# single-sourcing the package version using method 1 of:
#   https://packaging.python.org/guides/single-sourcing-package-version/
def parse_version_from(path):
    version_file = read(path)
    version_match = re.search(r"^__version__ = '(.*)'", version_file, re.M)
    if version_match is None or len(version_match.groups()) > 1:
        raise ValueError("couldn't parse version")
    return version_match.group(1)

setuptools.setup(
    name='hello',
    version=parse_version_from('hello/__init__.py'),
    description='A simple Python hello world function',
    long_description=read('README.md'),
    author='Dusan Vuckovic',
    author_email='dusan@dvuckovic.com',
    license='WTFPL',
    url='https://github.com/dvuckovic/rtd_test',
    packages=['hello'],
    include_package_data=True,
    zip_safe=True,
    keywords='hello world',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ]
)
