# jarmetainforeader
Returns and prints the contents of the manifest and pom.properties file of a given jar file
in the dictionary format.

Compatible with python versions > 3.x versions. 

Installation:

```
pip install jarmetainforeader
```

Sample usage:

```
>>> from jarmanifestreader import manifest_file_reader
>>> manifest_file_reader.get_manifest_contents(r'C:\patch.jar')
{'Manifest-Version': '1.0', 'Ant-Version': 'Apache Ant 1.9.4', 'Created-By': '1.8.0_152-release-1024-b01 (JetBrains s.r.o)'}
>>>
>>> manifest_file_reader.print_manifest_contents(r'C:\patch.jar')
{'Manifest-Version': '1.0', 'Ant-Version': 'Apache Ant 1.9.4', 'Created-By': '1.8.0_152-release-1024-b01 (JetBrains s.r.o)'}

```