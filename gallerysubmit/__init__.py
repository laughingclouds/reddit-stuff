"""Simple Module to upload all the images/gifs in a file in a specific subreddit

Since we're only going to upload media to reddit, we don't need to form a reddit instance
until we're ready to upload.

All the code before the creation of the instance aims to find and resolve the file names and their paths
to be uploaded to reddit. 

The account that would upload the image, the directory that contains the required images, all that information
is within the configuration file `config.cfg`.

NOTE: The caption of the media uploaded will be the same as its filename, so make sure to change it to your
liking before running the code.
NOTE: For now the code does not resolve the filenames to something meaningful. So name the file with whitespaces."""
from os import listdir
from os.path import isfile, join
from configparser import ConfigParser

from praw.models import Submission

from utils.models import sub, dictStr, listDictStr
from utils.configworker import getSectionKeyList


__cfg = ConfigParser()
__cfg.read("config/gallerysubmit.cfg")

#For dealing with the fetching of all the file names in the `images` folder
def __returnNameExt(fileName: str): return fileName.split('.')    # needs to be a file to not get errors


def __getListImages(basePath) -> listDictStr:
    """Return list[dict[`image_path`: `<path>`, `caption`: `<caption>`]]"""
    
    return [
        __dictObjectElement(basePath, file)
        for file in listdir(basePath)   # We can put images from any directory using this
        if __checkExt(basePath, file)
    ]


def __dictObjectElement(basepath, fileName) -> dictStr:
    """Return dict[`image_path`: `<path>`, `caption`: `<caption>`]"""
    return {
        'image_path': join(basepath, fileName),
        'caption': __returnNameExt(fileName)[0]
    }


def __checkExt(basePath: str, fileName: str) -> bool:
    """Will return true if filename has any of the accepted extensions defined
    in config.__cfg `ext` is file extension of file"""
    
    if not isfile(join(basePath, fileName)):
        return False
         
    ext = __returnNameExt(fileName)[-1].lower()
    return ext in __cfg['Gallery']['exts']
    

def gallerySubmit(subreddit: sub) -> Submission:
    """Takes a `Subreddit` instance\n
    Uses `__getListImages()` to get the info on the images to submit
    Finally calls `submit_gallery()` to submit."""

    return subreddit.submit_gallery(
        __cfg['Gallery']['title'], __getListImages(__cfg['Gallery']['path'])
    )

subNames = getSectionKeyList(__cfg, 'Sub')
