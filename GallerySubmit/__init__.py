"""Simple Module to upload all the images/gifs in a file in a specific subreddit

Since we're only going to upload media to reddit, we don't need to form a reddit instance
until we're ready to upload.

All the code before the creation of the instance aims to find and resolve the file names and their paths
to be uploaded to reddit. 

The account that would upload the image, the directory that contains the required images, all that information
is within the configuration file `config.cfg`.

NOTE: The caption of the media uploaded will be the same as it's filename, so make sure to change it to your
liking before running the code.
NOTE: For now the code does not resolve the filenames to something meaningful. So name the file with whitespaces."""
from os import listdir
from typing import Union
from os.path import isfile, join, dirname

import praw
from praw.reddit import Subreddit
from praw.models.helpers import SubredditHelper

from configparser import ConfigParser


cfg = ConfigParser()
cfg.read(join(dirname(__file__), "config.cfg"))

#For dealing with the fetching of all the file names in the `images` folder
def __returnNameExt(fileName: str): return fileName.split('.')    # needs to be a file to not get errors


def __getListImages(basePath) -> list[dict[str, str]]:
    """Return list[dict[`image_path`: `<path>`, `caption`: `<caption>`]]"""
    
    return [
        __dictObjectElement(basePath, file)
        for file in listdir(basePath)   # We can put images from any directory using this
        if __checkExt(basePath, file)
    ]


def __dictObjectElement(basepath, fileName) -> dict[str, str]:
    """Return dict[`image_path`: `<path>`, `caption`: `<caption>`]"""
    return {
        'image_path': join(basepath, fileName),
        'caption': __returnNameExt(fileName)[0]
    }


def __checkExt(basePath: str, fileName: str) -> bool:
    """Will return true if filename has any of the accepted extensions defined
    in config.cfg `ext` is file extension of file"""
    
    if not isfile(join(basePath, fileName)):
        return False
         
    ext = __returnNameExt(fileName)[-1].lower()
    return ext in cfg['Gallery']['exts']

# Initializing the Reddit instance
reddit = praw.Reddit(
    client_id = cfg['DEFAULT']['client_id'],
    client_secret = cfg['DEFAULT']['client_secret'],
    user_agent = cfg['DEFAULT']['user_agent'],
    username = cfg['OAuth']['username'],
    password = cfg['OAuth']['password'],
)

subreddit: Union[SubredditHelper, Subreddit] = reddit.subreddit(cfg['Sub']['name'])
subreddit.submit_gallery(cfg['Gallery']['title'], __getListImages(cfg['Gallery']['path']))
