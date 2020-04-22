from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from Extractor import processFile

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homePage():
	if (request.method == 'POST'):
		path = "../test/"
		fileFromWeb = request.files.getlist('file[]')
		files = []
		for f in fileFromWeb:
			files.append(f.filename)
		keyword = request.form['kw']
		algorithm = request.form['algo']
		listOfTotal, listOfTime, listOfWords, listOfFiles = processFile(path, files, keyword, algorithm)
		length = len(listOfTotal)
		return render_template('app.html', length=length, keyword=keyword, total=listOfTotal, time=listOfTime, words=listOfWords, files=listOfFiles)
	else:	
		keyword = ""
		listOfTotal = [] 
		listOfTime = [] 
		listOfWords = [] 
		listOfFiles = []
		length = len(listOfTotal)
		return render_template('app.html', length=length, keyword=keyword, total=listOfTotal, time=listOfTime, words=listOfWords, files=listOfFiles)

if __name__ == "__main__":
    app.run(debug=True)