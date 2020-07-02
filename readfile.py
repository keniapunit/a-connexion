from flask import Flask
from file_reader import fetch_file

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Index HTML!</h2>"

@app.route('/fetch/', methods=['GET'])
def default_method():
    file_string = fetch_file('file1.txt')
    return file_string

@app.route('/fetch/<file_name>/', methods=['GET'])
def read_file(file_name):
    file_string = fetch_file(file_name)
    return file_string

@app.route('/fetch/<file_name>/<int:start_line>/', methods=['GET'])
def read_part1(file_name, start_line):
    file_string = fetch_file(file_name, start_line)
    return file_string

@app.route('/fetch/<file_name>/<int:start_line>/<int:end_line>/', methods=['GET'])
def read_part2(file_name, start_line, end_line):
    file_string = fetch_file(file_name, start_line, end_line)
    return file_string