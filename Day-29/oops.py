class Playstation:
    products = {'PS5 Console': 50000, 'Gaming CDs': 10000, 'Sony PS Controller': 5000}
    discount = 20

    @staticmethod
    def greeting():
        print("Have a Great Day!!")
        print(f'{Playstation.discount}% is your discount.')

    @classmethod
    def display(cls):
        print(f"Product are: {cls.products}")

    def userinfo(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to PlayStation Store!!")

bharat = Playstation()
bharat.userinfo('Bharat Dasari', 1234567890, 'Hyderabad')
bharat.display()
bharat.greeting()

#using Object (we can acsess) --> ins, cls, stat, clsatt, instatt
#using Class (we can acsess) --> cls, stat, clsatt