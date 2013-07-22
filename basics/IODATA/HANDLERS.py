
def loadFile(filename="file.txt", raw= False):
	""" Returns file content , 
		raw : returns a string with all data of the file
		default value: False this returns a list of file values
	""" 
	data = []
	try:
		File2Read = open(filename, "r")
	except:
		print "{0}: Unable to open file".format(__file__)
		return data

	""" If everything was ok , let's continue working """
	if raw:
		data = File2Read.read()
	else:
		data = [line.strip().lower() for line in File2Read]
		# strip removes the tail and head such white spaces, or new lines. 

	""" closing file """
	File2Read.close()
	return data

