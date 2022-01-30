import random as r 
import math 

def breakStick(n):
  # Break a unit length stick into n pieces. Lengths are determined by the breaks.
  # Returns the unsorted lengths
  breaks = [0.0] + [r.random() for b in range(n-1)] + [1.0]
  breaks.sort()
  lengths = [breaks[i+1]-breaks[i] for i in range(n)]
  return lengths 

def isTriangle(lengths):
  # Given a list of three lengths, returns true if they can form a triangle.
  L = [lengths[0],lengths[1],lengths[2]]
  L.sort()
  return L[0] + L[1] > L[2]

def getFs(lengths):
  # Returns f_min and f_max
  a,b,c,d,e,f = lengths
  t1 = ( pow(e*e+b*b-c*c-d*d,2) )/(4*a*a)
  t2 = math.sqrt( d*d - pow((e*e-a*a-d*d)/(-2*a),2) )
  t3 = math.sqrt( b*b - pow((c*c-a*a-b*b)/(-2*a),2) )
  fmin = math.sqrt( t1+pow(t2-t3,2) )
  fmax = math.sqrt( t1+pow(t2+t3,2) )
  return fmin,fmax

def isTetrahedron(lengths):
  # Given a particular sequence of lengths [a,b,c,d,e,f], returns true if a 
  # tetrahedron can be constructed with triangles abc, ade, bdf, and cef
  a,b,c,d,e,f = lengths 
  if isTriangle([a,b,c]) and isTriangle([a,d,e]):
      f_min, f_max = getFs([a,b,c,d,e,f]) 
      if f > f_min and f < f_max:
        return True 
  return False 


def get30configurations(lengths):
  # Returns 30 configurations of lengths that would construct 30 unique 
  # tetrahedron when passed to isOrderedTetrahedron(configuration) 
  a,b,c,d,e,f = lengths 
  return [  [a, b, c, d, e, f],
            [a, b, c, d, f, e],
            [a, b, c, e, d, f],
            [a, b, c, e, f, d],
            [a, b, c, f, d, e],
            [a, b, c, f, e, d],
            [a, b, d, c, e, f],
            [a, b, d, c, f, e],
            [a, b, d, e, c, f],
            [a, b, d, e, f, c],
            [a, b, d, f, c, e],
            [a, b, d, f, e, c],
            [a, b, e, c, d, f],
            [a, b, e, c, f, d],
            [a, b, e, d, c, f],
            [a, b, e, d, f, c],
            [a, b, e, f, c, d],
            [a, b, e, f, d, c],
            [a, b, f, c, d, e],
            [a, b, f, c, e, d],
            [a, b, f, d, c, e],
            [a, b, f, d, e, c],
            [a, b, f, e, c, d],
            [a, b, f, e, d, c],
            [a, c, d, e, f, b],
            [a, c, d, f, e, b],
            [a, c, e, d, f, b],
            [a, c, e, f, d, b],
            [a, c, f, d, e, b],
            [a, c, f, e, d, b]   ]  


def get7configurations(lengths):    
  # Return the 7 primary configurations
  """
  The 7 primary configurations give faces of triangles
    abc-ade-bdf-cef
    abc-adf-bde-cef   # Only adf
    abc-ade-bef-cdf
    abc-aef-bde-cdf
    abd-ace-bef-cdf   # Only ace
    abd-aef-bec-cdf   # Only bec
    acd-aef-bce-bdf   # Only acd and only bce
  """
  a,b,c,d,e,f = lengths 
  return [  [a, b, c, d, e, f], 
            [a, b, c, d, f, e],
            [a, b, c, e, d, f],
            [a, b, c, e, f, d],
            #[a, b, c, f, d, e],
            #[a, b, c, f, e, d],
            #[a, b, d, c, e, f],
            #[a, b, d, c, f, e],
            [a, b, d, e, c, f],
            [a, b, d, e, f, c],
            #[a, b, d, f, c, e],
            #[a, b, d, f, e, c],
            #[a, b, e, c, d, f],
            #[a, b, e, c, f, d],
            #[a, b, e, d, c, f],
            #[a, b, e, d, f, c],
            #[a, b, e, f, c, d],
            #[a, b, e, f, d, c],
            #[a, b, f, c, d, e],
            #[a, b, f, c, e, d],
            #[a, b, f, d, c, e],
            #[a, b, f, d, e, c],
            #[a, b, f, e, c, d],
            #[a, b, f, e, d, c],
            [a, c, d, e, f, b] ]
            #[a, c, d, f, e, b],
            #[a, c, e, d, f, b],
            #[a, c, e, f, d, b],
            #[a, c, f, d, e, b],
            #[a, c, f, e, d, b]   ]             

          
def get23configurations(lengths):
  # Return the 23 "redundant" configurations
  # [  49,    1, 4940, 4707,    0,    0,    0,    0,  161,  146,    0,
  #     0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
  #     0,    0, 2228,    0,    0,    0,    0,    0]
  a,b,c,d,e,f = lengths 
  return [  #[a, b, c, d, e, f], 
            #[a, b, c, d, f, e],
            #[a, b, c, e, d, f],
            #[a, b, c, e, f, d],
            [a, b, c, f, d, e],
            [a, b, c, f, e, d],
            [a, b, d, c, e, f],
            [a, b, d, c, f, e],
            #[a, b, d, e, c, f],
            #[a, b, d, e, f, c],
            [a, b, d, f, c, e],
            [a, b, d, f, e, c],
            [a, b, e, c, d, f],
            [a, b, e, c, f, d],
            [a, b, e, d, c, f],
            [a, b, e, d, f, c],
            [a, b, e, f, c, d],
            [a, b, e, f, d, c],
            [a, b, f, c, d, e],
            [a, b, f, c, e, d],
            [a, b, f, d, c, e],
            [a, b, f, d, e, c],
            [a, b, f, e, c, d],
            [a, b, f, e, d, c],
            #[a, c, d, e, f, b],
            [a, c, d, f, e, b],
            [a, c, e, d, f, b],
            [a, c, e, f, d, b],
            [a, c, f, d, e, b],
            [a, c, f, e, d, b]   ]
