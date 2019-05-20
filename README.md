# jarmetainforeader
Returns and prints the contents of the manifest, pom.xml and pom.properties file of a given jar file in the dictionary format.

Originaly, This is forked from https://github.com/badari412/jarmanifestreader.
I added function to find metafiles(MANIFES.MF, pom.xml and pom.properties). 

Compatible with python versions > 3.x versions. 

Installation:

```
pip install jarmetainforeader
```

Sample usage:

If you want to print result
```
>>> from jarmetainforeader import meta_file_reader
>>> meta_file_reader.print_manifest_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

>>>
>>> meta_file_reader.print_pom_properties_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

>>>
>>> meta_file_reader.print_pomxml_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

```
If you want to get data
```
>>> from jarmetainforeader import meta_file_reader
>>> meta_file_reader.get_manifest_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

>>>
>>> meta_file_reader.get_pom_properties_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

>>>
>>> meta_file_reader.get_pomxml_contents('/Users/secuof/Downloads/commons-lang-2.4.jar')

```
