# conding:utf-8

class Deque(object):
	"""docstring for Queue"""
	def __init__(self):
		self.__list = []


	def add_font(self, item):
		"""从头部添加元素"""
		self.__list.insert(0, item)
		

	def add_rear(self, item):
		"""从尾部添加元素"""
		self.__list.append(item)


	def pop_front(self):
		"""从头部删除元素"""
		return self.__list.pop(0)


	def pop_rear(self):
		"""从尾部删除元素"""
		return self.__list.pop()
		

	def is_empty(self):
		return self.__list == []
		

	def size(self):
		return len(self.__list)
		

if __name__ == "__main__":
	q = Deque()
	q.add_font(1)
	q.add_font(2)
	q.add_font(3)
	q.add_font(4)
	q.add_rear("a")
	q.add_rear("b")
	q.add_rear("c")
	q.add_rear("d")
	print("is_empty:%s" % q.is_empty())
	print("size:%d" % q.size())
	print(q.pop_front())	
	print(q.pop_front())
	print(q.pop_rear())
	print(q.pop_rear())
	print("size:%d" % q.size())
	# 此时q = [4,3,2,1,a,b,c,d]
	print(q.pop_front())
	print(q.pop_front())
	print(q.pop_rear())
	print(q.pop_rear())
	print("is_empty:%s" % q.is_empty())
		