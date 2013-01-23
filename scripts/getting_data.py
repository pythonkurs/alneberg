#!/usr/bin/env python
import alneberg

xml_url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
xml = alneberg.fetch_xml(xml_url)
fraction_escalators = alneberg.fraction_escalator_with_repair_status(xml)
print fraction_escalators
