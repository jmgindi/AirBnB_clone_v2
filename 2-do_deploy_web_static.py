#!/usr/bin/python3
"""packs web_static into an archive"""
from fabric.api import *
import datetime
import os

env.hosts = ["35.237.8.203", "34.73.52.180"]
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """ deploys web_static.tgz to the web servers
    """
    if not archive_path:
        return False

    status = put(archive_path, "/tmp")
    if status.failed:
        return False

    server_path = archive_path.split("/")[-1].split('.')[0]
    status_2 = run("mkdir -p /data/web_static/releases/{}/".format(server_path))
    if status_2.failed:
        return False

    run(
        "tar -xzf /tmp/{}".format(server_path + ".tgz") +
        " -C /data/web_static/releases/{}/".format(server_path)
    )
    run("rm -rf /tmp/{}".format(server_path))
    run(
        "mv /data/web_static/releases/{}/web_static/* ".format(server_path) +
        "/data/web_static/releases/{}/".format(server_path)
    )

    status_3 = run(
        "rm -rf /data/web_static/releases/{}/web_static"
        .format(server_path)
    )
    if status_3.failed:
        return False

    status_4 = run("rm -rf /data/web_static/releases/{}/web_static"
                   .format(server_path))
    if status_4.failed:
        return False

    status_5 = run(
        "ln -sf /data/web_static/releases/{}/ /data/web_static/current"
        .format(server_path)
    )
    if status_5.failed:
        return False

    return True
