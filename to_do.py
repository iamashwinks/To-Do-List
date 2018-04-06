class TodoList(object):

	def __init__(self):
		self.todo = []
		self.done = []

	def add(self, task):
		self.todo.append(task)

	def mark_as_done(self):
		for i, task in enumerate(self.todo):
			print(i, task)

		index = int(input("Enter task you want to mark: "))
		task = self.todo.pop(index)
		self.done.append(task)

	def check_status(self):
		print("Pending: ")
		for i in self.todo:
			print(i)

		print("Completed:")
		for i in self.done:
			print(i)
