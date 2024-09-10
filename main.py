import os
import pygame
from processes import upload, main1

while True:
    pygame.mixer.init()

    up_dir = os.path.join(os.getcwd(), 'All_Music')

    x = input("Enter the name of a singer or playlist: ")
    y = os.path.join(up_dir, x) 
        
    if x == "end":
        break
    

    elif os.path.exists(y):   
        print("The playlist already exists.")
                        
    else:
        os.makedirs(y)
        print("Playlist created successfully.")
    
    
    upload()

main1()     





        
        


        
    
    
    
    
    
    



