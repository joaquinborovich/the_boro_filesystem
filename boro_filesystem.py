from flask import Flask, request, render_template, jsonify, redirect, send_file, send_from_directory
import os

boro_filesystem = Flask(__name__)

# TODO: make it relative
boro_filesystem.config["FILE_UPLOADS"] = "./filesystem"


@boro_filesystem.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.files:
            file_up = request.files["file-up"]

            file_up.save(os.path.join(boro_filesystem.config["FILE_UPLOADS"], file_up.filename))

            return redirect(request.url)
        
    # renders {root}/template/index.html
    return render_template('index.html')


@boro_filesystem.route('/file/<file_name>', methods=['GET'])
def file_access(file_name):
    if file_name and request.method == "GET":
        file_path = f"./filesystem/{file_name}"
        
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return send_file(file_path, file_name)
    
    return render_template('index.html')


@boro_filesystem.route('/files/', methods=['GET'])
def files():
    files_list = os.listdir(boro_filesystem.config["FILE_UPLOADS"])
    return render_template('files.html', files=files_list)




if __name__ == "__main__":
    boro_filesystem.run(debug=True, port=2020)