class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_older(self):
        self.age = self.age + 1
        
class Workers:
    
    def __init__(self):
        self.workers = []
        
    def add(self, worker):
        self.workers.append(worker)
        
    def get_average_age(self):
        age_sum = 0
        for worker in self.workers:
            age_sum = age_sum + worker.age
        return age_sum / len(self.workers)

workers = Workers()        
workers.add(Person(name="Ivan", age = 24))
workers.add(Person(name="Mary", age = 20))
workers.add(Person(name="Alex", age = 21))
workers.add(Person(name="Sara", age = 29))
           
print("Average age:", workers.get_average_age())
    
