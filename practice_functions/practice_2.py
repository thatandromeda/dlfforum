from pymarc import Field, MARCReader, MARCWriter, record_to_xml

# This will loop through our example files so that you can test different cases.
for i in range(10,20):
	filename = 'example_records/examplerecord_%s.dat' % i

	records = MARCReader(open(filename),
	                     to_unicode=True,
	                     force_utf8=True,
	                     utf8_handling='ignore')

	print "\n\n--> Examining record %s... \n" % filename
	for marc in records:
		# Look at the values in the 041 field.  If any of them aren't
		# 'eng', print out a warning that this record might need review by
		# a specialized cataloger.

		# Make sure to check your output against the records; are you
		# getting the results you expect?

		# Once you've got that working, see if you can print out different
		# warnings for different languages. You'll have to do some planning
		# ahead here: what languages do you see in your data set? What type of
		# review does each language need? (Feel free to make up fake cataloger
		# names.)
		
		# Once you've got that working, flag down the instructor or work
		# with a fellow student to see if you can make your solution more
		# elegant.

