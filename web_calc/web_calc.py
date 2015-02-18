from flask import Flask, render_template, request
#import random
app = Flask(__name__)

@app.route("/")
def ask_for_number():
    return render_template("pre_calc.html")

@app.route("/post_calc", methods=["POST"])
def math_stuff():
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])
    operator = request.form['operator']
    if operator == "+":
        total = number1 + number2
    elif operator == "-":
        total = number1 - number2
    elif operator == "*":
        total = number1 * number2
    else:
        total = number1 / number2
    return render_template("post_calc.html", final_total=total,
                            num1=number1, num2=number2,
                            oper=operator)

if __name__ == "__main__":
    app.run(debug=True)
