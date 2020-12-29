# create a basic flask server and import url and requests
from flask import Flask, url_for, request, redirect,abort, jsonify
from stockDAO import stockDao

app = Flask(__name__,static_url_path='',static_folder='staticPages') #. means this folder

@app.route('/')
def index():
    return "hello test for pythonanywhere"

# command to get all the stock
@app.route('/stock')
def getAll():
    return jsonify(stockDao.getAll()) 

# find stock by ID
@app.route('/stock/<int:id>')  
def findById(id):
    return jsonify(stockDao.findByID(id)) 
    
# create stock with POST
#curl -X POST -d "{\"Product\":\"test\", \"Quantity\":89, \"Price\":123}" http://127.0.0.1:5000/stock
@app.route('/stock', methods=['POST'])
def create():

    if not request.json:
        abort(400) 
#create new stock item
    stock = {
        "product": request.json["product"],
        "quantity": request.json["quantity"],
        "price": request.json["price"]
    }   
    return jsonify(stockDao.create(stock))

# update
# curl -X PUT -d "{\"Product\":\"White wine\", \"Price\":66}" -H "content-type:application/json" http://127.0.0.1:5000/stock/1
@app.route('/stock/<int:id>', methods=['PUT'])  
def update(id):
    #to update the stock with the new info
    foundStock=stockDao.findByID(id)
    print (foundStock)
    # add user error to be displayed
    if foundStock == {}:
        return jsonify({}), 404
    currentStock = foundStock
    if 'product' in request.json:
        currentStock['product'] = request.json['product']
    if 'quantity' in request.json:
        currentStock['quantity'] = request.json['quantity']
    if 'price' in request.json:
        currentStock['price'] = request.json['price']
    stockDao.update(currentStock)
    return jsonify(currentStock)

# delete
# curl -X "DELETE" http://127.0.0.1:5000/stock
@app.route('/stock/<int:id>', methods=['DELETE'])  
def delete(id):
    stockDao.delete(id)
    return jsonify({"done":True})

if __name__ == "__main__":  
    app.run(debug=True)


#Map POST method
