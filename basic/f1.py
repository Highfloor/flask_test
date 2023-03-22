from flask import flask,render_template,jsonify,url_for

app = flask(__name__)

@app.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True,ip='0.0.0.0',port=5000)
