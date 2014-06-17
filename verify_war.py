"""
Written by Michael Rice
Github: https://github.com/michaelrice
Website: https://michaelrice.github.io/
Blog: http://www.errr-online.com/
This code has been released under the terms of the MIT licenses
http://opensource.org/licenses/MIT
"""

import sys
import zipfile
from os.path import isfile
from os.path import expanduser

__author__ = 'michael rice <michael@michaelrice.org>'


class FileNotFoundException(Exception):
    pass


class InvalidFileFormat(Exception):
    pass


def find_config(war_file=None):
    """
    This is used from fabric to help QC grails war files
    that should contain an external config file.

    It was created because for some reason during a grails prod war
    from jenkins the external config file would sometimes not get
    added to the war. This was used from the fabric deployment script
    to check for this file before sending the war to the remote hosts.

    :param war_file (String): Full path to the war_file.
    :return: void
    :raise FileNotFoundException: Raised when the config cant be found
    :raise InvalidFileFormat: Raised when the war file is not a valid zip file.
    """
    war_to_check = expanduser(war_file)
    if isfile(war_to_check):
        if not zipfile.is_zipfile(war_to_check):
            raise InvalidFileFormat("The war file is not a valid zip file.")
        zf = zipfile.ZipFile(war_to_check, 'r')
        file_list = zf.namelist()
        if "WEB-INF/classes/external-config.groovy" in file_list:
            return
        raise FileNotFoundException("The config file was not found.")
    msg = "{0} is not a valid file on the file system.".format(war_file)
    raise FileNotFoundException(msg)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("This script only support 1 arg. That is the full path"
                        " to the war file.")
    war = sys.argv[1]
    find_config(war_file=war)
