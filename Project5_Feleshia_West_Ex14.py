#Exercise #14: Kinetic Energy


#This program will receive the mass and velocity from the user
# and calculate the kinetic energy.
def kinetic_energy():
    m = float(input("What is the mass of the object:  "))
    v = float(input("What is the velocity of the object: "))
    KE = (1/2 * (m * v**2))
    #print KE
    print("The kinetic energy of the mass is ", format(KE, '.2f'))
#calls KE    
kinetic_energy()


    
