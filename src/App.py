from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homePage():
	if request.method == "POST":
		files = request.files.getlist("file")
		# print(files)
		# return ""
		return redirect(url_for("keyPage", fls=files))
	else:
		return render_template('app.html')

@app.route("/keyword", methods=["POST", "GET"])
def keyPage(fls):
	if request.method == "POST":
		keyword = request.form["kw"]
		return redirect(url_for("algPage", fls=fls, kw=keyword))
	else:
		return render_template('keyword.html')

@app.route("/algorithm", methods=["POST", "GET"])
def algPage(fls, kw):
	if request.method == "POST":
		algorithm = "Boyer Moore"
		return redirect(url_for("resPage", fls=fls, kw=kw, alg=algorithm))
	else:
		return render_template('algorithm.html')

@app.route("/result")
def resPage(fls, kw, alg):
	return f"<h1>{kw}</h1>"

if __name__ == "__main__":
    app.run(debug=True)