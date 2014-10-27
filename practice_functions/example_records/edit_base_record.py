"""
Base script for DLF Forum 2014 Listening-Based Python workshop.

Modified from files at https://github.com/LibraryCodeYearIG/MARC-record-edit .
"""

import os
from pymarc import Field, MARCReader, MARCWriter, record_to_xml

records = MARCReader(open('../../exampledump.mrc'),
                     to_unicode=True,
                     force_utf8=True,
                     utf8_handling='ignore')

index = 1

for marc in records:
    filename_dat = 'examplerecord_%s.dat' % index
    filename_xml = 'examplerecord_%s.xml' % index

    writer_dat = MARCWriter(file(filename_dat,'a'))
    writer_xml = open(filename_xml,'a')

    writer_dat.write(marc)
    writer_xml.write(record_to_xml(marc) + "\n")

    writer_dat.close()
    writer_xml.close()

    index += 1
