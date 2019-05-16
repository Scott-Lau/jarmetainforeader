from setuptools import setup, find_packages

setup(
    name='jarmetainforeader',  # How you named your package folder (MyLib)
    packages=['jarmetainforeader'],  # Chose the same as "name"
    version='0.2',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Returns the contents of the manifest file of a given jar file in the dictionary format. This is originaly repository https://github.com/badari412/jarmanifestreader. This is forked.',
    # Give a short description about your library
    author='David Hong',  # Type in your name
    author_email='secuof@gmail.com',  # Type in your E-Mail
    url='https://github.com/secuof/jarmetainforeader.git',  # Provide either the link to your github or to your website
    download_url='https://github.com/secuof/jarmetainforeader/archive/master.zip',  # I explain this later on
    keywords=['PYTHON', 'JAR', 'MANIFEST', 'POM', 'JAR INFO READER' 'MANIFESTREADER', 'READER'],  # Keywords that define your package best
    python_requires  = '>=3',

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
