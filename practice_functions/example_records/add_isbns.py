"""
Base script for DLF Forum 2014 Listening-Based Python workshop.

Modified from files at https://github.com/LibraryCodeYearIG/MARC-record-edit .
"""

import os
from pymarc import Field, MARCReader, MARCWriter, record_to_xml

isbns = ['025710491', '8105610391', '9781041740192', '9791037492192',
         '1049126950', '819251', '4018597182', '978103784952X',
         '1023894675102', '910384765']

for i in range(10, 20):
    filename = 'examplerecord_%s.dat' % i 
    filename_xml = 'examplerecord_%s.xml' % i 
    filename_out = 'examplerecord_%s.out' % i 

    records = MARCReader(open(filename),
                         to_unicode=True,
                         force_utf8=True,
                         utf8_handling='ignore')

    writer_dat = MARCWriter(file(filename_out,'a'))
    writer_xml = open(filename_xml,'a')

    for marc in records:

        isbn_list = marc.get_fields('020')
        try:
            isbn_field = isbn_list[0]
        except Exception, e:
            j = i - 10
            marc.add_ordered_field(
                Field(
                    tag='020',
                    indicators=[' ', ' '],
                    subfields = ['a', isbns[j]]
                    ))

        writer_dat.write(marc)
        writer_xml.write(record_to_xml(marc) + "\n")

    writer_dat.close()
    writer_xml.close()
