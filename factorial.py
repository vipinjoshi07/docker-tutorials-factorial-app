from flask import Flask, render_template, request

app = Flask(__name__)

def get_factorial(x):
    if x == 0:
        result = 1
    else:
        result = x * get_factorial(x - 1)
    return result

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/factorial", methods=["GET", "POST"])
def factorial():
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            if number < 0:
                return "Please enter a non-negative  integer."
            else:
                return f"The factorial of {number} is {get_factorial(number)}."
        except ValueError:
            return "Please enter a valid integer."
    else:
        return render_template("factorial.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)