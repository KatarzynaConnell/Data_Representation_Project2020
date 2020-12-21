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
    return "hello test for pythonanywhere"

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
#curl -X POST -d "{\"Product\":\"test\", \"Quantity\":89, \"Price\":123}" http://127.0.0.1:5000/stock
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

# update
# curl -X PUT -d "{\"Product\":\"White wine\", \"Price\":66}" -H "content-type:application/json" http://127.0.0.1:5000/stock/1
@app.route('/stock/<int:id>', methods=['PUT'])  
def update(id):
        #to update the stock with the new info
    foundStock = list(filter (lambda t : t["id"]== id, stock))
    # add user error to be displayed
    if len(foundStock) == 0:
        return jsonify({}), 404
    currentStock = foundStock[0]
    if 'Product' in request.json:
        currentStock['Product'] = request.json['Product']
    if 'Quantity' in request.json:
        currentStock['Quantity'] = request.json['Quantity']
    if 'Price' in request.json:
        currentStock['Price'] = request.json['Price']

    return jsonify(currentStock)

# delete
# curl -X "DELETE" http://127.0.0.1:5000/stock
@app.route('/stock/<int:id>', methods=['DELETE'])  
def delete(id):
    foundStock = list(filter (lambda t : t["id"]== id, stock))
    # add user error to be displayed
    if len(foundStock) == 0:
        return jsonify({}), 404
    stock.remove(foundStock[0])

    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True)


#Map POST method
