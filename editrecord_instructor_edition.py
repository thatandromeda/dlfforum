"""
Base script for DLF Forum 2014 Listening-Based Python workshop.

Modified from files at https://github.com/LibraryCodeYearIG/MARC-record-edit .
"""
# Let's read this code and figure out what it does and why! And
# review syntax as we go.
# Warn them it doesn't 100% work and we're going to debug it.
# Make sure they add comments, IN COMPLETE SENTENCES, as they go.
# Remember declarative and procedural knowledge. They're articulating
# stuff now and doing more of it later. They'll be able to refer back to
# declarations then.
# Be explicit about iterative mental models.

import os
#import codecs
from pymarc import Field, MARCReader, MARCWriter, record_to_xml

records = MARCReader(open('examplerecord.mrc'),
					 to_unicode=True,
					 force_utf8=True,
					 utf8_handling='ignore')

writer_dat = MARCWriter(file('file.dat','a'))
writer_xml = open('file.xml','a')
# This will break when you do the full record set. Walk them through why.
# Mention encoding. Oy. Tell them you found the answer with googling.
# In fact, show them. record_to_xml
# Fix thusly, plus import statement above:
#writer_xml = codecs.open('file.xml', 'a', 'utf-8')
writer_xml.write('<collection>')


for marc in records:

    # See http://oclc.org/support/services/worldcat/documentation/tb/253.en.html
    # for handling of change to 13-digit ISBNs.

    # investigate properties of pymarc by discussion, debugging

    # talk about print statement debugging

    # talk about the fact that it returns an iterable - what does that mean?
    # how could we tell?
    # Play around with lists in the shell if we need to.

    # talk about good variable/function names

    # Modify this to add a try/except after the first time you run it
    # Use that to talk about reading the stacktrace, too

    other_identifier_list = marc.get_fields('024')
    #other_identifier_field = other_identifier_list[0]
    #other_identifier = other_identifier_field.get_subfields('a')

    isbn_list = marc.get_fields('020')
    isbn_field = isbn_list[0]
    isbn = isbn_field.get_subfields('a')[0]

    if len(isbn) == 10:
        isbn = '978' + isbn
        marc.remove_field(isbn_field)
        isbn_field['a'] = isbn
        marc.add_ordered_field(isbn_field)

    # They might notice the add_field / add_ordered_field discrepancy.
    # Look at the XML in your browser and decide what's better.
    marc.add_field(
	Field(
        tag = '590',
        indicators = [' ',' '],
        subfields = [
            'a', 'Donated by the DLF Pythonistas'
        ]))

    # These should be made into a function later. DRY!
    # Also note the single vs double quotes options
    marc.add_field(
    Field(
        tag = '590',
        indicators = [' ',' '],
        subfields = [
            'a', "Library's copy lacks appendices, and also all other pages"
        ]))

    writer_dat.write(marc)
    writer_xml.write(record_to_xml(marc) + "\n")

# Mention file closing hygiene.
writer_dat.close()
writer_xml.write('</collection>')
writer_xml.close()

# If no one notices this line is problematic, bring it up.
# How could we fix that? What are problems that might be caused by the fix?
record_date = '2013-05-02'

# Some better options...:

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('--filename')
#args = parser.parse_args()
#print args.filename

#from datetime import date
#print date.today()

# Note: python string manipulation is the bomb
record_date = record_date.replace("-", "")

os.rename('file.dat', '%s.dat' % record_date)
os.rename('file.xml', '%s.xml' % record_date)

# Ask people what are some modifications they might want to make. Write them
# down against future need.
# Make sure that we're consulting the XML output in so doing.

# Google how to write a good bug report. Pick something reputable, like Mozilla
# or MediaWiki.
# Say a feature request is the same thing: specify inputs and outputs as precisely
# as possible. Let's write a few together before we go on. We need not agree, but
# we should discuss them. And improve them if we can.