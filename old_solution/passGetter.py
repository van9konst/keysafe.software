import sys

__author__ = 'name'
from lxml import etree

tree = etree.parse('2.xml')
notes = etree.fromstring(etree.tostring(tree))

get_key_number = '5'
arr = []

for cells in notes.getchildren():
    try:
        if cells.getchildren()[0].text == get_key_number:
            for cell in cells.getchildren()[1:]:
                print(cell.text)
                if cell.text.isdigit:
                    arr.append(int(cell.text))
    except :
        print(sys.exc_info())

for item in arr:
    print("item: " + str(item))
for item in arr[::-1]:
    print("item: " + str(item * (-1)))
