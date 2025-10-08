class Order:
    ''' created by Narasimha '''
    def _init_(self,id,name,price):
        print("constructor is special method") 
        self.order_id=id 
        self.details=name 
        self.price=price
    def add_discount(self):
        self.discount=50

o1=Order(11,'MP1',35)
o2=Order(12,'MP2',40)
o3=Order(13,'MP3',45)
o1.add_discount()
o2.add_discount()

print(o1._dict_)
print(o2._dict_)
print(o3._dict_)