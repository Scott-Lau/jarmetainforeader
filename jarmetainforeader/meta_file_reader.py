from __future__ import print_function

import os
import zipfile

def _get_meta_file_contents(jar_file_path):
    with zipfile.ZipFile(jar_file_path) as z:
        att_list = []
        for name in z.namelist():
            if 'pom.properties' in name:
                pom_list = z.open(name).readlines()
                att_list.extend(pom_list)
            elif 'MANIFEST.MF' in name:
                manifest_list = z.open(name).readlines()
                att_list.extend(manifest_list)
            else:
                pass
        return att_list


def _format_attributes(metainfo_file_contents):
    metainfo_contents = {}
    for attribute in [a.decode('utf-8') for a in metainfo_file_contents]:
        try:
            if '#' in attribute:
                pass
            elif '=' in attribute:
                metainfo_contents[attribute.split('=')[0].strip()] = attribute.split('=')[1].strip()
            elif ':' in attribute:
                metainfo_contents[attribute.split(':')[0].strip()] = attribute.split(':')[1].strip()
            else:
                pass
        except IndexError:
            continue
    return metainfo_contents


def _is_valid_jar_file(jar_file_path):
    if jar_file_path == '' or jar_file_path is None:
        raise Exception('jar_file_path should not be empty. Please supply the path of the jar file.')

    if not os.path.exists(jar_file_path):
        raise Exception(jar_file_path + ' file does not exist. Please provide correct path.')

    if not jar_file_path.endswith('.jar'):
        raise Exception(jar_file_path + ' file is not a jar file. Please provide a jar file path.')


def get_metainfo_contents(jar_file_path):
    """
    Returns the contents of the manifest and pom.properties file of the given jar file in dictionary format
    :param jar_file_path: path of the jar file
    :return: Return s a dictionary of the manifets file contents
    """
    _is_valid_jar_file(jar_file_path)
    metainfo_file_contents = _get_meta_file_contents(jar_file_path)
    return _format_attributes(metainfo_file_contents)


def print_metainfo_contents(jar_file_path):
    """
    Prints the contents of the manifest and pom.properties  file of the given jar file in dictionary format
    :param jar_file_path:
    :return:
    """
    print(get_metainfo_contents(jar_file_path))
