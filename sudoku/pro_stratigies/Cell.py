class Cell:
    def __init__(self, cordinates, value = 0):
        self.x = cordinates[0]
        self.y = cordinates[1]
        self.incumbent = value
        self.candidates = []
        self.noncandidates = [0]

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def candidates(self):
        return self.__candidates
    
    @candidates.setter
    def candidates(self,candidates):
        self.__candidates = candidates

    @property
    def noncandidate(self):
        return self.__noncandidates   
    
    @noncandidate.setter
    def noncandidate(self,noncandidates):
        self.__noncandidates = noncandidates
    
    def __lt__(self,other):
        return self.incumbent < other

    def __le__(self,other):
        return self.incumbent <= other

    def __gt__(self,other):
        return self.incumbent > other

    def __ge__(self,other):
        return self.incumbent >= other

    def __eq__(self,other):
        return self.incumbent == other

    def __ne__(self,other):
        return self.incumbent != other

    def __repr__(self):
        if self.incumbent != 0 :
            return "%s" % self.incumbent
        else:
            return "%s" % self.candidates

    def __str__(self):
        return "<Cell x:%s, y:%s, candidates:%s, noncandidates:%s>" % (self.x, self.y, self.candidates, self.noncandidates)
