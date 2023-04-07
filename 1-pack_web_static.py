#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive"""
    try:
        # create the folder if it doesn't exist
        local("mkdir -p versions")
        # create the file name
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        # create the archive using tar
        local("tar -czvf versions/{} web_static".format(file_name))
        # return the path to the archive
        return "versions/{}".format(file_name)
    except:
        return None
