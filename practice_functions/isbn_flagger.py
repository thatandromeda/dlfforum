from pymarc import Field, MARCReader, MARCWriter, record_to_xml

records = MARCReader(open('examplerecord.mrc'),
                     to_unicode=True,
                     force_utf8=True,
                     utf8_handling='ignore')

for marc in records:
	# If the ISBN is 10 digits long, print "10 digits".
	# If it's 13 digits long, print "13 digits".
	# Otherwise, print some kind of warning message.

	# Once you've got that working...
	# If the ISBN is 13 digits and does not start with 978, print a warning.
	# For this, you will find the function "startswith" handy. It works like this:
	# your_string.startswith('letters') returns True if your_string starts
	# with the characters 'letters' and False if it does not.

	# Once you've got that working, you can provide additional validation, if you
	# like, with the isdigit() function (google "python isdigit" or 
	# "python isdigit example").

	# If you *really* want to make sure this is an ISBN, instead of just flagging
	# obvious mistakes, you'll need something that checks all the rules. Someone 
	# has probably already written this for you; google for "python isbn library"
	# or "python isbn validation" and use theirs rather than writing your own.
