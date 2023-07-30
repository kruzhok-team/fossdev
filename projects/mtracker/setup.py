from setuptools import setup

setup(
   name='mtracker',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Artem Vesnin',
   author_email='artemvesnin@gmail.com',
   url='https://github.com/standlab/mtracker',
   packages=['mtracker'], 
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
