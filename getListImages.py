"""
Module for dealing with the fetching of all the file names in the `images` folder
"""
from os import listdir
from os.path import isfile, join
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read('config.cfg')

def returnNameExt(fileName: str): return fileName.split('.')    # needs to be a file to not get errors


def getListImages(basePath) -> list[dict[str, str]]:
    """Return list[dict[`image_path`: `<path>`, `caption`: `<caption>`]]"""
    
    return [
        dictObjectElement(basePath, file)
        for file in listdir(basePath)   # We can put images from any directory using this
        if checkExt(basePath, file)
    ]


def dictObjectElement(basepath, fileName) -> dict[str, str]:
    """Return dict[`image_path`: `<path>`, `caption`: `<caption>`]"""
    return {
        'image_path': join(basepath, fileName),
        'caption': returnNameExt(fileName)[0]
    }


def checkExt(basePath: str, fileName: str) -> bool:
    """Will return true if filename has any of the accepted extensions defined
    in config.cfg `ext` is file extension of file"""
    
    if not isfile(join(basePath, fileName)):
        return False
         
    ext = returnNameExt(fileName)[-1].lower()
    return ext in cfg['Gallery']['exts']
