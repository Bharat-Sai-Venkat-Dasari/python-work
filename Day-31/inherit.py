# class Whatsappv1:

#     def messaging(self):
#         print("You can send messages")

# class Whatsappv2(Whatsappv1):

#     def calls(self):
#         print("You can make audio and video calls")

# class Whatsappv3(Whatsappv2):
#     def status(self):
#         print("You can add the status for 24 hours.")


# dasari = Whatsappv1()
# dasari.messaging()

# bharat = Whatsappv2()
# bharat.calls()
# bharat.messaging()

# sai = Whatsappv3()
# sai.status()
# sai.calls()
# sai.messaging()




# class Whatsappv1:

#     def messaging(self):
#         print("You can send messages")

# class Whatsappv2:

#     def calls(self):
#         print("You can make audio and video calls")

# class Whatsappv3(Whatsappv1, Whatsappv2):
#     def status(self):
#         print("You can add the status for 24 hours.")


# dasari = Whatsappv1()
# dasari.messaging()

# bharat = Whatsappv2()
# bharat.calls()
# bharat.messaging()

# sai = Whatsappv3()
# sai.status()
# sai.calls()
# sai.messaging()



# class Whatsappv1:

#     def messaging(self):
#         print("You can send messages")

# class Whatsappv2(Whatsappv1):

#     def calls(self):
#         print("You can make audio and video calls")

# class Whatsappv3(Whatsappv1):
#     def status(self):
#         print("You can add the status for 24 hours.")


# dasari = Whatsappv1()
# dasari.messaging()

# bharat = Whatsappv2()
# bharat.calls()
# bharat.messaging()

# sai = Whatsappv3()
# sai.status()
# sai.calls()
# sai.messaging()


# class Whatsappv1:

#     def messaging(self):
#         print("You can send messages")

# class Whatsappv2:

#     def extramessages(self):
#         print("You can emojis, stickers and gifs")

# class Whatsappv3(Whatsappv1, Whatsappv2):

#     def calls(self):
#         print("We can add audio and video calls")

# class Whatsappv4(Whatsappv3):
#     def status(self):
#         print("You can add the status for 24 hours.")


# a = Whatsappv1()
# a.messaging()

# b = Whatsappv2()
# b.extramessages()

# c = Whatsappv3()
# c.calls()
# c.messaging()

# d = Whatsappv4()
# d.status()
# d.calls()



# class Whatsappv1:
#     def status(self):
#         print("You can add images and videos")

# class Whatsappv2(Whatsappv1):
#     def status(self):
#         super().status()
#         print("You can add music, stickers.")

# class Whatsappv3(Whatsappv2):
#     def status(self):
#         super().status()
#         print("You can like and you can reaction")

# a = Whatsappv1()
# a.status()

# b = Whatsappv2()
# b.status()

# c = Whatsappv3()
# c.status()




class Whatsappv1:
    def status(self):
        print("You can add images and videos")

class Whatsappv2:
    def status(self):
        print("You can add music, stickers.")

class Whatsappv3(Whatsappv1, Whatsappv2):
    def status(self):
        Whatsappv1.status(self)
        Whatsappv2.status(self)
        print("You can like and you can reaction")

a = Whatsappv1()
a.status()

b = Whatsappv2()
b.status()

c = Whatsappv3()
c.status()