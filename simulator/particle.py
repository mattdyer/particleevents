from sympy.geometry import Ray, intersection
import random

class Particle:
	
	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.direction = Ray(position, (position[0], position[1] + 1))
		self.next_event_time = 0
		
	
	def set_position(self, position):
		self.position = position
	
	def get_direction(self):
		return self.direction
	
	def get_position(self):
		return self.position
		
	def set_random_direction(self):
		self.direction = Ray(self.position, (random.uniform(0, 1) + self.position[0], random.uniform(0, 1) + self.position[1]))
	
	def get_color(self):
		return self.color
	
	def get_next_event_time(self):
		return self.next_event_time
	
	def set_next_event_time(self, next_event_time):
		self.next_event_time = next_event_time
	
	def intersects(self, particle):
		result = intersection(self.get_position(), particle.get_position())
		
		print('---')
		print(result)
		print('---')
		
		#if(result):
			
		
	
	
	
	
# Check over the particles if our lines intersect, then we check the distance from current position.  
# If they match then that is a new event
	
	
	
	