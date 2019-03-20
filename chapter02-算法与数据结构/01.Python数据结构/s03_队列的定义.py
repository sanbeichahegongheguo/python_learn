# conding:utf-8

class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.__list = []


	def enqueue(self, item):
		"""如果入队列是从尾部入，那么出队列就 是要从头部出。反之亦然。"""
		self.__list.append(item)
		

	def dequeue(self):
		return self.__list.pop(0)
		

	def is_empty(self):
		return self.__list == []
		

	def size(self):
		return len(self.__list)
		

if __name__ == "__main__":
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	print("is_empty:%s" % q.is_empty())
	print("size:%d" % q.size())
	print(q.dequeue())
	print("size:%d" % q.size())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print("is_empty:%s" % q.is_empty())
