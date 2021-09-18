from configparser import ConfigParser


def getSectionKeyList(cfg: ConfigParser, sectionName: str) -> list[str]:
    keyList = []
    section = cfg[sectionName]
    
    for key in section.keys():
        keyList.append(section[key])

    return keyList