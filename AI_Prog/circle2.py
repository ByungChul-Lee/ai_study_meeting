pi = 3.141592123

def area(r):
    return pi*(r**2)

def circumference(r):
    return 2*pi*r

def sphereSurface(r):
    return 4.0*area(r)

def sphereVolume(r):
    return (4.0/3.0)*pi*(r**3)