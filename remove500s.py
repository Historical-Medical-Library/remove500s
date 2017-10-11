import os
import csv
from bs4 import BeautifulSoup as bs

#removes all 500 fields from MARC XML except 520 ind 3 (abstract)
for file in os.listdir('C:/path/to/MARCXML'):
    xmlTemp = open(('C:/path/to/MARCXML' + file), 'r', encoding='utf8')
    xmlString = xmlTemp.read()
    xmlTemp.close()
    soup = bs(xmlString, 'lxml')
    if soup.find('datafield', tag='500') is not None:
        soup.find('datafield', tag='500').decompose()
    if soup.find('datafield', tag='501') is not None:
        soup.find('datafield', tag='501').decompose()
    if soup.find('datafield', tag='502') is not None:
        soup.find('datafield', tag='502').decompose()
    if soup.find('datafield', tag='504') is not None:
        soup.find('datafield', tag='504').decompose()
    if soup.find('datafield', tag='506') is not None:
        soup.find('datafield', tag='506').decompose()
    if soup.find('datafield', tag='507') is not None:
        soup.find('datafield', tag='507').decompose()
    if soup.find('datafield', tag='508') is not None:
        soup.find('datafield', tag='508').decompose()
    if soup.find('datafield', tag='510') is not None:
        soup.find('datafield', tag='510').decompose()
    if soup.find('datafield', tag='511') is not None:
        soup.find('datafield', tag='511').decompose()
    if soup.find('datafield', tag='513') is not None:
        soup.find('datafield', tag='513').decompose()
    if soup.find('datafield', tag='514') is not None:
        soup.find('datafield', tag='514').decompose()
    if soup.find('datafield', tag='518') is not None:
        soup.find('datafield', tag='518').decompose()
    if soup.find('datafield', ind1='0', ind2=' ', tag='520') is not None:
        soup.find('datafield', ind1='0', ind2=' ', tag='520').decompose()
    if soup.find('datafield', ind1='1', ind2=' ', tag='520') is not None:
        soup.find('datafield', ind1='1', ind2=' ', tag='520').decompose()
    if soup.find('datafield', ind1='2', ind2=' ', tag='520') is not None:
        soup.find('datafield', ind1='2', ind2=' ', tag='520').decompose()
    if soup.find('datafield', ind1='8', ind2=' ', tag='520') is not None:
        soup.find('datafield', ind1='8', ind2=' ', tag='520').decompose()
    if soup.find('datafield', tag='521') is not None:
        soup.find('datafield', tag='521').decompose()
    if soup.find('datafield', tag='522') is not None:
        soup.find('datafield', tag='522').decompose()
    if soup.find('datafield', tag='524') is not None:
        soup.find('datafield', tag='524').decompose()
    if soup.find('datafield', tag='530') is not None:
        soup.find('datafield', tag='530').decompose()
    if soup.find('datafield', tag='533') is not None:
        soup.find('datafield', tag='533').decompose()
    if soup.find('datafield', tag='534') is not None:
        soup.find('datafield', tag='534').decompose()
    if soup.find('datafield', tag='535') is not None:
        soup.find('datafield', tag='535').decompose()
    if soup.find('datafield', tag='536') is not None:
        soup.find('datafield', tag='536').decompose()
    if soup.find('datafield', tag='538') is not None:
        soup.find('datafield', tag='538').decompose()
    if soup.find('datafield', tag='540') is not None:
        soup.find('datafield', tag='540').decompose()
    if soup.find('datafield', tag='541') is not None:
        soup.find('datafield', tag='541').decompose()
    if soup.find('datafield', tag='544') is not None:
        soup.find('datafield', tag='544').decompose()
    if soup.find('datafield', tag='545') is not None:
        soup.find('datafield', tag='545').decompose()
    if soup.find('datafield', tag='546') is not None:
        soup.find('datafield', tag='546').decompose()
    if soup.find('datafield', tag='555') is not None:
        soup.find('datafield', tag='555').decompose()
    if soup.find('datafield', tag='561') is not None:
        soup.find('datafield', tag='561').decompose()
    if soup.find('datafield', tag='562') is not None:
        soup.find('datafield', tag='562').decompose()
    if soup.find('datafield', tag='563') is not None:
        soup.find('datafield', tag='563').decompose()
    if soup.find('datafield', tag='581') is not None:
        soup.find('datafield', tag='581').decompose()
    xmlTemp = open('H:/Library/ArchivesSpace/cpparchives.org_MARCXML_soup/' + file, 'w', encoding='utf8')
    xmlTemp.write(str(soup))
    xmlTemp.close()
