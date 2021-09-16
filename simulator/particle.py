from vectors import point, vector

class Particle:
	
	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.direction = (0, 0)
		self.next_event_time = 0
		
		
	def set_direction(self, direction):
		self.direction = direction
		
		return self
	
	def get_direction(self):
		return self.direction
	
	def get_position(self):
		return self.position
		
	def set_random_direction(self):
		self.direction = (random.uniform(0, 1), random.uniform(1, 1))
	
	def get_color(self):
		return self.color
	
	def get_next_event_time(self):
		return self.next_event_time
	
	def set_next_event_time(self, next_event_time):
		self.next_event_time = next_event_time
	
	
#sympy has rays and can calculate intersection etc.
	
	
	
	