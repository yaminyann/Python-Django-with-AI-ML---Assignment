# Apply set union
a = {55,6,8,9,11}
b = {44,55,89,54}
print(' set union : ', a | b)
print(' set union ', a.union(b))


# which data type not duplicate , give an example
    # answare is set
    # example
a = {55,6,8,9,110,44,55,89,54}
print(a)


# print dictonarys key
myDict = {
    'djnago': 10,
    'project' : 5,
    'student' : 20,

}
keys = myDict.keys()
print(keys)



# create a function and call the function
def myFunc(name,email):
    print("MY name is ",name,' MY email is ',email)

print(myFunc('yamin','yaminredmi5@gmail.com'))



# create class and object
class Veicle:
    def __init__(self,brand,model,color,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def BrandName(self):
        print('Brand name is : ',self.brand)

    def Model(self):
        print('Model is : ', self.model)

    def Color(self):
        print('Color is :',self.color)

    def Price(self):
        print('Price is : ',self.price)

bike = Veicle('YAMAHA',"FZ-S",'Black',220000)
car = Veicle('TOYOTA','AXIO','Red',1500000)

bike.BrandName()
car.BrandName()
bike.Model()
car.Model()




# give an example on inheritance
class Car():
    def Start(self):
        print('Car is startting......')

    def Break(self):
        print('Car is breking..........')

    def Parking(self):
        print('car is parking......')
class Veicle(Car):
    def __init__(self,brand,model,color,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def BrandName(self):
        print('Brand name is : ',self.brand)

    def Model(self):
        print('Model is : ', self.model)

    def Color(self):
        print('Color is :',self.color)

    def Price(self):
        print('Price is : ',self.price)


bike = Veicle('YAMAHA',"FZ-S",'Black',220000)
mycar = Veicle('TOYOTA','AXIO','Red',1500000)

mycar.Start()
bike.Parking()