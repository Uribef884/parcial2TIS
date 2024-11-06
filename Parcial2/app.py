from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/factorial/<int:num>')
def factorial(num):
    result = math.factorial(num)
    return render_template('factorial.html', number=num, result=result)

if __name__ == '__main__':
    app.run(debug=True)
