#%% Imports
import numpy as np, matplotlib.pyplot as plt

#%% Main functions
# A function to generate the points on a circle around a given center and with a given radius
def generate_circle(center, radius, steps):
    # We calculate the points using complex powers of e, and return a set of x- and y-coordinates
    coords = np.array([center + radius*np.exp(gamma*1j) for gamma in np.linspace(0, 2*np.pi, steps, endpoint=False)])
    return coords.real, coords.imag


# A function to apply the Joukowski transform to given coordinates. The input could be both complex coordinates or a tuple of real coordinates,
# and the output will match this type
def transform(coords, b=1):
    match coords:  # requires Python 3.10
        case x_coords, y_coords:  # if we got a set of x- and y-coordinates:
            complex_coords = x_coords + 1j*y_coords  # make these into one or multiple complex coordinates
            transformed_complex_coords = complex_coords + b**2/complex_coords  # apply the Joukowski transform
            return transformed_complex_coords.real, transformed_complex_coords.imag  # return the result as x- and y-coordinates
        case complex_coords:  # if we got (one or multiple) complex coordinates:
            return complex_coords + b**2/complex_coords  # return the complex result as complex coordinates


# A function to calculate the complex potential at given coordinates
def complex_potential(coords, gamma, u=1):
    match coords:  # requires Python 3.10
        case x_coords, y_coords:  # if the input was real:
            complex_coords = x_coords + y_coords*1j  # transform into complex coordinates
            return u*complex_coords + u/complex_coords -1j*gamma/(2*np.pi)*np.log(complex_coords)  # return the complex potential
        case complex_coords:  # if the input was complex:
            return u*complex_coords + u/complex_coords -1j*gamma/(2*np.pi)*np.log(complex_coords)  # return the complex potential


# A function to calculate the streamfunction at given coordinates
def streamfunction(coords, gamma):
    return complex_potential(coords, gamma).imag  # return the imaginary part of the complex potential

#%% Exercise a
Z_0, R = -.1 + .22j, 1.12  # define the center of the circle and its radius (as given in the exercise)

coords = generate_circle(Z_0, R, 1000)  # generate the circle with the given conditions
x_coords_transformed, y_coords_transformed = transform(coords)  # apply the Joukowski transform

# Plot the results
plt.plot(x_coords_transformed, y_coords_transformed)
plt.axis('equal')
plt.show()

#%% Exercise b
# A function to display the streamfunction as a contourplot on a given grid for a certain gamma
def display_streamfunction(gridpoints, gamma):
    values = streamfunction(gridpoints, gamma)  # calculate the streamfunction along the grid
    
    # Plot the results
    plt.contourf(gridpoints[0], gridpoints[1], values)
    plt.axis('equal')
    plt.colorbar()
    plt.title(fr"The streamfunction for $\gamma=${gamma}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# Define the linear spaces for r and gamma and make it into a meshgrid
r, gam = np.meshgrid(np.linspace(1.12, 5, 1000), np.linspace(0, 2*np.pi, 10000, endpoint=False))

X, Y = r*np.cos(gam) - .1, r*np.sin(gam) + .22  # transform the meshdrid into the X-Y plane

display_streamfunction((X, Y), 0)  # display the streamfunction for gamma = 0
display_streamfunction((X, Y), -3)  # display the streamfunction for gamma = -3

#%% Exercise c
def display_transformed_streamfunction(gridpoints, gamma):
    values = streamfunction(gridpoints, gamma)  # calculate the streamfunction along the grid
    
    X_transform, Y_transform = transform(gridpoints)  # apply the Joukowski transform to the grid

    # Plot the results
    plt.contourf(X_transform, Y_transform, values)
    plt.axis('equal')
    plt.colorbar()
    plt.title(fr"The streamfunction for $\gamma=${gamma}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

display_transformed_streamfunction((X, Y), 0)  # display the streamfunction for gamma = 0
display_transformed_streamfunction((X, Y), -3)  # display the streamfunction for gamma = -3
