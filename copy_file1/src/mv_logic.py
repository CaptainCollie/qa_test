import xml.etree.ElementTree as ET
import os
import shutil
from pathlib import Path


def read_config(file):
    tree = ET.parse(file)
    return tree.findall('file')


def move(file):
    files = read_config(file)
    for file in files:
        items = list(file.items())
        src_pth = Path(items[0][1], items[2][1])
        destination_pth = Path(items[1][1], items[2][1])

        if os.path.exists(src_pth) and not destination_pth:
            shutil.copy(src_pth, destination_pth)



