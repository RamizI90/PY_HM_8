#Employee Class

class Employee:
    def __init__(self, name, id, dep, job):
        self.__name=name
        self.__id=id
        self.__dep=dep
        self.__job=job 
    
    # mutator methods    
    def set_name(self, name):
        self.__name=name
    
    def set_id(self, id):
        self.__id=id
        
    def set_dep(self, dep):
        self.__dep=dep
        
    def set_job(self, job):
        self.__job=job 
        
    # accessor methods    
    def get_name(self, name):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_dep(self):
        return self.__dep
    
    def get_job(self):
        return self.__job
    
    # string method for showing
    def __str__(self):
        return "Name: " + self.__name + \
            "\nID Number: " + str(self.__id) + \
            "\nDepartment: " + self.__dep + \
            "\nJob Title: " + self.__job 
