class MyDecorator(object):
	def __init__(self, decorated):
		print "============== INSIDE THE DECORATOR OBJECT ============= "
		self.decorated = decorated

	def __call__(self, x, y):
		""" execute the function """
		print "============= DECORATOR CALL FUNCTION ============="
		self.decorated(x, y)
		print "============= ENDING CALL ========================="

@MyDecorator
def normal_function(x, y):
	print "result:",x*y
	return x*y

def main():
	normal_function(3,4)

if __name__ == '__main__':
	main()
