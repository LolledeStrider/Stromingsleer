import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def circle(z0, R, theta = None, theta_min = 0, theta_max = 2*np.pi, N = 1000):
    if type(theta) == type(None):
        theta = np.linspace(theta_min, theta_max, num = N)
    z = z0 + R * np.exp(1j * theta)
    return z

def joukowski_transform(z, b):
    return z + b**2 / z

def potential_function(z, gamma, u = 1):
    return u * z + u/z - 1j * gamma / (2*np.pi) * np.log(z)

def stream_function(potential):
    return potential.imag

def calculate_grid(z0 = -0.1 + 0.22j, R = 1.12, r_min = 1.12, r_max = 10, theta_min = 0, theta_max = 2*np.pi, N_r = 1000, N_theta = 1000):
    r = np.linspace(r_min, r_max, N_r)
    theta = np.linspace(theta_min, theta_max, N_theta)
    rm, thetam = np.meshgrid(r, theta)
    zm = circle(z0, rm, thetam)
    return zm

def plot_objects(C, Z, R):
    fig, ax = plt.subplots(1, 2, sharey = True, figsize = (12, 6))
    
    ax[0].set_title('Circle with R = {:1.2f}'.format(R))
    ax[1].set_title('Joukowski transformed circle')
    
    ax[0].plot(C.real, C.imag, color = 'k', lw = 3)
    ax[1].plot(Z.real, Z.imag, color = 'k', lw = 3)
    
    ax[0].set_ylim([-3, 3])
    ax[1].set_ylim([-3, 3])
    
    ax[0].set_xlim([-3, 3])
    ax[1].set_xlim([-3, 3])
    
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    ax[0].set_xlabel('x = Re(z)')
    ax[1].set_xlabel('x = Re(z)')
    
    ax[0].set_ylabel('y = Im(z)')
    
    fig.tight_layout()
    return fig, ax

def plot_stream_function(C, cm, F1, F2, g1, g2, N_levels = 30):
    fig, ax = plt.subplots(1, 2, figsize = (12, 6), sharey = True)
    
    # norm = colors.SymLogNorm(linthresh = 0.03, linscale = 0.03, base = 10)
    norm = None 
    cmap = 'seismic'
    
    ax[0].set_title(r'$\psi(z)$ for $\Gamma = ${}'.format(g1))
    ax[1].set_title(r'$\psi(z)$ for $\Gamma = ${}'.format(g2))
    
    ax[0].plot(C.real, C.imag, color = 'k')
    ax[1].plot(C.real, C.imag, color = 'k')
    
    im1 = ax[0].contourf(cm.real, cm.imag, F1.imag, origin = 'lower', norm = norm, cmap = cmap, levels = N_levels)
    im2 = ax[1].contourf(cm.real, cm.imag, F2.imag, origin = 'lower', norm = norm, cmap = cmap, levels = N_levels)
    
    ax[0].set_xlim([-5, 5])
    ax[0].set_ylim([-5, 5])
    
    ax[1].set_xlim([-5, 5])
    ax[1].set_ylim([-5, 5])
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    
    ax[0].set_xlabel('x = Re(z)')
    ax[1].set_xlabel('x = Re(z)')
    
    ax[0].set_ylabel('y = Im(z)')
    
    plt.tight_layout()
    fig.subplots_adjust(right = 0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    
    fig.colorbar(im2, cax = cbar_ax, extend ='max')
   
    return fig, ax

#%%
plt.rcParams.update({'font.size': 16})

C = circle(-0.1 + 0.22j, 1.12)
Z = joukowski_transform(C, 1)


cm = calculate_grid()
zm = joukowski_transform(cm, 1)

g1, g2 = 0, -3

F1 = potential_function(cm, g1)
F2 = potential_function(cm, g2)

plot_objects(C, Z, 1.12)
plot_stream_function(C, cm, F1, F2, g1, g2)
plot_stream_function(Z, zm, F1, F2, g1, g2)
