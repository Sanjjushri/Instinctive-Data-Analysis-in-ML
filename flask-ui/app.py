# http://127.0.0.1:5000/

from flask import Flask,render_template,request,flash
import os
import sys

app=Flask(__name__)
app.secret_key="321"

app.config['UPLOAD_FOLDER1']="flask-ui\static\csv"

@app.route("/",methods=['GET','POST'])

def upload():
    global csv
    if request.method=='POST':
     csv =request.files['upload_csv']
         
     if csv.filename!='': 
    
      filepath=os.path.join(app.config["UPLOAD_FOLDER1"],csv.filename)
      csv.save(filepath)
    
      flash("File Upload Successfully","success")

    return render_template("upload.html") 

# def result():
#      global csv
#     if request.method=='GET':



    



if __name__ =='__main__':
    app.run(debug=True)
