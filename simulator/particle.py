class Particle:
	
	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.direction = (0, 0)
		
		
	def set_direction(self, direction):
		self.direction = direction
		
		return self
		
	def set_random_direction(self):
		self.direction = (random.uniform(0, 1), random.uniform(1, 1))
	
	def get_color(self):
		return self.color