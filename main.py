import random
import copy
from job import Job
from gene import Genes
import time

def sortkey(Genes):
    return Genes.obj

def selection(Mating_num, Set_Genes = []):
    Mating_pool = []
    for i in range(0, Mating_num):
        candidates = random.sample(Set_Genes, 2)
        candidates.sort(key = sortkey)
        Mating_pool.append(candidates[0])
        del candidates[1]

    return Mating_pool

def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    how_many = random.randint(1, len(parent1.chromosome))
    index_sample = []
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    for i in range(0, len(parent1.chromosome)):  # 빈 child 리스트
        index_sample.append(i)
    random.shuffle(index_sample)

    parent_legacy = []
    for i in range(0, how_many):
        parent_legacy.append(index_sample[i])
    parent_legacy.sort()

    unlegacy = index_sample[how_many:]
    unlegacy.sort()

    delete_1 = [] # parent1 에서
    delete_2 = []

    for i in unlegacy:
        delete_1.append(parent1.chromosome[i])
        delete_2.append(parent2.chromosome[i])

    for i in parent_legacy:
        child1.chromosome[i]=parent1.chromosome[i]
        child2.chromosome[i]=parent2.chromosome[i]

    unlegacy_1 = copy.deepcopy(unlegacy)
    for i in range(0, len(parent2.chromosome)):
        temp = parent2.chromosome[i]
        if temp in delete_1:
            child1.chromosome[unlegacy_1.pop(0)] = parent2.chromosome[i]
            delete_1.remove(temp)

    unlegacy_2 = copy.deepcopy(unlegacy)
    for i in range(0, len(parent1.chromosome)):
        temp = parent1.chromosome[i]
        if temp in delete_2:
            child2.chromosome[unlegacy_2.pop(0)] = parent1.chromosome[i]
            delete_2.remove(temp)

    child1.get_schedule()
    child1.makespan()
    child2.makespan()
    child2.get_schedule()
    Set_child = [child1, child2]
    return Set_child

def mutation(gene):

    r = random.randint(1, len(gene.chromosome) // 4)

    for i in range(0, r):
        ran = random.randint(range(0, len(gene.chromosome)-1))
        z = gene.chromosome.pop(ran)
        gene.chromosome.append(z)


    gene.makespan()
    gene.get_schedule()
#-----------------------loop------------------------------------
job_num =200
gene_num = 30
Mating_pool_num = 60
iteration_num = 30

elitism_num = int(0.1 * float(gene_num))
crossover_prob = 0.5
crossover_num = int(0.9 * float(gene_num))
mutation_prob = 0.05
end_generation = 50

jobs = [[1, 2, 3, 5, 9],
        [1, 3, 4, 5, 9],
        [1, 3, 5, 6, 7, 9],
        [1, 2, 3, 5, 6, 8, 9],
        [1, 2, 3, 4, 5, 9],
        [1, 3, 4, 5, 2, 8, 9],
        [1, 5, 6, 7, 2, 3, 9],
        [1, 6, 7, 4, 5, 9],
        [1, 3, 5, 4, 2, 8, 9]]

process_info = [[10, 500, 300, 0, 10],
                [15, 0, 450, 350, 0],
                [10, 0, 0, 400, 250, 20],
                [15, 500, 300, 0, 400, 250, 0],
                [15, 500, 300, 450, 350, 0],
                [10, 0, 450, 350, 500, 50, 15],
                [20, 0, 400, 250, 500, 300, 0],
                [20, 400, 250, 450, 350, 0],
                [5, 200, 300, 0, 100, 80, 100]]

if __name__ == '__main__':
    it=1
    optimal_val = 0
    for i in range(0, iteration_num):
        Set_jobs = []
        Set_Genes = []
        N_generation = 1
        for i in range(0, job_num):
            Set_jobs.append(Job(i, jobs, process_info))

        for i in range(0, gene_num):
            G = Genes(Set_jobs)
            G.makespan()
            Set_Genes.append(G)

        Set_Genes.sort(key=sortkey)


        #--------------초기 집단 생성------------------#

        #selection sample
        while N_generation < end_generation:
            M_P = []
            M_P = selection(Mating_pool_num, Set_Genes)
            Next_Generation = []
            for i in range(0, crossover_num):
                set_parents = random.sample(M_P, 2)
                children = crossover(set_parents[0], set_parents[1])
                for j in range(0, 2):
                    Next_Generation.append(children[j])

            for i in range(0, elitism_num):
                Next_Generation.append(Set_Genes[i])

            Set_Genes = Next_Generation
            Set_Genes.sort(key = sortkey)

            N_generation += 1

            if N_generation == end_generation:
                optimal_val += Set_Genes[0].obj
                print(N_generation, ", ", Set_Genes[0].obj)
                it+=1

    mean_makespan = optimal_val/iteration_num
    print(mean_makespan)