from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


alpha = 10.0

# # Define the Lorenz system
def lv(x, t):
    return alpha*x*(1-x)


# Initial conditions and parameters
state0 = 1.0  # initial state [x0, y0, z0]
t = np.linspace(0, 50, 100)  # time points

# Solve the system
solution = odeint(lv, state0, t)


#----------------------------------

# Plot the solution
sss = alpha*solution*(1-solution)
ss = np.ndarray.flatten(sss)
s = np.ndarray.flatten(solution)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(t,s,ss)
ax.set_xlabel('t')
ax.set_ylabel('X')
ax.set_zlabel('VX')
ax.set_title('3d phase space')

#----------------------------------

# fig,ax = plt.subplots(2,2,figsize=(10,10))
# ax[0,0].plot(t,solution)
# ax[0,0].set_xlabel('t')
# ax[0,0].set_ylabel('x')
# ax[0,0].set_title('population')



# ax[0,1].plot(t,alpha*solution*(1-solution))
# ax[0,1].set_xlabel('t')
# ax[0,1].set_ylabel('vx')
# ax[0,1].set_title('evolution rule')



# ax[1,0].plot(solution,alpha*solution*(1-solution))
# ax[1,0].set_xlabel('x')
# ax[1,0].set_ylabel('vx')
# ax[1,0].set_title('phase space')




plt.show()



#----------------------------------

#Bifurcation



