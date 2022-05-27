
import random
from math import cos, pi, sqrt

from numpy import asarray
from numpy import exp

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
	""" funkcja generująca losowy punkt startowy z podanego zakresu
		:parameter bounds - wektor temperatur
	"""
	minimum = min(bounds[0])
	maximum = max(bounds[0])
	return [random.uniform(minimum, maximum)]

def mutate(xVector):
	array = []
	for i in range(len(xVector)):
		array.append(xVector[i] + random.gauss(0, 1))
	return array

def simulatedAnnealing(tempArray, cost_fn, n, start_temp=100, stop_temp=15, cool=0.95):
	""" simulated annealing algorithm
	 	:parameter tempArray - wektor temperatur
	 	:parameter cost_fm - funkcja kosztu, którą minimalizujemy
	 	:parameter start_temp - początkowa temperatura
	 	:parameter stop_temp - temperatura końcowa
	 	:parameter cool - wartość chłodzenia
	 """
	k = Boltzmann
	print(f"zakres od {min(tempArray[0])} do {max(tempArray[0])}")
	x = generate_start_point(tempArray)
	xValue = cost_fn(x)
	print(f"Pkt początkowy x: {x}, xValue: {xValue}")
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
		print(f"x: {x}, xValue: {xValue}, temp: {temperature}")
	return x, xValue, temperature

if __name__ == '__main__':
	result = simulatedAnnealing(asarray([[-100, 100]]), ackley, 100)
	print(f"Wynik x: {result[0][0]}, f(x): {result[1]}, temp: {result[2]}")