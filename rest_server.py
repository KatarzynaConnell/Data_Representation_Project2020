# create a basic flask server and import url and requests
from flask import Flask, url_for, request, redirect,abort

app = Flask(__name__,static_url_path='',static_folder='staticPages') #. means this folder

@app.route('/')
def index():
    return "hello"

# command to get all the stock
@app.route('/stock')
def getAll():
    return "served by Get All()"  

# get stock by ID
@app.route('/stock/<int:id>')  
def findById(id):
    return "served by find by id with it "+ str(id)

# create stock with POST
@app.route('/stock', methods=['POST'])
def create():
    return "served by Create "

#update
@app.route('/stock/<int:id>', methods=['PUT'])  
def update(id):
    return "served by update with it "+ str(id)

#delete
@app.route('/stock/<int:id>', methods=['DELETE'])  
def delete(id):
    return "served by delete with it "+ str(id)


if __name__ == "__main__":
    app.run(debug=True)


#Map POST method
