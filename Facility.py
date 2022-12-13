class Facility:
    
    def __init__(self, name):
        self.name = name
        
    
    def addFacility(self):
        fname = input("Enter Facility name: \n")
        self.name = fname
        path = "facilities.txt"
        with open(path, "a") as file:
            file.write(self.name + "\n\n")
            
    def displayFacilities():
        print("The Hospital  Facilities are: \n\n")
        path = "facilities.txt"
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    
    def writeListOfFacilitiesToFile(facilityList):
        path = "faclities.txt"
        with open(path, "r+") as file:
            for facility in facilityList:
                file.write(facility + "\n\n")
    
    