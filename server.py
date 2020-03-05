from flask import Flask, render_template, request, send_file
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
        if input[0] == "Address Range":
            input[1] = float(request.args.get("keyfield"))
        else:
            input[1] = request.args.get("keyfield")
    except:
        input[1] = None
    try:
        input[2] = float(request.args.get("latitudetext"))
    except:
        input[2] = None
    try:
        input[3] = float(request.args.get("longitudetext"))
    except:
        input[3] = None
    print(input)
    mapgenerator.genmap(input)
    return render_template("patient_locations.html")


@app.route("/<path:subpath>/FF0000.png")
def returnredmarker(subpath):
    return send_file("static/markers/FF0000.png", mimetype="image")


@app.route("/<path:subpath>/0000FF.png")
def returnbluemarker(subpath):
    return send_file("static/markers/0000FF.png", mimetype="image")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)



