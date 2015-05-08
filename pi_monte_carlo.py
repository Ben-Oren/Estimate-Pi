
from pylab import plot, show, axis
from numpy import random, sqrt, pi

# scattering n points over the unit square
n = input("How many points? Hint: lots" )
n = int(n)
p = random.rand(n,2)

# counting the points inside the unit circle
idx = sqrt(p[:,0]**2+p[:,1]**2) < 1

plot(p[idx,0],p[idx,1],'b.') # point inside
plot(p[idx==False,0],p[idx==False,1],'r.') # point outside
axis([-0.1,1.1,-0.1,1.1]) 
show()
result = (sum(idx).astype('double')/n*4) # store estimate in var "result"


# print estimation of pi
print '%0.16f' % result,'result'
print '%0.16f' % pi,'real pi'
print '%0.16f' % ((result - pi) / pi) * 100), 'percent difference between estimate and real value of pi'
