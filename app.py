from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html', title='About me')

@app.route('/hobby')
def hobby():    
    return render_template('hobby.html', title='My hobbies')

@app.route('/classs')
def classs():    
    return render_template('classs.html', title='My classes')


if __name__ == '__main__':
    app.run(debug=True)