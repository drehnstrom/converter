from flask import Flask, render_template, request, json, jsonify
from Converter import Converter
from error import InvalidUsage

application = Flask(__name__)


@application.route("/")
def main():
    model = {"title":"Welcome to the GREAT CONVERTER!!"}
    return render_template('index.html', model=model)


@application.route("/temp-converter")
def tempconverter():
    model = {"title":"Temp Converter",
             "converter":Converter()}
    return render_template('temp_converter.html', model=model)


@application.route("/convert-temp", methods=['POST'])
def convert_temp():

    try:
        temptoconvert = float(request.form["temp"])
    except:
        temptoconvert = 0.0


    toC = request.form.get('toCelsius', False)
    conv = Converter()
    conv.setTemp(temptoconvert)

    if toC == False:
        conv.toFahrenheit()
    else:
        conv.toCelsius()


    model = {"title":"Temp Converter!",
             "converter":conv}
    return render_template('temp_converter.html', model=model)


@application.route("/api/conversions/temperature/<temp>")
def to_celsius(temp):

    try:
        temptoconvert = float(temp)
    except:
        raise InvalidUsage('Invalid User Input. Temperature parameter must be numeric.', status_code=400)

    conv = Converter()
    conv.setTemp(temptoconvert)
    conv.toCelsius()
    celsius = conv.converted_temp
    conv.toFahrenheit()
    fahrenheit = conv.converted_temp

    result = {"input":temptoconvert,
             "celsius":celsius,
             "fahrenheit":fahrenheit}

    return json.dumps(result)


@application.route("/api/pets")
def get_pets():

    pets = [{"name":"Noir", "breed":"Schnoodle"},
            {"name":"Bree", "breed":"MaltePoo"},
            {"name":"Sparky", "breed":"Mutt"}]

    return json.dumps(pets)


@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# Need to add  port=8080,  in run function below to run on ELB
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080, debug=True, threaded=True)