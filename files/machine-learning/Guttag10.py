# -*- coding: utf-8 -*-

# # Code from page 179
class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
        
    def size(self):
        return len(self._elems)

#print(type(Toy))
#print(type(Toy.__init__), type(Toy.add), type(Toy.size))

# # Code from page 180
#t1 = Toy()
#print(type(t1))
#print(type(t1.add))
#t2 = Toy()
#print(t1 is t2) #test for object identity

# # Code from page 181
#t1 = Toy()
#t2 = Toy()
#t1.add([3, 4])
#t2.add([4])
#print(t1.size() + t2.size())

# # Figure 10-1 from page 182
class Int_set(object):
    """An Int_set is a set of integers"""
    #Information about the implementation (not the abstraction):
      #Value of a set is represented by a list of ints, self._vals.
      #Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self._
           Nothing can be assumed about the order of the elements"""
        return self._vals[:]
    
    #Finger Exercise p.184
    def union(self, other):
        """other is an Int_set
           mutates self so that it contains exactly the elements in self
           plus the elements in other."""
        for item in other.get_members():
            self.insert(item)
        
        

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}' #'{{0}}'.format(result[:-1])
  
# # Code from page 183
#s = Int_set()
#s.insert(3)
#print(s.member(3))

# # Code from page 184
# s = Int_set()
# s.insert(3)
# s.insert(4)
# print(str(s))
# print('The value of s is', s)


# # Figure 10-2 on page 185
class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
        
    def size(self):
        return len(self._elems)
    def __len__(self):
        return len(self._elems)
    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    def __eq__(self, other):
        return self._elems == other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
        return id(self)
    
#t1 = Toy()
#t2 = Toy()
#t1.add([1, 2])
#t2.add([3, 4])
#t3 = t1 + t2
#print('The value of t3 is', t3)
#print('The length of t3 is', len(t3))
#d = {t1: 'A', t2: 'B'}
#print('The value', d[t1], 'is associated with the key t1 in d.')

#-----------------------------------------------------------------------------

# # Import used for class Person        
import datetime

# # Figure 10-3 from page 189
class Person(object):
    
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate
        
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name

# # Code from page 188
# me = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print(him.get_last_name())
# him.set_birthday(datetime.date(1961, 8, 4))
# her.set_birthday(datetime.date(1958, 8, 16))
# print(him.get_name(), 'is', him.get_age(), 'days old')

# # Code from page 190
# p_list = [me, him, her]
# for p in p_list:
#     print(p)
# p_list.sort()
# for p in p_list:
#     print(p)

# # Figure 10-4 from page 192
class MIT_person(Person):
    
    _next_id_num = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num

# # Code from page 192
# p1 = MIT_person('Barbara Beaver')
# print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))

# # Code from page 193
p1 = MIT_person('Mark Guttag')
p2 = MIT_person('Billy Bob Beaver')
p3 = MIT_person('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

# print('p1 < p2 =', p1 < p2)
# print('p3 < p2 =', p3 < p2)
# print('p4 < p1 =', p4 < p1)

# print('p1 < p4 =', p1 < p4)

# Finger exercise from page 194
class Politician(Person):
    """ A politician is a person that can belong to a political party"""
    
    def __init__(self, name, party = None):
        """name and party are strings"""
    
    def get_party(self):
        """returns the party to which self belongs"""
    
    def might_agree(self, other):
        """returns True if self and other belong to the same part
             or at least one of then does not belong to a party"""
    
# # Figure 10-5 from page 194
class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year
    
class Grad(Student):
    pass

# # Code from page 195
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate student is', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)

# # Code from page 195 -- Should be added to class MIT_Person
def is_student(self):
    return isinstance(self, Student)

# print(p5, 'is a student is', p5.is_student())
# print(p6, 'is a student is', p6.is_student())
# print(p3, 'is a student is', p3.is_student())

# # Code from page 196
class Transfer_student(Student):

    def __init__(self, name, from_school):
        MIT_person.__init__(self, name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school

       
# # Figure 10-8 from page 201
class info_hiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__also_visible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'    
        
    def print_visible(self):
        print(self.visible)
        
    def print_invisible(self):
        print(self.__invisible)
        
    def __print_invisible(self):
        print(self.__invisible)
        
    def __print_invisible__(self):
        print(self.__invisible)

# # Code from page 201
#test = info_hiding()
#print(test.visible)
#print(test.__also_visible__)
#print(test.__invisible)

#test = info_hiding()
#test.print_invisible()
#test.__print_invisible__()
#test.__print_invisible()

# # Code from page 202
class Sub_class(info_hiding):
    def new_print_invisible(self):
        print(self.__invisible)       

#test_sub = Sub_class()
#test_sub.new_print_invisible()

#s = Toy()