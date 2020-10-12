"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Encapsulation :- refers to the creation of self-contained modules that bind 
processing functions to the data. 

Abstraction:- Abstracting  the structure and method from parent class ie tyhis way 
programming can be more structured and ignore multiple, complex coding.

Polymorphism:-Object-oriented programming allows procedures about objects to be 
created whose exact type is not known until runtime.

2. What is a class?
 it is a object constructor, its like a blueprint for creating an OOP
 It can even be called as smarter dictionary which has its own smarts, is more structured  
 and is flexible too. 

 

3. What is a method?
it is a fuction defined in class.Objects contain methods. Methods in objects are functions that belong 
to the object.



4. What is an instance in object orientation?
An instance, in object-oriented programming (OOP), is a specific representation of 
any object. An object is a generic thing while an instance is a single object that 
has been created in memory.
(replace this with your answer)


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
"""

"""2. Road Class"""

class Road:
    num_lanes=2
    speed_limit=25
    def __init__(self,num_lanes,speed_limit):
        self.num_lanes=num_lanes
        self.speed_limit=speed_limit
Road_1= Road(4,60)
Road_2=Road(2,25)


# Replace this with your code


"""3. Update Password"""
class User:
    
    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password


    def update_password(self, current_pass,new_pass):
        if current_pass == self.password:
           self.password=new_pass
           print ("updated password to "+ new_pass)
        else:
            print("invalid password")

"""4. """
class Book(object):
    """A Book object."""
    book_by_author=[]
    def __init__(self, title, author):
        """Create a book with the given title and author."""
        self.title = title
        self.author = author

class Library():
    def __init__(self):      
        self.books= []

    def create_and_add_book(self,title,author):
        book_obj = Book(title, author)
        self.books.append(book_obj)
        
    def find_books_by_author(self,author):
        books_by_author=[]
        for book in self.books:
            if author==book.author:
                books_by_author.append(book.title)
            
        return books_by_author


"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)
    
    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width



class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
        self.length=self.width
    
    
    def calculate_area_square(self):
        """Return the area of the square."""
        if self.length == self.width:
            super().calculate_area()
        else:
            print("invalid square")


    
