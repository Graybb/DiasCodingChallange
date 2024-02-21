import numpy as np
from flask import Flask
from flask_restful import Resource, Api,reqparse
import random
patientDict = {}
doctorLists = []
AdmissionDict = {}


class Admission:
    def __init__(self,department,patient,doctors =None):
        self.department = department
        self.doctors = doctors
        self.patient = patient

class Patient:
    def __init__(self,name,SSN,patientID):
        self.name = name
        self.SSN = SSN
        if patientID == None:
            self.patientID = len(patientDict)+1
    

class Doctor:
    def __init__(self, name, id, department):
        self.name = name
        self.ID = id
        self.department = department
def createDataset():
    #creates Doctors
    doctors = [Doctor("Jan Hajsen","001","A"),Doctor("Mani Freidrich","002","B"),Doctor("Josefine Hajsen","003","A"),Doctor("Kim Possible","004","C")]
    
    #creates Patients
    for i in range(8):
        patient = Patient("Testperson"+i,random.randint(0000,9999))
        patientDict[patient.patientID] = patient

    doctorWithPatient = {
        '001': ["001","002","003"],
        '002': ["007","008"],
        '003':["002",],
        '004': ["001","005","006","004"]}    
    







app = Flask("journal system")
api = Api(app)
createDataSet()
parser = reqparse.RequestParser()
parser.add_argument()

class Manage(Resource):
    #default method for api, and will return patient if the given doctor has said patient
    def get(self,doctor_id,patient_id): #using id instead of SSN since the doctor might not be allowed to know SSN if they arent their patient
        return doctor_id
    def createPatient(self):
        return NotImplemented
    def createDoctor(self):
        return NotImplemented
    def getAllPatientsFromDoctor(self, doctor):
        return NotImplemented
    def getAllDoctorsFromPatient(self,patient):
        return NotImplemented
    def assignDoctorToPatient(self):
        return NotImplemented
     

api.add_resource(Manage,'/<doctor_id>')        

if __name__ == '__main__' :
    app.run()