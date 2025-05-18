from setuptools import setup, find_packages

setup(
    name='vulnpro',
    version='1.0.0',
    author='Abhi',
    author_email='abhi@example.com',
    description='Advanced vulnerability scanner by ABHI 🚀',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Abhi-sec566/VulnPro-Python-Project',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'vulnpro=vulnpro.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
