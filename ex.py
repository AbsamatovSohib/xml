import xml.etree.ElementTree as ET
mytree = ET.parse("example2.xml")
my_root = mytree.getroot()
# my_root = ET.fromstring(example2_as_string)

print(my_root.tag)

# for x in my_root.findall("PricedItineraries"):
#     # carrier = x.find("Carrier").text
#     print(x[0].tag)