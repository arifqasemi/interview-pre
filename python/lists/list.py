#---------------- operations ------------
# num = 2
# num1 = 3

# print(num * num1)



# num = 2
# num1 = 3

# print(num / num1)


# num = 25
# num1 = 4

# print(num // num1)

# num = 2
# num1 = 3

# print(num ** num1)

# num = 2
# num1 = 3

# print(num % num1)

################# practice ###############

# greeting ='hello'
# greeting +=' world'

# print(greeting)

# number = 1
# number +=1
# print(number)

# my_list =['item']
# my_list *=3
# print(my_list)

# my_list = [3]
# my_list *=2
# print(my_list)

#-------------- varaible --------------

# var = 'hello'
# my_var = 'world'
# print(var)



#--------------- functions -------------


# def foo():
#     """
#     this is a function
#     ''' function '''
#     """


# foo()


#----------- print --------

# print('hello')

# num = 1
# print('hellow',num)

# my_lst =['okaye','oh','wow']

# for word in my_lst:
#     print(word,end='-')


# print('i','am','practicing','python','code',sep=',')



#--------------- input function -------------
# print('what is your name?')
# input_data = input('What is your name?')


# print('Hi,{}'.format(input_data))



#---------------- len function ----------------

# print(len('hellow'))

# print(len(['cat',3,'dog']))


#---------------- test of emptiness----------------

## Bad
# a = []
# if len(a) >0:
#     print('the list is not empty')



# if a:
#     print('the list is not empty')
# else:
#     print('empty')




#--------------------- The str(), int(), and float() Functions ----------------------

# print(str(24))
# print(int('11'))
# print(float('3.4'))




#---------------- build in functions --------------


# a = dict()

# print(type(a))

# print(max([1,3,4,6,7]))

# print(min([1,3,4,6,7]))
# print(len([1,3,4,6,7]))



# print(reversed([1,3,4,6,7]))

# furniture = ['table', 'chair', 'rack', 'shelf']
# print(furniture[::2])

# furniture = ['table', 'chair', 'rack', 'shelf']

# print(sorted(furniture))


# text = "hello world"
# words = text.split()
# print(words)


# line = "name:age:location"
# info = line.split(":",1)
# print(info)

#----------------- functions -----------------

# add = lambda x,y:x*y

# print(add(5,8))

# def make_adder(n):
#     return lambda x: x + n

# add_num = make_adder(4)
# print(add_num(3))




#----------------- List and Tuple ----------------- 

# furniture = ['table', 'chair', 'rack', 'shelf']
# print(furniture)
# furniture.clear()
# print(furniture)
# print(furniture[3])
# print(furniture[-3])
# print(furniture[-1])

# for i in furniture[:2:]:
#     print(i)

####### Changing values with indexes



# furniture = ['table', 'chair', 'rack', 'shelf']

# furniture[0] ='computer'


# print(furniture)



######## Concatenation and Replication


# my_list = [1, 2, 3] + ['A', 'B', 'C']
# print(my_list)


######### Getting the index in a loop with enumerate()

# furniture = ['table', 'chair', 'rack', 'shelf']

# for i,n in enumerate(furniture):
#     print(i,n)

########### Loop in Multiple Lists with zip()


# price = [100, 50, 80, 40]


# for item,amount in zip(furniture,price):
#     print(item,amount)


############# The in and not in operators


# if 'rack' not in furniture:
#     print('it is not there')

# else:
#     print('it is there')

######### The index Method

# print(furniture.index('shelf'))



############ Adding Values
# furniture.append('sofa')

# furniture.insert(0,'bed')

# print(furniture)

# del furniture[0]
# print(furniture)


# furniture.remove('chair')
# print(furniture)

# furniture.pop()

# sorted(furniture)

# print(sorted(furniture,reverse=False))
# furniture.sort(reverse=True)
# print(furniture)

# tuple(['cat', 'dog', 5])

# list(('cat', 'dog', 5))




#----------------- Python Dictionaries -----------------

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}


##############   Set key, value using subscript operator []
# my_cat['size'] ='thin'

# my_cat['age'] =12
# print(my_cat)


########### keys

# for key in my_cat.keys():
#     print(key)



############ values


# for value in my_cat.values():
#     print(value)



######### items


# for item in my_cat.items():
#     print(item)


# print(f'my cat is {my_cat.get('size')}')


