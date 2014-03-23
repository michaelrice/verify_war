import sys
import zipfile
from os.path import isfile
from os.path import expanduser

__author__ = 'errr'


class FileNotFoundException(Exception):
    pass


def find_config(war_file=None):
    war_to_check = expanduser(war_file)
    if isfile(war_to_check) and zipfile.is_zipfile(war_to_check):
        zf = zipfile.ZipFile(war_to_check, 'r')
        file_list = zf.namelist()
        if "WEB-INF/classes/external-config.groovy" in file_list:
            return
        raise FileNotFoundException("The config file was not found.")
    raise FileNotFoundException("The war file could not be found, or was not a valid zipfile.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("This script only support 1 arg. That is the full path to the war file.")
    war_file = sys.argv[1]
    find_config(war_file)
