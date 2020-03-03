from flask import Flask, render_template, request, redirect
import mapgenerator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/filter", methods=["GET"])
def generatemap():
    input = [None, None, None, None]
    try:
        input[0] = request.args.get("filterselect")
    except:
        input[0] = None
    try:
        input[1] = request.args.get("keyfield")
    except:
        input[1] = None
    try:
        input[2] = request.args.get("latitudetext")
    except:
        input[2] = None
    try:
        input[3] = request.args.get("longitudetext")
    except:
        input[3] = None
    print(input)
    mapgenerator.genmap(input)
    return render_template("patient_locations.html")


@app.route("/locations")
def location_map():
    raw_html_file = open("templates/patient_locations.html")
    raw_html = raw_html_file.read()
    return raw_html



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)



