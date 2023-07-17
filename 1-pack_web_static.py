#!/usr/bin/python3
"""
This script contains the `do_pack` function, which generates a compressed archive file (.tgz)
from the contents of the `web_static` folder using the Fabric library.
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a compressed archive (.tgz) from the contents of the `web_static` folder
    using the Fabric library.

    Returns:
        str: The filename of the generated archive if successful, otherwise None.
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None

