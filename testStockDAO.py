from stockDAO import stockDao

stock1 = {
    'id':80,
    'product': 'white wine',
    'quantity': 50,
    'price': 25
}

stock2 = {
    'id': 80,
    'product': 'Greek wine',
    'quantity': 30,
    'price': 90

}
#returnvalue = stockDao.create(stock)
returnvalue = stockDao.getAll()
print(returnvalue)
returnvalue = stockDao.findByID(stock2['id'])
print("find by id")
print(returnvalue)
returnvalue = stockDao.update(stock2)
print(returnvalue)
returnvalue = stockDao.findByID(stock2['id'])
print(returnvalue)
returnvalue = stockDao.delete(stock2['id'])
print(returnvalue)
returnvalue = stockDao.getAll()
print(returnvalue)


