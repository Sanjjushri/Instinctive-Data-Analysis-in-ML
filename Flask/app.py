# importing the required libraries
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# initialising the flask app
app = Flask(__name__)

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      f.save(secure_filename(f.filename)) # this will secure the file
      return 'file uploaded successfully' # Display thsi message after uploading
		
if __name__ == '__main__':
   app.run() # running the flask app