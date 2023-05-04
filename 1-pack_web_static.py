#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack.
from datetime import datetime
from fabric.api import local
import os.path
import tarfile


def do_pack():
    """ Creates a tar gzipped archive of the directory web_static """
    d = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(d.year,
                                                         d.month
                                                         d.day
                                                         d.hour
                                                         d.minute
                                                         d.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").format is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
