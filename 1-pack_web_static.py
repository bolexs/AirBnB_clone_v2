#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the folder"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Function to compress files"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        dates = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(dates)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None
