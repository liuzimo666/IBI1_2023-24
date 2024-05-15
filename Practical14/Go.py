import xml.etree.ElementTree as ET
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import matplotlib.pyplot as plt
import datetime

# Define a SAX ContentHandler to parse the XML file
class GOCountHandler(ContentHandler):
    def __init__(self):
        self.counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.current_ontology = None

    def startElement(self, tag, attributes):
        if tag == 'namespace':
            self.current_ontology = attributes.get('id', '').lower()

    def endElement(self, tag):
        if tag == 'term':
            if self.current_ontology:
                self.counts[self.current_ontology] += 1
            self.current_ontology = None

    def getCounts(self):
        return self.counts

# The definition function parses the XML file using the DOM API
def parse_xml_dom(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    for child in root:
        if child.tag == 'namespace':
            ontology = child.get('id').lower()
            if ontology in counts:
                counts[ontology] += len(child.findall('term'))
    return counts

# The definition function parses XML files using the SAX API
def parse_xml_sax(xml_file):
    parser = make_parser()
    handler = GOCountHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    return handler.getCounts()

# Measure and record time
def measure_time(func, *args):
    start_time = datetime.datetime.now()
    result = func(*args)
    end_time = datetime.datetime.now()
    return result, end_time - start_time

xml_file = 'go_obo.xml'

# Parsing using the DOM API
dom_counts, dom_time = measure_time(parse_xml_dom, xml_file)

# Parsing using the SAX API
sax_counts, sax_time = measure_time(parse_xml_sax, xml_file)

# Print result
print(f"DOM API counts: {dom_counts}")
print(f"SAX API counts: {sax_counts}")

# Plot the result
labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
dom_bars = dom_counts.values()
sax_bars = sax_counts.values()

plt.figure(figsize=(10, 6))
plt.bar(labels, dom_bars, label='DOM API')
plt.bar(labels, sax_bars, label='SAX API', alpha=0.5)
plt.legend()
plt.title('GO Term Counts in Each Ontology')
plt.show()

# Record the time and compare
print(f"DOM API time: {dom_time}")
print(f"SAX API time: {sax_time}")
if dom_time < sax_time:
    print("DOM API was faster.")
else:
    print("SAX API was faster.")