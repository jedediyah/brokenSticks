import BreakSticks as bs
import matplotlib.pyplot as plt
from random import randint

# Given a stick broken into six pieces, what is the probability that we can form a tetrahedron?
# This script runs n parallel Monte Carlo simulations of breaking a stick into 6 random
# pieces.  It keeps an average of the probability that a tetrahedron is possible from those 
# pieces and plots the individual running averages with the total running average. 

N = 10_000_000     # Number of iterations 
n = 301            # Number of parallel simulations 

# Initialize plotting 
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('iterations')
plt.ylabel('% probability of tetrahedron')
plt.title('Monte Carlo estimate of tetrahedron probabilty from broken stick')
color = ['#%06X' % randint(0, 0xFFFFFF) for _ in range(n)]
plotx, ploty = [[] for _ in range(n)],[[] for _ in range(n)]
lines = [[] for _ in range(n)]
for i in range(n):
  lines[i] = ax.plot(plotx[i], ploty[i], color[i], alpha=0.22)
line_avg = ax.plot([],[],'k')
y_avg = []

# Run Monte Carlo with graphics 
tetra_count = n*[0.0]
for iteration in range(1,N+1):
  for i in range(n):
    for configuration in bs.get7configurations( sorted(bs.breakStick(6)) ):
      if bs.isTetrahedron(configuration):
        tetra_count[i] += 1
        break
  if iteration % 5_000 == 0:
    # Update plots 
    for i in range(n):
      plotx[i].append(iteration)
      ploty[i].append(100*tetra_count[i]/iteration)
      lines[i][0].set_data(plotx[i], ploty[i])
    y_avg.append( sum([ploty[i][-1] for i in range(n)])/n )
    print('Current probability: ', y_avg[-1],'%')
    plt.title('Estimate of tetrahedron probability: ' + str(y_avg[-1]))
    line_avg[0].set_data(plotx[0],y_avg)      
    ax.set(xlim=(0,iteration),ylim=(5.75,7.35))      
    fig.canvas.draw()  
    plt.pause(0.01)
    plt.savefig('sticks.pdf',dpi=150)

