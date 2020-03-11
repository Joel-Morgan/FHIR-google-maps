# FHIR-Google-Maps

This project is a quick proof of concept of displaying patients on a google map with interesting filters to show trends.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites and Installation

What things you need to run the software

```
Follow the setup here - FHIR_works github - https://github.com/goshdrive/FHIRworks_2020
Python 3.7 - https://www.python.org/downloads/
FHIR-parser - pip install FHIR-Parser
Flask - pip install flask
Haversine - pip install haversine

SETUP A GOOGLE API KEY FOR YOUR USE: https://support.google.com/googleapi/answer/6158862?hl=en
API key must be stored in a text file named "googleapikey.txt" in the root directory.
```

Once installed, clone this repository and run the server.py file in python.

## Running the program

The webapp runs off 2 services in separate folders:

To run the FHIR-service, navigate to the FHIRworks/dotnet-azure-fhir-web-api folder and run:
```
dotnet run
```

To run the actual webapp, navigate to the GOSH-FHIRworks2020-google-maps folder and run:

```
python3.7 server.py
```

Flask should now bootup and the site will be acessible by:
```
0.0.0.0:12345 or localhost:12345
```

## Deployment

If this is to be deployed onto a public endpoint, the app.run line domain will need to be changed to your taste.

## Authors

* **Joel Morgan** - *Initial work and dev* - 

## License

This project is licensed under the Apache License version 2 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Big thanks to the FHIR-Parser project for enabling easy development of this: https://pypi.org/project/FHIR-Parser/
* The Map drawing code was adjusted from the Gmplot project to allow for cross platform use: https://github.com/vgm64/gmplot/tree/master/gmplot
