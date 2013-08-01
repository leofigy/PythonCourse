class basic(object):
	def __init__(self):
		print "at parent"

	def foo(self):
		print "at foo"

class daughter(basic):
	def __init__(self):
		print "at daughter"
		super(daughter, self).__init__()


	def foo(self):
		print "at foo daughter"
		super(daughter, self).foo()


def main():
	son = daughter()
	son.foo()

if __name__ == '__main__':
	main()