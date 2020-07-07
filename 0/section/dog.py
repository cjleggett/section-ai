class Dog():
	def __init__(self, name):
		self.name = name
		self.age = 0
		self.sticks_fetched = 0
	
	def grow(self):
		self.age += 1

	def fetch_sticks(self, sticks):
		self.sticks_fetched += sticks

    
class LazyDog(Dog):
    
    def fetch_sticks(self, sticks):
        if self.sticks_fetched > 5:
            self.sticks_fetched = 5