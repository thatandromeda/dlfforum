from pymarc import Field, MARCReader, MARCWriter, record_to_xml

favorite_countries = ['Sweden', 'England', 'Spain']
favorite_subjects = ['Sweden', 'Science fiction', 'Langland, William',
                     'English Literature']

# This will loop through our example files so that you can test different cases.
for i in range(10, 20):
    filename = 'example_records/examplerecord_%s.dat' % i

    records = MARCReader(open(filename),
                         to_unicode=True,
                         force_utf8=True,
                         utf8_handling='ignore')

    print "\n\n--> Examining record %s... \n" % filename
    for marc in records:
        # subjects() is a convenience function that will get all the fields
        # that might be subject entries.  See its definition in
        # https://github.com/edsu/pymarc/blob/master/pymarc/record.py for
        # details.
        subject_list = marc.subjects()

        # Replace the following comments with code...
        # Loop through the subject list
        # Look at subfield a (if your loop variable is named "subject", 
        # you can do this with "subject['a']")
        # If subfield a is in favorite_countries, print a helpful notification

        # Once you've got that working...
        # Modify the code to check if subfield a is in favorite_subjects instead.
        # Does this yield the behavior you expect? Why or why not? Compare notes
        # with someone else and see if you had the same expectations.
