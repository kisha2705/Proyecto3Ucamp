

# Máquina de Galton

import random
import matplotlib.pyplot as plt

def galton_machine(num_marbles, num_levels):
    ''' Definition of the function for the galton machine '''
    conteiners = [0] * (num_levels)    # Containers are started with 0 marbles

    for marble in range(num_marbles):
        position = num_levels // 2
        for levels in range(num_levels):
                direction= random.choice([-1, 1])  # Decide if it falls to the left or to the right
                position = position + direction    # Movement of the marbles
                   
                if position < 0:
                    position = 0
                elif position >= num_levels:
                    position = num_levels - 1

        conteiners [position] += 1   #Filling the containers 

    return conteiners


def graphic_Galton(conteiners):
    ''' Definition of the function for the graphic where the results will be displayed'''
    plt.bar(range(len(conteiners)), conteiners)
    plt.xlabel('Levels')
    plt.ylabel('Number of Marbles')
    plt.title('Galton Machine')
    plt.show()

# Data for simulation
num_marbles = 3000 
num_levels = 12


results = galton_machine(num_marbles, num_levels) # Variable that stores the simulation results
graphic_Galton(results) # Variable that shows the results of the graphic
    