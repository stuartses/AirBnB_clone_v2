#!/usr/bin/python3

"""
AirBnB Clone
Deploy using Fabric
Upload data to remote server
"""

from fabric.api import *
import os.path

# Set a default env.user if you want, quit # to the next line
# env.user = 'ubuntu'
env.hosts = ['35.237.164.135', '18.234.226.240']


def do_deploy(archive_path):
    """ Distributes an archive to web servers

    Return:
        True on sucess
        False on fails
    """

    # check if archive_path exists
    if (os.path.exists(archive_path) is False):
        return False

    file_name = archive_path.split("/")[-1]  # the last position in split array
    file_basename = file_name.split(".")[0]  # without extension

    dest_path = "/tmp/" + file_name
    uncom_path = "/data/web_static/releases/" + file_basename

    symbol_path = "/data/web_static/current"

    try:
        # upload file
        put(archive_path, dest_path)

        # Uncompress
        run("mkdir -p {}".format(uncom_path))
        run("tar -xzf {} -C {}".format(dest_path, uncom_path))

        # delete uploaded file
        run("rm {}".format(dest_path))

        # move files out of web_static directory
        run("mv {} {}".format(uncom_path + "/web_static/*", uncom_path))
        run("rm -rf {}".format(uncom_path + "/web_static"))

        # Symbolic Link. With overwrite option if exist
        run("rm -rf {}".format(symbol_path))
        run("ln -s {} {}".format(uncom_path, symbol_path))

        print("New version deployed!")

        return True

    except:
        return False
