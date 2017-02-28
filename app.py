from flask import Flask, render_template, request, json
from Converter import Converter

app = Flask(__name__)


@app.route("/")
def main():

    model = {"title":"Welcome to Converter!"}
    return render_template('index.html', model=model)


@app.route("/temp-converter")
def tempconverter():

    model = {"title":"Temp Converter",
             "converter":Converter()}
    return render_template('temp_converter.html', model=model)


@app.route("/convert-temp", methods=['POST'])
def convert_temp():

    temptoconvert = float(request.form["temp"])

    conv = Converter()
    conv.setTemp(temptoconvert)
    conv.toCelsius()

    model = {"title":"Temp Converter",
             "converter":conv}

    return render_template('temp_converter.html', model=model)



if __name__ == "__main__":
    app.run()