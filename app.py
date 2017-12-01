from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/readonly')
def readonlyrota():
    return render_template('readonly.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
