#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

# Importing the libaries required for this program
import socket, json

# Declare a Python dictionary data type named "person"
# to store key value pairs
person = {}

# Define the main function
def Main():
    # Initialise a variable named "thing" with Boolean value True
    thing = True
  
    # Initialise a variable named "host" with value 127.0.0.1 (localhost)
    # This is the servers IPv4 address
    host = '127.0.0.1'
  
    # Initialise a variable named "port" with value 5000
    # This is the servers port
    port = 5000
    
    # Create a socket with the socket function
    s = socket.socket()
  
    # The connect function can take arguments, the variables "host" 
    # and "port" have been passed to the connect function
    s.connect((host, port))
  
    # Print to standard output (stdout) - the CLI
    print ("You are connected to the server.")
    
    # Create an infinite while loop
    while True:
        ### ADD COMMENT HERE LATER
        data = s.recv(1024).decode('utf0')
        
        ### ADD COMMENT HERE LATER
        if data:
            ### ADD MISSING CODE LATER
            print (person)
            
            # Break out of the loop
            break
        # Print to standard output (stdout) - the CLI    
        print ("Thanks for your participation")
    input("")



# Run the Main function
if __name__ == '__main__':
    Main()
