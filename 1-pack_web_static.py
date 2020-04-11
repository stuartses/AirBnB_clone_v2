#!/usr/bin/python3

"""
AirBnB Clone
Deploy using Fabric
Creates tgz file from web static
"""

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """ Creates a tgz of a Web Static directory

    Return:
        Path of tgz file
    """

    # create directory
    version_dir = "versions"
    if (os.path.exists(version_dir) is False):
        local("mkdir {}".format(version_dir))

    # create tgz file
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_path = version_dir + "/web_static_" + current_time + ".tgz"
    source_dir = "web_static"

    try:
        print("Packing web_static to {}".format(tgz_path))
        local("tar -cvzf {} {}".format(tgz_path, source_dir))
        print("web_static packed: {}".format(tgz_path))
        return tgz_path
    except:
        return None
