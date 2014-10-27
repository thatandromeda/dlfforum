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
        # Once you've got practice_1 working...
        # If the ISBN is 13 digits and does not start with 978, print a warning.
        # For this, you will find the function "startswith" handy. It works like this:
        # your_string.startswith('letters') returns True if your_string starts
        # with the characters 'letters' and False if it does not.
        # Examples:
        # 'cronuts'.startswith('c')
        # >>> True
        # 'cronuts'.startswith('cr')
        # >>> True
        # 'cronuts'.startswith('Cr')
        # >>> False
        # 'cronuts'.startswith('7')
        # >>> False

        # Once you've got that working...
        # You can provide additional validation, if you like, with the isdigit()
        # function (google "python isdigit" or  "python isdigit example").

        # If you *really* want to make sure this is an ISBN, instead of just flagging
        # obvious mistakes, you'll need something that checks all the rules for ISBNs.
        # Someone has probably already written this for you; google for "python isbn
        # library" or "python isbn validation" and use theirs rather than writing
        # your own.
