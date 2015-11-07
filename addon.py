import xml.etree.ElementTree as ET
import urllib2

tree = ET.ElementTree(file=urllib2.urlopen('http://192.168.1.119:8111/JMMServerPlex/GetFilters/Default'))

root = tree.getroot()

for child in root.findall('Directory'):
  title = child.get('title')
  key = child.get('key')
  leafcount = child.get('leafCount')
  print title
  print key[17:].decode("hex")
  print leafcount

