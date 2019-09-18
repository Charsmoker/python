from xml.dom import minidom
import os
import shutil

class AutoTiledAtlas(object):
    def __init__(self, path, name):
        dom = minidom.parse(path + "/" + name)
        root = dom.documentElement
        content = root.childNodes
        for v in content:
            if v.nodeType == v.ELEMENT_NODE and v.nodeName == "tileset":
                tsname = v.getAttribute("name")
                subdir = path + "/" + tsname
                print "subdir=" + subdir
                if not os.path.exists(subdir):
                    print "making:" + tsname
                    os.makedirs(subdir)
                for t in v.childNodes:
                    if t.nodeType == t.ELEMENT_NODE and t.nodeName == "tile":
                        source = t.getElementsByTagName("image")[0].getAttribute("source")
                        shutil.copy (path + "/" + source + ".png", subdir)

if __name__ == "__main__":
    AutoTiledAtlas("assets/resources/res/warMap/tmx", "worldTMX.tmx")
    AutoTiledAtlas("assets/resources/res/warMap/tmx", "shadow.tmx")
