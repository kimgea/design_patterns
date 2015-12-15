
###############
#
#    Complex parts
###

class FreebaseAPI(object):
    
    def __init__(self, auth_key, auth_secret):
        self.auth_key = auth_key
        self.auth_secret = auth_secret
    
    def get_characters(self, isbn):
        #Get characters by using isbn
        return ["Harry Potter", "Snape"]
    
    def get_title(self, isbn):
        return "Harry Potter"


class AmazonAPI(object):
    
    def get_image(self, isbn):
        #Scrape image url by using isbn
        return "http://image.com"
    
    def get_author(self, isbn):
        return "J.K. Rowling"


class GoogreadsAPI(object):
    def get_rating(self, title, author):
        #Get rating of book from title and author
        return "8.9"
    

###############
#
#    Facade
###

class BookFacade(object):
    
    def __init__(self):
        self.freebase = FreebaseAPI("key","secret")
        self.amazon = AmazonAPI()
        self.goodreads = GoogreadsAPI()
    
    def display_book(self, isbn):
        title = self.freebase.get_title(isbn)
        author = self.amazon.get_author(isbn)
        print (title,"by",author)
        print ("Rating:",self.goodreads.get_rating(title, author))
        print ("Image url:",self.amazon.get_image(isbn))
        print ("Characters:",self.freebase.get_characters(isbn))
        
        
book = BookFacade()
book.display_book("isbn")
        
    
        


