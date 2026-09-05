class Whatsappv1:

    def __init__(self, name):
        self.name = name
        print(f"Welcome to the Whatsapp - v1 {self.name}!")

    def messaging(self):
        print("You can send messages")

class Whatsappv2(Whatsappv1):

    def calls(self):
        print("You can make audio and video calls")

bharat = Whatsappv2('Bharat Dasari')
bharat.calls()
bharat.messaging()