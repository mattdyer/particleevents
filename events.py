import pyglet
import random
from pyglet import shapes
import simulator
from simulator.particle import Particle
from simulator.event import Event


window_width = 960
window_height = 540

window = pyglet.window.Window(window_width, window_height)

batch = pyglet.graphics.Batch()

circle = shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=batch)

particles = [Particle((50, 225, 30), (10, 100)).set_direction((1, 0)), Particle((70, 200, 40), (100, 10)).set_direction((0, 1))]

start_event = {
	'particle1': particles[0],
	'particle2': particles[1],
	'position': (100, 100)
}

@window.event
def on_key_press(symbol, modifiers):
	print('A key was pressed')

@window.event
def on_draw():
	window.clear()
	batch.draw()

	
def run_event(dt, event):
	print(dt)
	print(event)
	
	event_particles = [event['particle1'], event['particle2']]
	
	color_totals = [
		sum([particle.get_color()[0] for particle in event_particles]),
		sum([particle.get_color()[1] for particle in event_particles]),
		sum([particle.get_color()[2] for particle in event_particles])
	]
	
	new_color_1 = []
	new_color_2 = []
	
	for total in color_totals:
		if(total > 255):
			new_val = total - 255
			new_val_2 = 255
		else:
			new_val = total
			new_val_2 = 0
		
		new_color_1.append(new_val)
		new_color_2.append(new_val_2)
	
	
	print(new_color_1)
	print(new_color_2)
	
	event_particles.append(Particle(tuple(new_color_1), event['position']))
	
	particles.append(event_particles[2])
	
	if(sum(new_color_2) > 0):
		event_particles.append(Particle(tuple(new_color_2), event['position']))
		particles.append(event_particles[3])
	
	#print(particles)
	
	event_particles_copy = event_particles.copy()
	
	for event_particle_index, event_particle in enumerate(event_particles):
		
		for particle_index, particle in enumerate(particles):
			if(not (event_particle == particle)):
				print('something')
			
		
		print(event_particle_index)
		print(event_particle)


#I need an array of particles, I just want to avoid looping over all of them during each frame.
#So maybe I do need to still loop over all of them when an event happens to
# calculate future events with the current particles I'm working with
#if particles had a direction I may be able to quickle find intersecting paths and create future events
#does the particle need to store a location of its next event so we can igore it when finding other interactions
	
	

	
	
#pyglet.clock.schedule_interval(update_objects, 1/60.0)

schedule_result = pyglet.clock.schedule_once(run_event, 1, start_event)

print(schedule_result)

pyglet.app.run()

