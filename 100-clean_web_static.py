#!/usr/bin/python3
# A Fabric script that generates a .tgz archive
from fabric.api import *
import os


env.hosts = ['54.234.63.33', '18.234.193.44']


def def do_clean(number=0):
    """ Deletes out-of-date archives """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
