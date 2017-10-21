import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [
    'ipython>=1.0',
    'shortuuid'
]

setup(
    name='text_visualization_magic',
    py_modules=['text_visualization_magic'],
    version='0.1',
    description='Allow to run sentree to visualize text via ipython',
    long_description=README,
    author='Eyal Trabelsi',
    author_email='eyaltrabelsi@gmail.com',
    url='https://github.com/eyaltrabelsi/text_visualization_magic',
    keywords=['visualize', 'ipython', 'text'],
    install_requires=install_requires
)
