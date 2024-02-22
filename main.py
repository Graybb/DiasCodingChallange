import numpy as np
from flask import Flask
from flask_restful import Resource, Api,reqparse,request
import random
patientDict = {}
doctorDict = {}
AdmissionDict = {}

class Admission:
    def __init__(self,department,patient,doctors =None):
        self.department = department
        self.doctors = doctors
        self.patient = patient
        self.admissionID = ""+str(len(AdmissionDict)+1)

    def __str__(self):
        return f'{self.admissionID},{self.patient},{self.doctors},{self.department}'
                                  

class Patient:
    def __init__(self,name,SSN):
        self.name = name
        self.SSN = SSN
        self.patientID = ""+str(len(patientDict)+1)
        self.admissionList = []#i assume that a patient can have mutiple admissions, but not concurrent, i dont keep a check of that, since it is not specified, and also able to just look at last entry.
        #there is an argument of having a patient admission relation.
    def __str__(self):
        return f'patients name {self.name}, SSN : {self.SSN}, patientID :{self.patientID}'
    

class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.ID = ""+str(len(doctorDict)+1)
        self.department = department

    def __str__(self):
        return f'{self.name},{self.ID},{self.department}'


def createDataset():
    #creates Doctors
    for i in range(4):
        doctor = Doctor("TestDoctor"+str(i+1),"TestDepartment") #dont really uses the department, since in the requirements it is not really used/specified.
        doctorDict[doctor.ID] = doctor     
    #creates Patients and their admissions
    for i in range(8):
        
        patient = Patient("Testperson"+str(i+1),random.randint(0000,9999))
        patientDict[patient.patientID] = patient
        doctorForPatient = [doctorDict[str(random.randint(1,4))]]
        admission = Admission("A", patient, doctorForPatient)
        patient.admissionList.append(admission)
        AdmissionDict[admission.admissionID] = admission
    return doctorDict,patientDict,AdmissionDict
    




app = Flask("journal system")
api = Api(app)
class Manage(Resource):
    #default method for api, and will return patient if the given doctor has said patient
    @app.route('/getPatient', methods=['GET'])
    def get(): #using id instead of SSN since the doctor might not be allowed to know SSN if they arent their patient
        args = request.args
        patientID = args.get('patientID',default="0", type=str)
        doctorID = args.get('doctorID',default="0", type=str)
        patient = patientDict.get(patientID)
        #checks each admission, and sees if the doctor have worked with the patient before
        for admissions in patient.admissionList:
            for doctors in admissions.doctors:
                print(doctors)
                if doctorID == doctors.ID:
                    return str(patient)
#http://127.0.0.1:5000/getPatient?patientID=1&doctorID=3
        return "please input correct information"
    @app.route('/createPatient', methods=['PUT'])
    def createPatient(self):
        args = request.args
        patientName = args.get('patientName',default="J. Doe", type=str)
        patientSSN = args.get('patientSSN',default="0", type=str)

        return NotImplemented
    def createDoctor(self):
        return NotImplemented
    def getAllPatientsFromDoctor(self, doctor):
        return NotImplemented
    def getAllDoctorsFromPatient(self,patient):
        return NotImplemented
    def assignDoctorToPatient(self):
        return NotImplemented
     

api.add_resource(Manage,'/')        

if __name__ == '__main__' :
    doctorLists, patientDict, AdmissionDict =createDataset()
    app.run()
    
    