import re
class Laboratory:
    
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        
    def addLabToFile(labObject):
        path = "laboratories.txt"
        textOutput = ""
        
        file = open(path, "a")
        labPropertiesList = [labObject.name, labObject.cost]
        
        addText = Laboratory.formatLabInfo(labPropertiesList)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def writeListOfLabsToFile(labObjectsList):
        path = "laboratories.txt"
        file = open(path, "r+")
        textOutput = ""
        for lab in labObjectsList:
            labPropertiesList = [lab.name, lab.cost]
            ft = Laboratory.formatLabInfo(labPropertiesList)
            textOutput += ft + "\n\n"
            
        file.truncate(0)
        file.write(textOutput)
        file.close()
    
    def displayLabList():
        path = "laboratories.txt"
        headerList = ["Lab", "Cost" ]
        print(Laboratory.formatLabInfo(headerList))
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()
    
    def formatLabInfo(propertiesValuesList):
        spaces = [16, 16]
        formattedText = ""
        
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText
    
    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory facility: \n")
        self.cost = input("Enter Laboratory cost: \n")
        
        Laboratory.addLabToFile(self)
    
    def readLaboratoriesFile():
        path = "laboratories.txt"
        labsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    lab = Laboratory(line[0], line[1])
                    
                    labsObjectList.append(lab)
          
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("laboratories.txt file created")
           
        return labsObjectList