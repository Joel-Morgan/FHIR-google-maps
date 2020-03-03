# uses the FHIR_parser project at: https://pypi.org/project/FHIR-Parser/

from gmplot import gmplot
import patientcollector, inputhandler
from haversine import haversine


def genmap(input_value):
    api_key_file = open("googleapikey.txt", "r")
    api_key = api_key_file.readline().replace("\n", "")
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)

    if len(input_value) == 4 and input_value[0] == "Address Range":
        gmap.marker(input_value[2], input_value[3], 'blue', title="reference")
        patients = patientcollector.loadpatients(input_value[0], input_value[1], input_value[2], input_value[3])
    else:
        patients = patientcollector.loadpatients(input_value[0], input_value[1])

    print("{} entries found".format(len(patients)))

    # plot markers
    for patient in patients:
        gmap.marker(patient.addresses[0].latitude, patient.addresses[0].longitude, 'red', title=patient.addresses[0].full_address.replace("\n", ", "))

    # Draw
    gmap.apikey = api_key
    gmap.draw("templates/patient_locations.html")
