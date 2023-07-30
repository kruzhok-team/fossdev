with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='useful-utils',
    version='1.0.0',
    packages=find_packages(),
    description='Utils to make life easier',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the type of long description
    author='Your Name',
    author_email='your_name@example.com',
    url='https://github.com/your_username/your_repository',
    install_requires=[
        'pytest',  
    ],
    license='MIT',  # Add your library's license here
    classifiers=[
        # Add classifiers that describe your library
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='python library example',  # Add keywords that describe your library
)
