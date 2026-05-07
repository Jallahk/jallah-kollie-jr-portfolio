'''CS235 Program 1, Jallah Kollie, 2/1/2025
worked with Doran and Marcellus'''



#this imports the parent class (person) for Politician
from Guttag10 import Person    
    
# Finger exercise from page 194
class Politician(Person):
    """ A politician is a person that can belong to a political party"""
    
    def __init__(self, name, party = None):
        """name and party are strings"""
        self._name = name
        self.party = party
        
     #identifies partyName as the party or Independent if no party and returns the politician's Name and their party    
    def __str__(self):
        partyName = self.party if self.party else 'Independent'
        return f'{self._name} ({partyName})'
        
  
    def get_party(self):
        """returns the party to which self belongs"""
        return self.party
   
    def might_agree(self, other):
        """returns True if self and other belong to the same party
             or at least one of then does not belong to a party"""
        return self.party == other.party or self.party in {None, 'Independent'} or other.party in {None, 'Independent'}
                                                        #checks if there is no party or Independent 
        
class Representative(Politician):
    _term = 2
        
    def get_election_year(self,electionyear):
        ''' Sets self's election year to electionyear'''
        self.electionyear = electionyear
        return self.electionyear
    
    def get_reelection_year(self):
        return self.electionyear + self._term
        '''returns the sum of the election year and how long the term is '''
    
    
class Senator(Politician):
    _term = 6
                     
    def get_election_year(self,electionyear):
        " Sets self's election year to electionyear"
        self.electionyear = electionyear
        #return self.electionyear
    
    def get_reelection_year(self):
        return self.electionyear + self._term
        '''returns the sum of the election year and how long the term is '''
        
        
#------------------------------------------------------------- this is the test 
    
def program1test():
    p1 = Politician('Juliana Stratton', 'Democrat')
    print(p1)
    p2 = Senator('Richard Durbin', 'Democrat')
    print(p2)
    p2.get_election_year(2020)
    print(p2.get_reelection_year())
    p3 = Representative('Mary Miller', 'Republican')
    print(p3)
    p3.get_election_year(2024)
    print(p3.get_reelection_year())
    p4 = Senator('Bernie Sanders')
    print(p4)
    def collegial(p,q):
        if p.might_agree(q):
            coll = 'agree'
        else:
            coll = 'not agree'
        print(p.get_name(),'might',coll,'with',q.get_name())
    collegial(p2,p3)
    collegial(p1,p2)
    collegial(p4,p2)
    collegial(p4,p3)
program1test()      

