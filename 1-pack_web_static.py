#!/usr/bin/python3
"""packs web_static into an archive"""
from fabric.api import *
import datetime


def do_pack():
    """archives the web_static folder
    """
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    command = local("tar -czvf versions/web_static_{}.tgz web_static"
               .format(time))
    if command.failed:
        return None
    else:
        return command
