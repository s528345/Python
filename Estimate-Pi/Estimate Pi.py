import random

def estimate_Pi(numberOfPoints):
	# Estimate pi but number of points in the circle divided by the total
	points_Circle = 0
	total_Points = 0 
	for i in range(numberOfPoints):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		distance = x**2 + y**2
		if distance <= 1:
			points_Circle += 1
		total_Points += 1

	return 4 * points_Circle / total_Points


print(estimate_Pi(10))
print(estimate_Pi(100))
print(estimate_Pi(1000))
print(estimate_Pi(10000))
print(estimate_Pi(100000))
