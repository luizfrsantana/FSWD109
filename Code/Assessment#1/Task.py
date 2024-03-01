from datetime import datetime

class Task():
    
    #Attributes
    name = ''
    description = ''
    dueDate = datetime.strptime('2020-10-02', "%Y-%m-%d") 
    priority = ''
    
    #constructor
    def __init__(self,name,description,dueDate,priority):
        self.setName(name)
        self.setDescription(description)
        self.setDueDate(dueDate) 
        self.setPriority(priority)
     
    #Methods to get attributes information    
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getDueDate(self):
        return self.dueDate.strftime("%Y-%m-%d")
    def getPriority(self):
        return self.priority
    
    #Methods to set attributes information 
    def setName(self, name):
        self.name = name
    def setDescription(self, description):
        self.description = description
    def setDueDate(self, dueDate):
        self.dueDate = datetime.strptime(dueDate, "%Y-%m-%d") 
    def setPriority(self, priority):
        self.priority = priority