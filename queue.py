#!/usr/bin/python3

""" Class queue  """
class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		return len(self.items)

	def array(self):
		return self.items

if __name__ == "__main__":
	q = Queue()
	print(q.size())
	q.enqueue("hello")
	print(q.array())
	q.enqueue(3)
	print(q.array())
	q.dequeue()
	print(q.array())
