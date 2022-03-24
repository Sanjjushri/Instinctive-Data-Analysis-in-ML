# http://127.0.0.1:5000/

from flask import Flask,render_template,request,flash,redirect
from flask import *
import sys
import os, glob

app=Flask(__name__)
app.secret_key="321"

app.config['UPLOAD_FOLDER1']="flask-ui\static\csv"

dir = 'static/csv'
filelist = glob.glob(os.path.join(dir, "*"))

for f in filelist:
    os.remove(f)

# global csv.

@app.route("/",methods=['GET','POST'])
def upload():
    global csv
    print("1==========================1")
    if request.method=='POST':
     csv =request.files['upload_csv']
     print("2==========================2")
         
     if csv.filename!='': 
    
      filepath=os.path.join(app.config["UPLOAD_FOLDER1"],csv.filename)
      csv.save(filepath)
      print("3==========================3")
    
      flash("File Upload Successfully","success")

    return render_template("upload.html") 

# def result():
#      global csv
#     if request.method=='GET':

#     global csv
#     print("1==========================1")
#     if request.method=='POST':
#      csv =request.files['upload_csv']
#      print("==========================")
         
#      if csv.filename!='': 
    
#       filepath=os.path.join(app.config["UPLOAD_FOLDER1"], csv.filename)
#       csv.save(filepath)
#       print("==========================",csv.save(filepath))
#       print("==========================")
    
#       flash("File Upload Successfully","success")
#     #   print(csv.save(filepath))
    
#     # print(csv.save(filepath))
#     return render_template("upload.html") 

@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        # upload_csv = request.form['upload_csv']

        # value = 0
        # if value == 0:
     return redirect(url_for("result"))

@app.route('/result')
def result():
    return render_template("result.html")


if __name__ =='__main__':
    app.run(debug=True)

