#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repO
"""

from fabric import task
from fabric import Connection
from datetime import datetime

@task
def do_pack(c):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    versions_folder = "versions"
    web_static_folder = "web_static"
    archive_path = f"{versions_folder}/{archive_name}"

    # Create the versions folder if it doesn't exist
    c.run(f"mkdir -p {versions_folder}")

    # Create the archive
    result = c.run(f"tar -czvf {archive_path} {web_static_folder}")

    if result.ok:
        return archive_path
    else:
        return None

