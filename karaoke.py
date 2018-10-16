#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import json
import sys


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

    def __str__(self):
        for etiquetas in self.lista:
            elementos = []
            for etiqueta in etiquetas:
                if etiqueta != "element" and etiquetas[etiqueta] != "":
                    elementos += ("\t", etiqueta, '="', etiquetas[etiqueta], '"')
            print(etiquetas["element"], "".join(elementos))


    def to_json(self, fichero, jfichero):
        if jfichero == "":
            jfichero = fichero.split(".")[0] + ".json"
        json.dump([self.lista], open(jfichero, "w"))


    def do_local(self):
        for etiquetas in self.lista:
            for tag in etiquetas:
                if tag == 'src' and etiquetas[tag].startswith('http://'):
                    urlretrieve(etiquetas[tag], etiquetas[tag].split('/')[-1])
                    etiquetas[tag] = etiquetas[tag].split('/')[-1]

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")
    karaoke = KaraokeLocal(fichero)
    karaoke.__str__()
    karaoke.to_json(fichero, '')
    karaoke.do_local()
    karaoke.to_json(fichero, "local.json")
    karaoke.__str__()
