def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
        if isinstance(top,int) and isinstance(bottom,int):
            common = gcd(top,bottom)
            self.num = top//common
            self.den = bottom//common
        else:
            raise ValueError('value Error! The value has to be a integer')
         

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         
         return Fraction(newnum,newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
        
     def getNum(self):
        return self.num
    
     def getDen(self):
        return self.den
    
     def __sub__(self,otherfraction):
        nnum = self.num*otherfraction.den - \
                 self.den*otherfraction.num
        nden = self.den * otherfraction.den
        
        return Fraction(nnum,nden)
        
     def __mul__(self,other):
         mnum = self.num * other.num
         mden = self.den * other.den
         
         return Fraction(mnum,mden)
        
    def __truediv__(self,other):
        dnum = self.num * other.den
        dden = self.num * other.num
        
        return Fraction(dnum,dden)
    
    def __gt__
    
    

x = Fraction(1,2)
y = Fraction(2,3)
print(y.getNum())
print(x*y)
print(x == y)

print
