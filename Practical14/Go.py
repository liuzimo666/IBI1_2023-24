import xml.dom.minidom as minidom
import xml.sax as sax
from datetime import datetime
import matplotlib.pyplot as plt

# Define the handler for SAX
class GOHandler(sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.counts = {"molecular_function": 0, "biological_process": 0, "cellular_component": 0}

    def startElement(self, tag, attributes):
        self.current_data = tag

    def characters(self, content):
        if self.current_data == "namespace":
            self.namespace = content.strip()

    def endElement(self, tag):
        if tag == "namespace" and self.namespace in self.counts:
            self.counts[self.namespace] += 1
        self.current_data = ""

# Function to parse using DOM
def parse_with_dom(file_path):
    counts = {"molecular_function": 0, "biological_process": 0, "cellular_component": 0}
    dom_tree = minidom.parse(file_path)
    terms = dom_tree.getElementsByTagName("term")
    for term in terms:
        namespaces = term.getElementsByTagName("namespace")
        for ns in namespaces:
            namespace = ns.childNodes[0].data.strip()
            if namespace in counts:
                counts[namespace] += 1
    return counts

# Function to parse using SAX
def parse_with_sax(file_path):
    handler = GOHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler.counts

# Main function
def main():
    file_path = 'go_obo.xml'

    # Time and parse with DOM
    start_time = datetime.now()
    dom_counts = parse_with_dom(file_path)
    dom_duration = datetime.now() - start_time

    # Time and parse with SAX
    start_time = datetime.now()
    sax_counts = parse_with_sax(file_path)
    sax_duration = datetime.now() - start_time

    # Print results
    print("DOM counts:", dom_counts)
    print("SAX counts:", sax_counts)
    print("DOM duration:", dom_duration)
    print("SAX duration:", sax_duration)
    
    # Comment on which one ran fastest
    if dom_duration < sax_duration:
        print("DOM was faster")
    else:
        print("SAX was faster")

    # Plotting the results
    labels = list(dom_counts.keys())
    dom_values = list(dom_counts.values())
    sax_values = list(sax_counts.values())

    x = range(len(labels))
    
    fig, ax = plt.subplots()
    ax.bar(x, dom_values, width=0.4, label='DOM', align='center')
    ax.bar(x, sax_values, width=0.4, label='SAX', align='edge')
    
    ax.set_xlabel('Ontology')
    ax.set_ylabel('Number of GO Terms')
    ax.set_title('GO Terms Count in Ontologies')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()