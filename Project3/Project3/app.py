from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def registration_page():
    return render_template('registration.html')

@app.route('/photos')
def photos_page():
    return render_template('photos.html')

if __name__ == '__main__':
    app.run(debug=True)