from flask import Flask,render_template

app = Flask(__name__)
var = [{'name':'Ratul','job':'programmer'},{'name':'Diva','job':'financer'}]


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Contact_us')
def Contact():
    return render_template('contact.html',dev=var)

@app.route('/drawing')
def drawing():
    return render_template('drawing.html')

@app.route('/about/<string:job>/')
def about(job):
    return render_template('about.html',jav=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80,threaded=True)
