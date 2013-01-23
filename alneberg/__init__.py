import untangle
import requests

def fetch_xml(url):
    r = requests.get(url)
    return r.text


def fraction_escalator_with_repair_status(xml_raw):
    doc = untangle.parse(xml_raw)
    outages = doc.NYCOutages.outage
    escalator_count = 0
    repair_escalator_count = 0
    
    for outage in outages:
        if outage.equipmenttype.cdata == 'ES':
            escalator_count += 1
            if outage.reason.cdata == 'REPAIR':
                repair_escalator_count += 1
    
    fraction = repair_escalator_count/float(escalator_count)        
    return fraction
