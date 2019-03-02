from flask import Flask
bmi=Flask(__name__)
@bmi.route("/")
def home():
    return "hello" 
@bmi.route("/bmi/<int:x>/<int:y>")
def a(x,y):
    s=x/((y/100)**2)
    if s<16:
        return "Severely underweight"
    elif 16 <= s < 18.5: 
        return "Underweight"
    elif 18.5 <= s < 25: 
        return "Normal"
    elif 25 <= s < 30: 
        return "Overweight"
    elif s>30:
        return "OBESE"

    


if __name__=="__main__":
    bmi.run(debug=True, port=2000)
