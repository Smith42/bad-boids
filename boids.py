"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes
n_boids = 50

boids_x=[random.uniform(-450,50.0) for x in range(n_boids)]
boids_y=[random.uniform(300.0,600.0) for x in range(n_boids)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(n_boids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(n_boids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	x_positions,y_positions,x_velocities,y_velocities=boids
	# Fly towards the middle
	for i in range(n_boids):
		for j in range(n_boids):
			x_velocities[i]=x_velocities[i]+(x_positions[j]-x_positions[i])*0.01/n_boids

	for i in range(len(x_positions)):
		for j in range(len(x_positions)):
			y_velocities[i]=y_velocities[i]+(y_positions[j]-y_positions[i])*0.01/n_boids

	# Fly away from nearby boids
	for i in range(n_boids):
		for j in range(n_boids):
			if (x_positions[j]-x_positions[i])**2 + (y_positions[j]-y_positions[i])**2 < 100:
				x_velocities[i]=x_velocities[i]+(x_positions[i]-x_positions[j])
				y_velocities[i]=y_velocities[i]+(y_positions[i]-y_positions[j])

	# Try to match speed with nearby boids
	for i in range(n_boids):
		for j in range(n_boids):
			if (x_positions[j]-x_positions[i])**2 + (y_positions[j]-y_positions[i])**2 < 10000:
				x_velocities[i]=x_velocities[i]+(x_velocities[j]-x_velocities[i])*0.125/n_boids
				y_velocities[i]=y_velocities[i]+(y_velocities[j]-y_velocities[i])*0.125/n_boids

	# Move according to velocities
	for i in range(len(x_positions)):
		x_positions[i]=x_positions[i]+x_velocities[i]
		y_positions[i]=y_positions[i]+y_velocities[i]


figure=plt.figure()
axes_min = -500
axes_max = 1500
axes=plt.axes(xlim=(axes_min,axes_max), ylim=(axes_min,axes_max))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
