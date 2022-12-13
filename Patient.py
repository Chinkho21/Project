import re
class Patient:

    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
        
    def formatPatientInfo(propertiesValuesList):
        spaces = [5, 23, 16, 16, 16]
        formattedText = ""
        
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText
    
    def enterPatientInfo(self):
        self.id = input("Enter the Patient's ID: \n")
        self.name = input("Enter the Patient's name: \n")
        self.disease = input("Enter the Patient's disease: \n")
        self.gender = input("Enter the Patient's gender: \n")
        self.age = input("Enter the Patient's agae: \n")

        
        Patient.addPatientToFile(self)
    
    def readPatientsFile():
        path = "patients.txt"
        patientsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    patient = Patient(line[0], line[1], line[2], line[3], line[4])
                    
                    patientsObjectList.append(patient)
          
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("patients.txt file created")
           
        return patientsObjectList

    def searchPatientById(idSearch):
        patientsObjectList = Patient.readPatientsFile()
        idExist = False
        for patient in patientsObjectList:
            if patient.id == idSearch:
                patient.displayPatientInfo()
                idExist = True
                return patientsObjectList.index(patient)
        if idExist == False:
            print("Can't find the patient with the same ID on the system \n")
            return -1
                
    
    def displayPatientInfo(self):
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        print(Patient.formatPatientInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.disease, self.gender, self.age]
        print(Patient.formatPatientInfo(valuesList))
        
        
    def editPatientInfo():
        pt_Id = input("Please enter the id of the Patient that you want to edit their information:\n")
        pt_index = Patient.searchPatientById(pt_Id)
        if pt_index != -1:
            ptObjList = Patient.readPatientsFile()
            ptObjList[pt_index].name = input("Enter new Name: \n")
            ptObjList[pt_index].disease = input("Enter new Disease: \n")
            ptObjList[pt_index].gender = input("Enter new Gender: \n")
            ptObjList[pt_index].age = input("Enter new Age: \n")

            Patient.writeListOfPatientsToFile(ptObjList)
        else:
            return -1
        
    def displayPatientsList():
        path = "patients.txt"
        headerList = ["ID", "Name", "Disease", "Gender", "Age" ]
        print(Patient.formatPatientInfo(headerList))
        print("\n\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()
        
    def writeListOfPatientsToFile(patientsObjList):
        path = "patients.txt"
        file = open(path, "r+")
        textOutput = ""
        for pt in patientsObjList:
            ptProperties = [pt.id, pt.name, pt.disease, pt.gender, pt.age]
            ft = Patient.formatPatientInfo(ptProperties)
            textOutput += ft + "\n\n"
            
        file.truncate(0)
        file.write(textOutput)
        file.close()
    
    def addPatientToFile(ptObject):
        path = "patients.txt"
        textOutput = ""
        
        file = open(path, "a")
        pt = ptObject
        ptProperties = [pt.id, pt.name, pt.disease, pt.gender, pt.age]
        addText = Patient.formatPatientInfo(ptProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()