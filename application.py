from flask import Flask, render_template, request, json
from Converter import Converter

application = Flask(__name__)



@application.route("/")
def main():

    model = {"title":"Welcome to Converter!"}
    return render_template('index.html', model=model)


@application.route("/temp-converter")
def tempconverter():

    model = {"title":"Temp Converter",
             "converter":Converter()}
    return render_template('temp_converter.html', model=model)


@application.route("/convert-temp", methods=['POST'])
def convert_temp():

    temptoconvert = float(request.form["temp"])
    toC = request.form.get('toCelsius', False)


    conv = Converter()
    conv.setTemp(temptoconvert)

    if toC == False:
        conv.toFahrenheit()
    else:
        conv.toCelsius()


    model = {"title":"Temp Converter",
             "converter":conv}

    return render_template('temp_converter.html', model=model)



if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080, debug=True)