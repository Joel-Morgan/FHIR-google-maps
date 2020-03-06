# uses the FHIR_parser project at: https://pypi.org/project/FHIR-Parser/

import patientcollector, inputhandler, mapdraw


def genmap(input_value):
    api_key_file = open("googleapikey.txt", "r")
    api_key = api_key_file.readline().replace("\n", "")
    startoptions = [0, 0, 2]
    markerlist = []

    if len(input_value) == 4 and input_value[0] == "Address Range":
        markerlist.append([input_value[2], input_value[3], "0000FF", "reference"])
        patients = patientcollector.loadpatients(input_value[0], input_value[1], input_value[2], input_value[3])
    else:
        patients = patientcollector.loadpatients(input_value[0], input_value[1])

    print("{} entries found".format(len(patients)))

    # plot markers
    for patient in patients:
        markerlist.append([patient.addresses[0].latitude, patient.addresses[0].longitude, "FF0000", patient.addresses[0].full_address.replace("\n", ", ")])

    # Draw
    mapdraw.drawmap("templates/" + str(input_value[0]) + str(input_value[1]) + ".html", api_key, startoptions, markerlist)
