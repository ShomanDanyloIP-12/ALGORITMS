import random
import numpy as np
import matplotlib.pyplot as plt


class Item:
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight


def init(population_size, lenth_of_chromosome):
    population = []
    for i in range(population_size):
        population_piece = '0' * i
        population_piece += '1'
        population_piece += '0' * (lenth_of_chromosome - i)
        population.append(population_piece)
    return population


def decode(chromosome, length, stuff, restriction):
    taken_stuff = []
    total_weight = 0
    total_cost = 0
    for i in range(length):
        if chromosome[i] == '1':
            if total_weight+stuff[i].weight <= restriction:
                total_weight += stuff[i].weight
                total_cost += stuff[i].cost
                taken_stuff.append(i)
            else:
                break
    return total_cost, taken_stuff


def fitness(population, length, stuff, restriction):
    stuff_cost = []
    taken_stuff = []
    for i in range(len(population)):
        total_cost, taken_stuff = decode(population[i], length, stuff, restriction)
        stuff_cost.append(total_cost)
    return stuff_cost, taken_stuff


def randomization(population, stuff_cost, size_of_population):
    fitness_sum = []
    stuff_cost_sum = sum(stuff_cost)
    fitness = [i/stuff_cost_sum for i in stuff_cost]
    for i in range(len(population)):
        if i == 0:
            fitness_sum.append(fitness[i])
        else:
            fitness_sum.append(fitness_sum[i-1]+fitness[i])
    new_population = []
    for j in range(size_of_population):
        r = np.random.uniform(0, 1)
        for i in range(len(fitness_sum)):
            if i == 0:
                if 0 <= r <= fitness_sum[i]:
                    new_population.append(population[i])
            else:
                if fitness_sum[i-1] <= r <= fitness_sum[i]:
                    new_population.append(population[i])
    return new_population


def crossover(population):
    mother = population[:int(len(population)/2)]
    father = population[int(len(population)/2):]
    np.random.shuffle(mother)
    np.random.shuffle(father)
    offspring = []
    for i in range(int(len(population)/2)):
        r = np.random.uniform(0, 1)
        mother_offspring = mother[i][:50]+father[i][50:]
        father_offspring = father[i][:50]+mother[i][50:]
        offspring.append(mother_offspring)
        offspring.append(father_offspring)
    return offspring


def mutation(offspring, mutation_chance):
    for i in range(len(offspring)):
        r = np.random.uniform(0, 1)
        if r <= mutation_chance:
            point = np.random.randint(0, len(offspring[i]))
            if not point:
                if offspring[i][point] == '1':
                    offspring[i] = '0'+offspring[i][1:]
                else:
                    offspring[i] = '1'+offspring[i][1:]
            else:
                if offspring[i][point] == '1':
                    offspring[i] = offspring[i][:(point-1)]+'0'+offspring[i][point:]
                else:
                    offspring[i] = offspring[i][:(point-1)]+'1'+offspring[i][point:]
    return offspring


def local_improve(offspring, stuff, capacity, arranged_stuff):
    for gen in range(len(offspring)):
        weight = 0
        for chromosome in range(len(offspring[gen])):
            if offspring[gen][chromosome] == '1':
                weight += stuff[chromosome].weight
        if weight <= capacity:
            for item in range(len(arranged_stuff)):
                if offspring[gen][arranged_stuff[item][1]] == '0':
                    if weight + stuff[arranged_stuff[item][1]].weight <= capacity:
                        weight += stuff[arranged_stuff[item][1]].weight
                        if not arranged_stuff[item][1]:
                            offspring[gen] = '1' + offspring[gen][1:]
                        else:
                            offspring[gen] = offspring[gen][:(arranged_stuff[item][1] - 1)] + '1' + offspring[gen][arranged_stuff[item][1]:]
                    break
    return offspring


def arrange_stuff(stuff):
    arranged_stuff = []
    for i in range(len(stuff)):
        arranged_stuff.append((stuff[i].cost/stuff[i].weight, i))
    arranged_stuff.sort(reverse=True)
    return arranged_stuff


def main():
    num_of_iterations = 1000
    mutation_chance = 0.1
    population_size = 100
    length_of_chromosome = 100
    stuff = []
    for item in range(length_of_chromosome):
        stuff.append(Item(random.randint(2, 20), random.randint(1, 10)))
    arranged_stuff = arrange_stuff(stuff)
    capacity = 250
    population = init(population_size, length_of_chromosome)
    t = []
    best = []
    stuff_cost_temp = []
    for i in range(num_of_iterations):
        if i % 20 == 0 and i > 0:
            print(f"Best value at the moment - {max(stuff_cost_temp)}, on {i} iteration")
        offspring = crossover(population)
        offspring = mutation(offspring, mutation_chance)
        offspring = local_improve(offspring, stuff, capacity, arranged_stuff)
        union = population+offspring
        stuff_cost, taken_union_stuff = fitness(union, length_of_chromosome, stuff, capacity)
        population = randomization(union, stuff_cost, population_size)
        stuff_cost_temp, taken_stuff = fitness(population, length_of_chromosome, stuff, capacity)
        h = stuff_cost_temp.index(max(stuff_cost_temp))
        t.append(max(stuff_cost_temp))
        best.append(population[h])
    total_cost, taken_stuff_1 = decode(best[t.index(max(t))], length_of_chromosome, stuff, capacity)
    cost, weight = 0, 0
    for i in taken_stuff_1:
        cost += stuff[i].cost
        weight += stuff[i].weight
    print(f"Best combination:\n{taken_stuff_1}\nCost: {cost}, Weight: {weight}")
    print(f"First appeared on {t.index(max(t))} iteration")
    plt.plot(t)
    plt.xlabel('Iterations')
    plt.ylabel('Quality')
    plt.title('Dependence of quality on amount of iterations')
    plt.show()


main()
