# http://127.0.0.1:5000/

from flask import Flask,render_template, request, flash, redirect, url_for
import os
import sys

from werkzeug.utils import secure_filename

UPLOAD_FOLDER      = 'static/csv'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.secret_key="321"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=['GET','POST'])

def upload():
    global csv
    if request.method=='POST':
     csv =request.files['upload_csv']
         
     if csv.filename!='': 
    
      filepath=os.path.join(app.config["UPLOAD_FOLDER"],csv.filename)
      csv.save(filepath)
    
      flash("File Upload Successfully","success")

    return render_template("upload.html")

if __name__ =='__main__':
    app.run(debug=True)
