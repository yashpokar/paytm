from setuptools import setup, find_packages

setup(
    name='paytm',
    version='0.0.1-dev',
    description='High level paytm mall api',
    url='http://github.com/yashpokar/paytm',
    author='Yash Pokar',
    author_email='hello@yashpokar.com',
    install_requires=[
        'requests',
    ],
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
)
