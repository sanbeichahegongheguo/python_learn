# conding:utf-8

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.__list = []


	def push(self, item):
		return self.__list.append(item)
		

	def pop(self):
		return self.__list.pop()
		

	def peek(self):
		if self.__list:
			return self.__list[-1]
		else:
			return None


	def is_empty(self):
		return self.__list == []
		

	def size(self):
		return len(self.__list)
		pass

if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push("abc")
	print("size:%d" % s.size())
	print(s.pop())
	print("size:%d" % s.size())
	print(s.pop())
	print("is_empty:%s" % s.is_empty())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print("is_empty:%s" % s.is_empty())
