import xml.etree.ElementTree as ET

def read_xml_file():
    f = ET.parse("orders.xml")
    root = f.getroot()
    for order in root:
        print(order.tag, ' - ', order.attrib)
        for child in order:
            print(child.text)
        
def update_xml_file():
    f = ET.parse("orders.xml")
    root = f.getroot()
    for order in root:
        if order.attrib['id'] == '2':
            root.remove(order)
    f.write("orders.xml")
    #f.close()
    
#read_xml_file()
update_xml_file()