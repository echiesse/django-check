from setuptools import setup

setup(
    name='djangocheck',
    version='0.2',
    description='Deploy checker for Django',
    url='https://github.com/echiesse/django-check',
    author='Eric Chiesse',
    author_email='techiesse@gmail.com',
    license='MIT',
    packages=['djangocheck'],
    install_requires=[
        'najha',
    ],
    zip_safe=False
)
