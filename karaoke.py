#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


def __str__(lista):
    for etiquetas in lista:
        elementos = []
        for etiqueta in etiquetas:
            if etiqueta != "element" and etiquetas[etiqueta] != "":
                elementos += ("\t", etiqueta, '="', etiquetas[etiqueta], '"')
        print(etiquetas["element"], "".join(elementos))

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(fichero)
    __str__(sHandler.get_tags())
