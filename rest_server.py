# create a basic flask server and import url and requests
from flask import Flask, url_for, request, redirect,abort, jsonify

app = Flask(__name__,static_url_path='',static_folder='staticPages') #. means this folder

#make an array in memory 
stock=[
    {"id": 1, "Product":"Wine", "Quantity": 200, "Price": 25},
    {"id": 2, "Product":"Whiskey", "Quantity":100, "Price": 47},
    {"id": 3, "Product":"Champagne", "Quantity":50, "Price": 100}
]
nextId=4


@app.route('/')
def index():
    return "hello"

# command to get all the stock
@app.route('/stock')
def getAll():
    return jsonify(stock) 

# find stock by ID
@app.route('/stock/<int:id>')  
def findById(id):
    #use lambda function converting stock into the list
    foundStock = list(filter (lambda t : t["id"]== id, stock))
    # add user error to be displayed
    if len(foundStock) == 0:
        return jsonify({}) , 204
    return jsonify(foundStock[0])
    return "served by find by id with it "+ str(id)

# create stock with POST
@app.route('/stock', methods=['POST'])
def create():
    # pull id
    global nextId
    # if request is not json send error 400
    if not request.json:
        abort(400) 
#create new stock item
    stockItem = {
        "id": nextId,
        "Product": request.json["Product"],
        "Quantity": request.json["Quantity"],
        "Price": request.json["Price"]
    }
    stock.append(stockItem)
    nextId += 1
    return jsonify(stockItem)

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
