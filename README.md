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
>>> manifest_file_reader.get_manifest_contents('/Volumes/backup_disk/clarity/clarity_automation_test/clarity_db/central/indy-diagnostics-jaxrs/indy-diagnostics-jaxrs-1.3.0.jar')
{'Manifest-Version': '1.0', 'Archiver-Version': 'Plexus Archiver', 'Built-By': 'jdcasey', 'Created-By': 'Apache Maven 3.5.0', 'Build-Jdk': '1.8.0_171', 'version': '1.3.0', 'groupId': 'org.commonjava.indy', 'artifactId': 'indy-diagnostics-jaxrs'}
>>>
>>> manifest_file_reader.print_manifest_contents('/Volumes/backup_disk/clarity/clarity_automation_test/clarity_db/central/indy-diagnostics-jaxrs/indy-diagnostics-jaxrs-1.3.0.jar')
{'Manifest-Version': '1.0', 'Archiver-Version': 'Plexus Archiver', 'Built-By': 'jdcasey', 'Created-By': 'Apache Maven 3.5.0', 'Build-Jdk': '1.8.0_171', 'version': '1.3.0', 'groupId': 'org.commonjava.indy', 'artifactId': 'indy-diagnostics-jaxrs'}

```