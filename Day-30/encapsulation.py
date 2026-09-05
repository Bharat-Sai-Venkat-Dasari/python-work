class Instagram:

    def __init__(self, username, password, post):
        self.username = username
        self.__password = password
        self._post = []
        print(f'Hello {self.username}, Welcome to Instagram!!')

    def get_password(self):
        return self.__password
    
    @property
    def access_posts(self):
        return self._post

    @access_posts.setter
    def access_posts(self, newpost):
        self._post.append(newpost)

    def setpassword(self, newpassword):
        self.__password = newpassword
    

bharat = Instagram('Bharat Dasari', 'bharat7', [])
print(bharat.username)
print(bharat.get_password())
print(bharat.access_posts)

bharat.username = 'Bharat'
print(bharat.username)

bharat.setpassword('Bharat123')
print(bharat.get_password())

bharat.access_posts = 'Spiderman.png'
bharat.access_posts = 'Uncharted4.png'
bharat.access_posts = 'RedDeadRedemption.png'
print(bharat.access_posts)

#using Object (we can acsess) --> ins, cls, stat, clsatt, instatt
#using Class (we can acsess) --> cls, stat, clsatt