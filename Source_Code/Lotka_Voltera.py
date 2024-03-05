from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# # Define the Logistic system
def lv(state, t, alpha, beta, gamma,delta):
     x, y = state
     dxdt = alpha*x - beta*y*x
     dydt = -gamma*y + delta*x*y
     return [dxdt, dydt]



# Initial conditions and parameters
state0 = [1.0, 1.0]  # initial state [x0, y0, z0]
t = np.linspace(0, 50, 100)  # time points
alpha = 10.0
beta = 28.0
gamma = 8.0 / 3.0
delta = 20

# Solve the system
solution = odeint(lv, state0, t, args=(alpha, beta, gamma,delta))


#----------------------------------

# Plot the solution
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(t,solution[:, 0], solution[:, 1])
# ax.set_xlabel('t')
# ax.set_ylabel('X')
# ax.set_zlabel('Y')
# ax.set_title('Lotka-Voltera')

#----------------------------------

fig,ax = plt.subplots(2,2,figsize=(10,10))
ax[0,0].plot(t,solution[:,0])
ax[0,0].set_xlabel('t')
ax[0,0].set_ylabel('x')
ax[0,0].set_title('population')



ax[0,1].plot(t,solution[:,1])
ax[0,1].set_xlabel('t')
ax[0,1].set_ylabel('y')
ax[0,1].set_title('resources')



ax[1,0].plot(solution[:,0],solution[:,1])
ax[1,0].set_xlabel('x')
ax[1,0].set_ylabel('y')
ax[1,0].set_title('state space')

a = np.arange(-30,30,1)
X,Y = np.meshgrid(a,a)
VX = alpha* - beta*Y*X
VY = -gamma*Y + delta*X*Y
Norm = np.sqrt(VX**2+VY**2)
st = ax[1,1].streamplot(X,Y,VX,VY,color=Norm,cmap=plt.cm.inferno,arrowstyle='->',arrowsize=4)
ax[1,1].set_xlabel('x')
ax[1,1].set_ylabel('y')
ax[1,1].set_title('state space')
ax[1,1].grid()




plt.show()



#----------------------------------

#Bifurcation



