from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def calculator_app():
    # Simply serves our beautiful, interactive HTML file
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)


