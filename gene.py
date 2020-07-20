import random
from job import Job




class Genes:
    def __init__(self, job_set = []):
        self.chromosome = self.generate(job_set)
        self.obj = 0
        self.fit = 0
        self.job_set = job_set
        self.schedule = self.get_schedule()

    def generate(self, job_set):
        g = []
        for job in job_set:
            g += [job] * len(job.operations)
        random.shuffle(g)
        return g

    def makespan(self):
        max_time = 0

        able_time_m = []
        able_time_j = []

        for i in range(0, 9):
            able_time_m.append(0)

        for job in self.chromosome:
            job.process_num=0

        for job in self.job_set:
            able_time_j.append(0)

        for job in self.chromosome:
            able_time_m[job.operations[job.process_num]-1]=max(able_time_m[job.operations[job.process_num]-1], able_time_j[job.num-1])+job.process_time[job.process_num]
            able_time_j[job.num-1] = able_time_m[job.operations[job.process_num] - 1]
            job.process_num += 1

            max_time = max(max(able_time_m), max_time)

        self.obj = max_time

    def fitness(self):
        self.fit = self.obj

    def get_schedule(self):
        schedule = []
        for job in self.chromosome :
            schedule += [job.num]
        return schedule

def sortkey(Genes):
    return Genes.obj

