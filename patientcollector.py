# uses the FHIR_parser project at: https://pypi.org/project/FHIR-Parser/

from haversine import haversine
from fhir_parser import FHIR, Patient, Observation
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
from fhir_parser.observation import Observation, ObservationComponent

fhir = FHIR()


def loadpatients(filteroption=None, key=None, lat=None, long=None):
    patients = fhir.get_all_patients()

    if filteroption is None or key is None:
        return patients
    elif filteroption == "Marital Status":
        filtered_patients = [patient for patient in patients if str(patient.marital_status) == key]
        return filtered_patients
    elif filteroption == "Gender":
        filtered_patients = [patient for patient in patients if str(patient.gender) == key]
        return filtered_patients
    elif filteroption == "Address Range":
        filtered_patients = [patient for patient in patients if haversine((lat, long), (patient.addresses[0].latitude, patient.addresses[0].longitude)) <= key]
        return filtered_patients
    return patients


def loadpatient(uuid):
    patient = fhir.get_patient(uuid)
    return patient
