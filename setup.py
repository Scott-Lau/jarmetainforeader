import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='jarmetainforeader',  
    packages=['jarmetainforeader'],  # Chose the same as "name"
    version='0.2.2',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Returns the contents of the manifest and pom.properties file of a given jar file in the dictionary format. This is originaly repository https://github.com/badari412/jarmanifestreader. This is forked. I added function to find metainfo file to read pom.properties and MANIFES file',
    # Give a short description about your library
    author='David Hong',  # Type in your name
    author_email='secuof@gmail.com',  # Type in your E-Mail
    url='https://github.com/secuof/jarmetainforeader.git',  # Provide either the link to your github or to your website
    download_url='https://github.com/secuof/jarmetainforeader/archive/master.zip',  # I explain this later on
    keywords=['PYTHON', 'JAR', 'MANIFEST', 'POM', 'JAR INFO READER' 'MANIFESTREADER', 'READER'],  # Keywords that define your package best
    install_requires = ['xmltodict'],
    python_requires  = '>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
