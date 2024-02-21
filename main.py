import numpy as np
from flask import Flask
from flask_restful import Resource, Api,reqparse



app = Flask("journal system")
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument()
class Manage(Resource):
    def get(self,doctor_id):
        return doctor_id
    def getPatient(self,doctor,patient):
        return NotImplemented
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
     

api.add_resource(Manage,'/getPatient/<doctor_id>')        

class Admission:
    department = NotImplemented
    doctors = NotImplemented
    medicalJournal = NotImplemented

class Patient:
    name = NotImplemented
    SSN = NotImplemented
    patientID = NotImplemented

class Doctor:
    name = NotImplemented
    ID = NotImplemented
    department = NotImplemented


if __name__ == '__main__' :
    app.run()