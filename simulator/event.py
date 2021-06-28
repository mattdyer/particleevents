class Event:
	
	def __init__(self, particle1, particle2, position):
		self.particle1 = particle1
		self.particle2 = particle2
		self.position = position
	
	def get_particle_1(self):
		return self.particle1
	
	def get_particle_2(self):
		return self.particle2
	
	def get_position(self):
		return self.position