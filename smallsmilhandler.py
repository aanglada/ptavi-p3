#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

        def __init__(self):

            self.elementos = []
            self.tags = ["root-layout", "region", "img", "audio", "textstream"]
            self.atributos = {
                "root-layout": ["width", "height", "background-color"],
                "region": ["id", "top", "bottom", "left", "right"],
                "img": ["src", "region", "begin", "dur"],
                "audio": ["src", "begin", "dur"],
                "textstream": ["src", "region"]
                }

        def startElement(self, name, attrs):

            self.diccionario = {}
            if name in self.tags:
                self.diccionario['etiqueta'] = name
                for atributo in self.atributos[name]:
                    self.diccionario[atributo] = attrs.get(atributo, "")
                self.elementos.append(self.diccionario)

        def get_tags(self):

            return self.elementos

if __name__ == "__main__":

    parser = make_parser()
    myHandler = SmallSMILHandler()
    parser.setContentHandler(myHandler)
    parser.parse(open('karaoke.smil'))
    print(myHandler.get_tags())
