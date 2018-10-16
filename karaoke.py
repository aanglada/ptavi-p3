#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import json
import sys


def __str__(lista):
    for etiquetas in lista:
        elementos = []
        for etiqueta in etiquetas:
            if etiqueta != "element" and etiquetas[etiqueta] != "":
                elementos += ("\t", etiqueta, '="', etiquetas[etiqueta], '"')
        print(etiquetas["element"], "".join(elementos))


def to_json(lista, fichero):
    fichjson = fichero.split('.')[0] + '.json'
    json.dump(lista, open(fichjson, 'w'))


def downloadLista(lista):
    for etiquetas in lista:
        for tag in etiquetas:
            if tag == 'src' and etiquetas[tag].startswith('http://'):
                urlretrieve(etiquetas[tag], etiquetas[tag].split('/')[-1])


if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(fichero))
    __str__(sHandler.get_tags())
    to_json(sHandler.get_tags(), fichero)
    downloadLista(sHandler.get_tags())
