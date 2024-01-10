#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._is_valid_name(value):
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    def _is_valid_name(self,value):
        return isinstance(value,str) and 1 <= len(value) <= 25
    
my_self = Person("Katie", "Legal")
print(my_self.name)
