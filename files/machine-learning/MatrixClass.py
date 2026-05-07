#The Matrix Class

class Matrix():
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns = columns
        
        mat=[]
           
        for i in range(rows):
            row=[]
            for j in range(columns):
                row.append(0)
            mat.append(row)
        self.mat=mat
    
    def scalarMult(self,scalar):
        sM=Matrix(self.rows,self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                sM.mat[i][j]=scalar*self.mat[i][j]
        return sM
        
    def __add__(self, m):
        if self.rows==m.rows and self.columns==m.columns:
            sumM=Matrix(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    sumM.mat[i][j]=m.mat[i][j]+self.mat[i][j]
            return sumM
        else:
            print('Not conformable for addition')
    
    def __mul__(self,m):
        if self.columns==m.rows:
            prodM=Matrix(self.rows,m.columns)
            for i in range(self.rows):
                for j in range(m.columns):
                    Cij=0
                    for k in range(self.columns):
                        Cij=Cij+self.mat[i][k]*m.mat[k][j]
                    prodM.mat[i][j]=Cij
            return prodM
        else:
            print('Not conformable for multiplication')
                
   
    def POW(self,k):
        Z=self.Mult(self)
        for i in range(k-2):
            Z=Z.Mult(self)
        return Z
            
    def transpose(self):
        tM=Matrix(self.columns,self.rows)
        for i in range(self.columns):
            for j in range(self.rows):
                tM.mat[i][j]=self.mat[j][i]
        return tM    
        
    def sign(self):
        sM=Matrix(self.rows,self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                if self.mat[i][j] > 0.1:
                    sM.mat[i][j] = 1
                elif self.mat[i][j] < 0.1:
                    sM.mat[i][j] = -1
        return sM
    
    def __str__(self):
        mstring=''
        for i in range(self.rows):
            mstring=mstring+str(self.mat[i])+'\n'
        return mstring


m1=Matrix(4,4)
m1.mat = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]








