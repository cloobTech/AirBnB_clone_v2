#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import env, put, run, sudo
import os


# Set environment variables
env.user = 'ubuntu'
env.hosts = ['100.24.74.137', '54.209.138.65'] # IP addresses of your servers
env.key_filename = '~/.ssh/id_rsa' # SSH key file

def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    # Check if archive_path exists
    if not os.path.exists(archive_path):
        return False

    # Get filename without extension
    filename = os.path.basename(archive_path).split('.')[0]

    # Upload archive to /tmp/ directory on servers
    put(archive_path, '/tmp/')

    # Create release directory and uncompress archive
    run('mkdir -p /data/web_static/releases/{}'.format(filename))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(os.path.basename(archive_path), filename))

    # Delete archive from server
    run('rm /tmp/{}'.format(os.path.basename(archive_path)))

    # Move files to proper directory and delete old symlink
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(filename, filename))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))
    run('rm -rf /data/web_static/current')

    # Create new symlink
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(filename))

    print("New version deployed!")
    return True

