#Positional Arguments

# def display(name, email, password):
#     print(f'Name: {name}')
#     print(f'Email: {email}')
#     print(f'Password: {password}')
    
# display('Bharat', 'bharat123@gmail.com', '12345')


#Keyword Arguments

# def display(name, email, password):
#     print(f'Name: {name}')
#     print(f'Email: {email}')
#     print(f'Password: {password}')
    
# display(name='Bharat', email='bharat123@gmail.com', password='12345')
# display(password='Bharat123', email='bharat123@gmail.com', name='Bharat')

#Default Arguments

# def display(name='Bharat', email='bharat@gmail.com', password='Bharat123'):
#     print(f'Name: {name}')
#     print(f'Email: {email}')
#     print(f'Password: {password}')
    
# display(name='Bharat', email='bharat123@gmail.com')
# display()
# display(email='bharatdasari111@gmail.com')

#Variable Length Arguments

# def display(*names):
#     print(names)

# display('Bharat')
# display('Bharat', "Avinash")
# display('Bharat', 'Avinash', 'Lokesh')
# display('Bharat', 'Avinash', 'Lokesh', 'NaraSimha')
# display('Bharat', 'Avinash', 'Lokesh', 'NaraSimha', 'Vikas')

#Keyword Variable Length Arguments

def display(**products):
    print(products)

display(Bag = 500)
display(Bag = 500, Book = 100)
display(Bag = 500, Book = 100, Bottle=200)