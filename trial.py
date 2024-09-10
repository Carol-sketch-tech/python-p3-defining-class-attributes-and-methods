# defining class attribute and class methods.
'''
when we have a class name Album has attribute of name and date of an instance.
however we can consider Album to be and object because an object is anything that has attributes and methods.
the attributes and methods of a class are called class attributes and class methods.

'''

class Album:

    album_count = 0# setting an class attribte that stores the number of album isntances created.
    def __init__(self,name, date):
        self.name= name
        self.realease_date= date
        Album.album_count += 1 

lemonade = Album("lemonade", "12-8- 2018")
pieces = Album('pieces', '12-12-1331')

print(lemonade.name)
print(lemonade.realease_date)

# why do we use class attributes and class methods.
'''
for instance say we want ot keep track of the albums we own,
our current code has no way of knowing this.
we currently have our album class and album instance, so it the responsibility of the album class to keep count
of all the other albums.

how then do we enact this behaviour (of keeping count of all album instances)?
we do so with the use of class attributes and methods.
when we ask class to tell us something about itself, we use methods.


# Defining a class attrubute.
A clas atribute is declaredusing the same notation as anywhere else.
a class attribute must be decalred outside af any methods in the class.

# manipualting class attributes from instance methods.
note that our album count is stuck at 0. 
when and how should we increamnt it?

the count of album should go out as soon as a new album is created. or initialized.
we can do this by hooking into this moment on time our __init__ method.

note that we have used album_count class attribute inside of our __init__ method and instance method,
we are saying that when a new album is created, accees the album_count class atriute and increament its value by 1.
using our class name dot notation we can access nout class attributes anywhere in our class, in both class and instance methods
'''
print(Album.album_count)
print(lemonade.album_count)

# DEFINIG A CLASS METHOD.
'''
a class method is defined as follows:
@classmethod
def class_method_name(cls):
  .... some code in here.

  when we use the @classmethod decorator in python, it tell the interpreter that the method being defined is a class 
  method.
  Unlike the instance method whcih operarted on an instance of the class and have access to the instance via self,
  class methods operate on the class itself and have access to the class via cls

  here's a quick rundown of what happens when you define a class method:
      
     1. method binding-> the @classmethod decorator binds the method to the clas rather than to instances of the class. 
     this means that when you call a class method, its invokes onnthe class itself, not on an intance.

     2. first parameter-> the first parameter of a class methos is typically named cls(though you can use 
     any name). this parameter represents the class and allows you to access attributes and other class methods from within the method.
     3. accessing class data -> class methods are often ued for operations that need to access or modify class-level data.
     or for factory methods that create instances of the class using different set of parameters.


# lets refactor our class Album class so that album_count can be changed by the class itself.
'''
class Another_album:
    def __init__(self, name,date):
        self.name= name
        self.release_date = date

    @classmethod
    def album_count(cls, increament = 1):
        cls.album_count += increament

    # in this example. we have an Another_album class that inceases the number of albums as we get new ones,
    # but that does so through a method connected to the class itseld rather than new objects.


'''
CLASS CONSTANTS.

One other type od constant that can be useful when building out classes is a class constant.
class constants have alot in common with class attributes.
   - they are defined in the body of the class.
   - can be accessed from within a class method.
   - can be accessed within an instance method.

a class constant looks a bit different than a class attribute.
it is defines using capital letters.
when deciding when to use a class cosntnat or a class attribute, the key distiction is that class cosntants are 
used to store data that does not change(it is constant), while class attributes are used to store data that does change.
'''

class User:
    ROLES = ['Admin','Moderater', 'Contributer']# this is a class constant.

class Second_Album_Class:
    GENRES = ['Hiphop',  'jazz', 'soul', 'RnB', 'Pop']
    album_count = 0
    def __init__(self,genre, date):  # the __init__ method is the initializer method that is called when an new instance of Second_Album_Class is created. it takes genre and date as paramters.
        if self.check_genre(genre):  # this is to validate if the provided  genre is in the list of alloed genres.
            self.increase_album_count()  # if the genre is valid it calls  self. increament _album_count() to increament the album_count.
            self.genre = genre # it then sets the genre and release_date attributes for the instance.
            self.release_date = date
        else:
            raise ValueError(f'Invalid genre: {genre}') # this else statements is for handling invalid inputs. Rasing an exception.

    @classmethod
    def check_genre(cls, genre):# this method is used for genre validation.
        return genre in cls.GENRES # checks if the provided genre is in the GENRES list.
    
    @classmethod
    def increase_album_count(cls, increament = 1):
        cls.album_count += increament
bongo = Second_Album_Class('soul', '12-22-2333')
print(bongo.genre)
print(Second_Album_Class.GENRES)
Second_Album_Class.GENRES = 'i dont know any genres of music'
print(Second_Album_Class.GENRES)


'''
Scope-wise, class constants can also be accessed from outside of the class using this Syntax
Album.GENRES

unlike in javascript, declaring a constant variable in python doesnt actually prevent the variable from being reassigned.
it is however a good indicator to other developers that they shouldnt reassign the variables value.
'''