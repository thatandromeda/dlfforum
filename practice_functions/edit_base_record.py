"""
Base script for DLF Forum 2014 Listening-Based Python workshop.

Modified from files at https://github.com/LibraryCodeYearIG/MARC-record-edit .
"""

import os
from pymarc import Field, MARCReader, MARCWriter, record_to_xml

records = MARCReader(open('examplerecord.mrc'),
                     to_unicode=True,
                     force_utf8=True,
                     utf8_handling='ignore')

writer_dat = MARCWriter(file('examplerecord_3.dat','a'))
writer_xml = open('examplerecord_3.xml','a')


for marc in records:

    isbn_list = marc.get_fields('020')
    isbn_field = isbn_list[0]
    isbn = isbn_field.get_subfields('a')[0]

    isbn = '97' + isbn
    marc.remove_field(isbn_field)
    isbn_field['a'] = isbn
    marc.add_ordered_field(isbn_field)

    writer_dat.write(marc)
    writer_xml.write(record_to_xml(marc) + "\n")

writer_dat.close()
writer_xml.close()
