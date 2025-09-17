'''
API URL:https://dummyjson.com/products
Method Type:GET
'''
import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
print 