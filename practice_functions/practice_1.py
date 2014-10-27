from pymarc import Field, MARCReader, MARCWriter, record_to_xml

# This will loop through our example files so that you can test different cases.
# You should have a look at the XML files in the example_records directory in your
# own browser and think about the behavior you expect to see.
for i in range(10, 20):
    filename = 'example_records/examplerecord_%s.dat' % i

    records = MARCReader(open(filename),
                         to_unicode=True,
                         force_utf8=True,
                         utf8_handling='ignore')

    # This line is here purely to help you understand and debug the program
    # output. print statements are often removed from programs before they
    # are finalized and shared, but they're incredibly useful during
    # development. And depending on what you need your program to do, they 
    # may be all the output you need!
    print "\n\n--> Examining record %s... \n" % filename

    for marc in records:
        # If the ISBN is 10 digits long, print "10 digits".
        # If it's 13 digits long, print "13 digits".
        # Otherwise, print some kind of warning message.

        # By the way, if you just want to *look* at fields in pymarc, and don't
        # need to modify them, you can use a shorthand like this:
        # "marc['020']['a']" will give you subfield a of field 020.
        # This will only work if there IS a field 020, and only one field 020, 
        # and it has a subfield a, though. Can you imagine some cases where
        # you wouldn't be guaranteed that a MARC field would exist, or where
        # there might be more than one of it?
