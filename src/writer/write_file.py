import logging
import csv
import xml.etree.ElementTree as ET
from config import UPLOAD_FOLDER


def create_xml_file(data, file_name):
    """data is of type Response"""
    try:
        with open(UPLOAD_FOLDER+'/'+file_name, 'wb') as file:
            root = ET.fromstring(data.text)
            logging.info('root :', root)
            tree = ET.ElementTree(root)
            tree.write(file, encoding='UTF-8', xml_declaration=True)
    except IOError as e:
        return e.args

    
def create_csv_file(data, file_name):
    """data is of type Response"""
    with open(UPLOAD_FOLDER+'/'+file_name, 'wt') as file:
        writer = csv.writer(file, quotechar="'")
        for line in data.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))