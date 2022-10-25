import numpy as np

# Emmett, here I create 4 vectors from the problem. They are complex valued. change the values if you like (in python, j is i)

v1 = np.transpose(np.array([(-4j/3),(-4j/3),2/3,2]).astype(complex)/(2*np.sqrt(2)))
v2 = np.transpose(np.array([2j/3,-1j/3,2/3,0]).astype(complex))
v3 = np.transpose(np.array([0,2j,1,1]).astype(complex)/(np.sqrt(6)))
v4 = np.transpose(np.array([1j,0,-1,1]).astype(complex)/(np.sqrt(3)))

#Here is another set, I think representing the wrong answer mathematica gave. comment out the above ones and bring these in to run it for these

# v1 = np.transpose(np.array([-2j,-1j,0,2]).astype(complex)/(2*np.sqrt(2)))
# v2 = np.transpose(np.array([2j,-1j,2,0]).astype(complex))
# v3 = np.transpose(np.array([0,2j,1,1]).astype(complex)/(np.sqrt(6)))
# v4 = np.transpose(np.array([1j,0,-1,1]).astype(complex)/(np.sqrt(3)))

#---------------------------------------------------------

#I define the inner product and outer product 

def ip(v1,v2):
    prod = np.matmul(np.transpose(np.conjugate(v1)),v2)
    return prod

def op(v1,v2):
    prod = np.matmul(v1,np.transpose(np.conjugate(v2)))
    return prod

#I make it so small numbers are treated as 0

def round(v):
    v[np.abs[v] < 0.000001] = 0
    return v


#just creating some organizational stuff
H = np.zeros((4,4))
vectors = [v1,v2,v3,v4]
lamda = [-4,-4,2,-1]

#magic formula on eigenvectors H = sum (eigenvector times |psi><psi|)
for i in range(4):
        vi = vectors[i] #get vector
        M = np.outer(vi,np.conjugate(vi)) # do |eigenvector> <conjugate transpose eigenvector|
        M = M*lamda[i] #multiply the eigenvalue 
        H=np.add(H,M) #place it in the matrix

H = np.around(H,decimals=1)

print(f'Matrix: \n {H}') #output the matrix


#print((np.outer(v1,np.conjugate(v2))))





