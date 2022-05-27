
import random
from math import exp, cos, pi, sqrt

from numpy import asarray
from numpy import exp
from numpy.random import rand

from scipy.constants import Boltzmann

def ackley(xVector):
    sqrtSum = 0
    cosinusSum = 0
    n = len(xVector)
    for i in range(0, n):
        sqrtSum += xVector[i] ** 2
    for i in range(0, n):
        cosinusSum += cos(2 * pi * xVector[i])
    return exp(1) + 20 - 20 * exp(-0.2 * sqrt((1 / n) * sqrtSum)) - exp((1 / n) * cosinusSum)


def generate_start_point(bounds):
	return bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])

def mutate(xVector):
	array = []
	for i in range(len(xVector)):
		array.append(xVector[i] + random.gauss(1, 10))
	return array

def simulatedAnnealing(bounds, cost_fn, n, start_temp=350, stop_temp=15, cool=0.95):
	""" simulated annealing algorithm
	 	:parameter bounds - given temperatures
	 	:parameter cost_fm - cost function which we minimize
	 	:parameter start_temp - starting temperature
	 	:parameter stop_temp - stop temperatur
	 	:parameter cool - cooling
	 """
	k = Boltzmann
	print(f"range{bounds}")
	x = generate_start_point(bounds)
	xValue = cost_fn(x)
	print(f"start point x: {x}, xValue: {xValue}")
	temperature = start_temp
	while temperature > stop_temp:
		for i in range(0, n):
			xPrim = mutate(x)
			xPrimValue = cost_fn(xPrim)
			if xPrimValue < xValue:
				x = xPrim
				xValue = xPrimValue
			else:
				y = random.random()
				if y < exp(-(xPrimValue - xValue) / k * temperature):
					x = xPrim
					xValue = xPrimValue
		temperature = temperature * cool
	return x, xValue, temperature

if __name__ == '__main__':
	result = simulatedAnnealing(asarray([[-100, 100]]), ackley, 1000)
	print(f"result x: {result[0]}, f(x): {result[1]}, temp: {result[2]}")