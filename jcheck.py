from jnpr.junos import Device
import pprint
import json
from lxml import etree

if __name__ == '__main__':
    with  Device(host='1.1.1.1', user='username', passwd='passw') as dev:
        #print(json.dumps(dev.facts))
        #print(dev.facts["version"])
        print(dev.display_xml_rpc('show chassis routing-engine', format='text'))
        infotext = dev.rpc.get_software_information({'format':'text'})
        print(etree.tostring(infotext, encoding='unicode'))