# print(my_cat)

# my_cat.pop('color')
# print(my_cat)

# del my_cat['disposition']

# print(my_cat)
# my_cat
######################### Checking keys in a Dictionary

# if 'size' in my_cat.keys():
#     print('it is')


######################### Checking values in a Dictionary

# if 'size' in my_cat.values():
#     print('it is')

# import pprint


# pprint.pprint(my_cat)

####################### Merge two dictionaries
# my_dic ={
#     'color':'white',
#     'size':'thin',
#     'weight':'2kg'
# }
# merge_dic = {**my_cat,**my_dic}

# print(merge_dic)


###################### set

# s = set([1, 2, 3])
# print(type(s))
# s = {1, 2, 3}
# s.add(4)


# s = {1, 2, 3}
# s.update([2, 3, 4, 5, 6])


################ set remove and discard
# s = {1, 2, 3}
# s.remove(3)




#------------------------------- comperhensions ---------------------


names = ['Charles', 'Susan', 'Patrick', 'George']
new_list =[]

# new_list = [name for name in names]
# print(new_list)


# n = [(a,b) for a in range(1,3) for b in range(1,3)]
# print(n)
# tags = 'doctor,nurse'

# new_list = ['#' + name.capitalize() for name in tags.split(',')]

# print(new_list)

# nums = [1, 2, 3, 4, 5, 6]
# new_nums =[num  for num in nums if num !=1 ]

# print(new_nums)


# c = {'name': 'Pooka', 'age': 5}
# c['email'] = 'pooka@gmail.com'
# print(c)

# d = {k:n   for k, n in c.items() if k =='name'}

# print(d)


#------------------------ manipulating strings ---------------------


# print('how are you?\nwhat is your name\nI\'m doing fine.')


############## multiline Strings

# print("""Dear John, '''how are you? '''are you okay? """)


###################### Indexing and Slicing strings

# spam = 'Hello world!'

# print(spam[:5])

#################### The in and not in operators

# if 'Hello' in 'Hello World':
#     True


# 'Hello world!'.startswith('Hello')
# # True

# 'Hello world!'.endswith('world!')
# # True

# 'abc123'.startswith('abcdef')
# # False

# 'abc123'.endswith('12')

# st = ''.join(['My', 'name', 'is', 'Simon'])
# print(st)
# 'MynameisSimon'

# st = ', '.join(['cats', 'rats', 'bats'])
# print(st)
# 'cats, rats, bats'

# st = ' '.join(['My', 'name', 'is', 'Simon'])
# 'My name is Simon'

# 'ABC'.join(['My', 'name', 'is', 'Simon'])


# 'Hello'.rjust(10)
# # '     Hello'

# 'Hello'.rjust(20)
# # '               Hello'

# 'Hello World'.rjust(20)
# # '         Hello World'

# 'Hello'.ljust(10)
# # 'Hello     '

# 'Hello'.center(20)







############# Replace Method

# text = "Hello, world!"
# text.replace("world", "planet")
# # 'Hello, planet!'

# fruits = "apple, banana, cherry, apple"
# fruits.replace("apple", "orange", 1)



#--------------------------- class ----------------#

# class User:
#     def __init__(self,data):
#         self.firstname = data['firstName']
#         self.lastName = data['lastName']
#         self.products = []
#     def __str__(self):
#         return f"{self.firstname}"

#     def addProduct(self,data):
#         self.products.append(data)

# class Category:
#     def __init__(self,data):
#         self.id = data['id']
#         self.name = data['name']
#     def __str__(self):
#         return f"{self.name}"

# class Product:
#     def __init__(self,data):
#         self.name = data['name']
#         self.descriptioin = data['description']
#         self.image = data['image']
#         self.price = data['price']
#         self.category = data['category']
#         self.owner = data['user']
#         data['user'].addProduct(self)
#     # def __str__(self):
#     #     return f"{self.name}"
    
# user = User({'firstName':'mhd','lastName':'hamid'})
# category = Category({'name':'electric','id':'2ld'})
# data = {'name':'Iphone','description':'new brand iphone','image':'image','price':12,'category':category,'user':user}
# products = Product(data)

# print(products.owner)



#----------------------- abstractions -----------------#
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def test(self,data):
        return 'ddd'
    

class Cat(Animal):
    def test(self,data):
        return 'howw'

