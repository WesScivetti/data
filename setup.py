from setuptools import setup, find_packages


setup(
    name='pylodata',
    version='0.1.0.dev0',
    license='MIT',
    description='Python Package for Phylogenetic Reconstruction in Linguistics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    author='Johann-Mattis List and Taraka Rama',
    author_email='mattis_list@eva.mpg.de',
    url='https://github.com/pylotests/parsimony',
    keywords='data',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5',
    install_requires=[],
    extras_require={
        'dev': ["pep8", 'wheel', 'twine'],
        'test': [
            'pytest>=4.3',
            "lingpy",
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
)

