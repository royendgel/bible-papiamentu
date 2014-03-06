from csv import reader
import os , glob
books = glob.glob('csvbible/*.csv')
# books = ["csvbible/1_korintionan.csv"]
for book in books:
	bible = reader(open(book, 'U'))
	l = 0
	for read in bible:
		try:
			chapter 	= read[0]
			vers 		= read[1]
			text 		= read[2]

			data = {
			'book' 		: book,
			'chapter' 	: chapter,
			'vers' 		: vers,
			'text' 		: text
			}
			print data
		except:
			print book