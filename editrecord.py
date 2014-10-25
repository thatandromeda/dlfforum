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

writer_dat = MARCWriter(file('file.dat','a'))
writer_xml = open('file.xml','a')
writer_xml.write('<collection>')


for marc in records:

    other_identifier_list = marc.get_fields('024')
    other_identifier_field = other_identifier_list[0]
    other_identifier = other_identifier_field.get_subfields('a')

    isbn_list = marc.get_fields('020')
    isbn_field = isbn_list[0]
    isbn = isbn_field.get_subfields('a')[0]

    if len(isbn) == 10:
        isbn = '978' + isbn
        marc.remove_field(isbn_field)
        isbn_field['a'] = isbn
        marc.add_ordered_field(isbn_field)

    marc.add_field(
    Field(
        tag = '590',
        indicators = [' ',' '],
        subfields = [
            'a', 'Donated by the DLF Pythonistas'
        ]))

    writer_dat.write(marc)
    writer_xml.write(record_to_xml(marc) + "\n")

writer_dat.close()
writer_xml.write('</collection>')
writer_xml.close()

record_date = '2013-05-02'

record_date = record_date.replace("-", "")

os.rename('file.dat', '%s.dat' % record_date)
os.rename('file.xml', '%s.xml' % record_date)
