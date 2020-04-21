from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
    'app.html')

# @app.route("/upload", methods=["POST"])
# def upload():
#     uploaded_files = flask.request.files.getlist("file[]")
#     print (uploaded_files)
#     return render_template(
#     'app.html')

if __name__ == "__main__":
    app.run()