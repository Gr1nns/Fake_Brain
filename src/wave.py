import random as rd

# 1 = Hz,  2 = Amp
def delta():
    d1 = rd.uniform(0.5, 4.0)
    d2 = rd.uniform(20.0, 200.0)
    return d1, d2
    
def theta():
    t1 = rd.uniform(4.0, 8.0)
    t2 = rd.uniform(10.0, 100.0)
    return t1, t2
    
def alpha():
    a1 = rd.uniform(8.0, 13.)
    a2 = rd.uniform(5.0, 50.0)
    return a1, a2
    
def mu():
    m1 = rd.uniform(9.0, 12.0)
    m2 = rd.uniform(5.0, 30.0)
    return m1, m2
    
def sigma():
    s1 = rd.uniform(12.0, 16.0)
    s2 = rd.uniform(5.0, 20.0)
    return s1, s2
    
def beta():
    b1 = rd.uniform(13.0, 30.0)
    b2 = rd.uniform(1.0, 20.0)
    return b1, b2
    
def gamma():
    g1 = rd.uniform(30.0, 60.0)
    g2 = rd.uniform(0.5, 10.0)
    return g1, g2
    
def high_gamma():
    hg1 = rd.uniform(60.0, 100.0)
    hg2 = rd.uniform(0.1, 5.0)
    return hg1, hg2
