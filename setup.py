from setuptools import setup

setup(
    name='Django Check',
    version='0.1',
    description='Deploy checker for Django',
    url='https://github.com/techiesse/django-check',
    author='Eric Chiesse',
    author_email='techiesse@gmail.com',
    license='MIT',
    packages=['djangocheck'],
    install_requires=[
        'najha',
    ],
    zip_safe=False
)
