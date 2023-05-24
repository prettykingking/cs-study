"""Report disk usage
"""

import os


def disk_usage(path):
    """Return the number of bytes used by a file or directory and any descendants."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child = os.path.join(path, filename)
            total += disk_usage(child)
    print("{0:<7}".format(total), path)
    return total

disk_usage('/usr/local/bin')
