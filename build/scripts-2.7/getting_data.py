#!/home/johannes/.virtualenvs/py2.7/bin/python
import alneberg

xml = alneberg.fetch_NYC_escalator_info()
fraction_escalators = alneberg.fraction_escalator_with_repair_status(xml)
print fraction_escalators
