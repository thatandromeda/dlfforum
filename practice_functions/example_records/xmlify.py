"""
Base script for DLF Forum 2014 Listening-Based Python workshop.

Modified from files at https://github.com/LibraryCodeYearIG/MARC-record-edit .
"""

import os
from pymarc import Field, MARCReader, MARCWriter, record_to_xml

for i in range(10, 20):
    filename = 'examplerecord_%s.dat' % i
    filename_xml = 'examplerecord_%s.xml' % i

    records = MARCReader(open(filename),
                         to_unicode=True,
                         force_utf8=True,
                         utf8_handling='ignore')

    writer_xml = open(filename_xml,'a')
    writer_xml.write('<collection>')

    for marc in records:

        writer_xml.write(record_to_xml(marc) + "\n")

    writer_xml.write('</collection>')
    writer_xml.close()
