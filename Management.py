from Doctor import Doctor
from Facility import Facility
from Laboratory import Laboratory
from Patient import Patient

class Management:
    
    def displayMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to Main Menu\n")
                
            print("Welcome to Alberta Hospital (AH) Managment system")
            print("Select from the following options, or select 0 to stop:")
            print("1 - 	Doctors")
            print("2 - 	Facilities")
            print("3 - 	Laboratories")
            print("4 - 	Patients\n")
            
            userInput = input("\n")
            
            if userInput == "1":
                Management.displayDoctorMenu()
            elif userInput == "2":
                Management.displayFacilityMenu()
            elif userInput == "3":
                Management.displayLaboratoryMenu()
            elif userInput == "4":
                Management.displayPatientMenu()
            elif userInput == "0":
                break
            
            isback = True            
    
    def displayDoctorMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to previous Menu\n")
            print("Doctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu\n")
            
            userInput = input("\n")
            
            if userInput == "1":
                Doctor.displayDoctorsList()
            elif userInput == "2":
                idSearch = input(" Enter the doctor Id: \n")
                Doctor.searchDoctorById(idSearch)
            elif userInput == "3":
                nameSearch = input(" Enter the doctor name: \n")
                Doctor.searchDoctorByName(nameSearch)
            elif userInput == "4":
                Doctor.enterDrInfo(Doctor)
            elif userInput == "5":
                Doctor.editDoctorInfo()
            elif userInput == "6":
                break
            
            isback = True
        
    
    def displayFacilityMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to the previous Menu\n")
            
            print("Facilities Menu:")
            print("1 - Display Facilities list")
            print("2 - Add Facility")
            print("3 - Back to the Main Menu\n")
            
            userinput = input("")
            
            if userinput == "1":
                Facility.displayFacilities()
            elif userinput == "2":
                Facility.addFacility(Facility)
            elif userinput == "3":
                break
            
            isback = True
    
    def displayLaboratoryMenu():
        isback = False
        while True:
            if isback == True:
                print("Back to the previous Menu")
            
            print("Laboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu\n")
            
            userInput = input("")
            
            if userInput == "1":
                Laboratory.displayLabList()
            elif userInput == "2":
                Laboratory.enterLaboratoryInfo(Laboratory)
            elif userInput == "3":
                break
            
            isback = True
    
    def displayPatientMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to the previous Menu\n")
                
            print("Patient Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu\n")
            
            userInput = input("")
            
            if userInput == "1":
                Patient.displayPatientsList()
            if userInput == "2":
                idSearch = input("\n Enter the Patient Id: \n")
                Patient.searchPatientById(idSearch)
            if userInput == "3":
                Patient.enterPatientInfo(Patient)
            if userInput == "4":
                Patient.editPatientInfo()
            if userInput == "5":
                break
            
            isback = True