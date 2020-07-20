import random
from gene import Genes
from job import Job
import math
import copy

class Population:
    def __init__(self, Set_Genes = []):
        self.set_G = Set_Genes
        self.Mating_pool = self.selection()

    def crossover(self, parent1, parent2, child_1, child_2):
        how_many = random.randint(1,len(parent1.chromosome))
        index_sample = []
        child1 = []
        child2 = []
        for i in range(0, len(parent1.chromosome)): #빈 child 리스트
            child1.append(0)
            child2.append(0)

        for i in range(0, len(parent1.chromosome)): # 어느 자리를 따올 것인지
            index_sample.append(i)
        random.shuffle(index_sample)

        parent_legacy = []
        for j in range(0, how_many):
            parent_legacy.append(index_sample[j]) # parent1에서 상속시킬 유전자의 위치
        parent_legacy.sort()

        for i in parent_legacy :
            child1[i] = parent1.chromosome[i]
            child2[i] = parent2.chromosome[i]

        O1 = parent2.chromosome
        O2 = parent1.chromosome

        for i in range(0, len(child1)):
            if child1[i] != 0:
                O1.remove(child1[i])
        j=0
        for i in range(0, len(child2)):
            if child1[i] == 0:
                child1[i] = O1[j]
                j += 1

        for i in range(0, len(child2)):
            if child2[i] != 0:
                O2.remove(child2[i])
        j=0
        for i in range(0, len(child2)):
            if child2[i] == 0:
                child2[i] = O2[j]
                j += 1

        child_1.chromosome = child1
        child_2.chromosome = child2

    def mutation(self, gene):
        index_list = []
        change_index_1 = []
        change_index_2 = []
        change_value_1 = []
        change_value_2 = []

        r = random.randint(1, len(gene.chromosome)//8)
        for i in range(0, r):
            change_index_1.append(0)
            change_index_2.append(0)
            change_value_1.append(0)
            change_value_2.append(0)

        for i in range(0, len(gene.chromosome)):
            index_list.append(i)
        random.shuffle(index_list)

        for i in range(0, r):
            change_index_1[i] = index_list[i]
            change_index_2[i] = index_list[i+r]

        for j in range(0, len(change_index_1)):
            change_value_1[j]=gene.chromosome[change_index_1[j]]
            change_value_2[j]=gene.chromosome[change_index_2[j]]

        for k in range(0, len(change_index_1)):
            gene.chromosome[change_index_1[k]] = change_value_2[k]
            gene.chromosome[change_index_2[k]] = change_value_1[k]

    def selection(self, mating_num):
        for i in range(0, mating_num):
            candidates = random.sample(self.Set_Genes)
            candidates.sort(key = self.sortkey)


    def sortkey(self, Genes):
        return Genes.obj

