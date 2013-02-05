#!/usr/bin/env python
from alneberg.session2 import fetch_NYC_escalator_info, fraction_escalator_with_repair_status

xml = fetch_NYC_escalator_info()
fraction_escalators = fraction_escalator_with_repair_status(xml)
print fraction_escalators
