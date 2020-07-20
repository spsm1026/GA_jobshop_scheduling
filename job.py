import random

class Job:
    def __init__(self, num, jobs = [], process = []):
        self.num = num+1
        self.kind = self.decide_job_kind()
        self.operations = self.get_job_info(jobs)
        self.process_time = self.get_process_time(process)

    def decide_job_kind(self):
        k = random.randint(1, 8)
        return k

    def get_job_info(self, jobs):
        operations = jobs[self.kind - 1]
        return operations

    def get_process_time(self, process):
        process_t = process[self.kind - 1]
        return process_t