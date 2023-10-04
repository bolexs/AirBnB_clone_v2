#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
import os
import shlex

env.hosts = ['54.173.237.68', '54.157.161.250']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """deploys the archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        no_ext = name.replace('.', ' ')
        no_ext = shlex.split(no_ext)
        no_ext = no_ext[0]

        releases = '/data/web_static/releases/{}/'.format(no_ext)
        tmp_path = '/tmp/{}'.format(name)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases))
        run('tar -xzf {} -C {}'.format(tmp_path, releases))
        run('rm {}'.format(tmp_path))
        run('mv {}web_static/* {}'.format(releases, releases))
        run('rm -rf {}web_static'.format(releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases))
        return True
    except:
        return False
