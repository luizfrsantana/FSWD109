class Task():
    
    #Attributes
    name = ''
    description = ''
    dueDate = '2020-02-28'
    priority = ''
    
    #constructor
    def __init__(self,name,description,dueDate,priority):
        self.name = name
        self.description = description
        self.dueDate = dueDate 
        self.priority = priority
     
    #Methods to get attributes information    
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getDueDate(self):
        return self.dueDate
    def getPriority(self):
        return self.priority
    
    #Methods to set attributes information 
    def setName(self, name):
        self.name = name
    def setDescription(self, description):
        self.description = description
    def setDueDate(self, dueDate):
        self.dueDate = dueDate
    def setPriority(self, priority):
        self.priority = priority