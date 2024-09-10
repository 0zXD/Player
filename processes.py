def intch(message):
    while True:
        try:
            x = int(input(message))
            return x
        except: 
            print("Please enter an integer.")
        

def upload():
    import os
    import shutil
    import main

    while True:
        source = input("Enter the path of the Mp3 file: ").strip()
        if source == "end":
            break
                
        a = main.y
        name = os.path.basename(source)
        dest = os.path.join(a, name)

        shutil.copy2(source, dest)
        print("File added successfully.")
        print("****************************")


def play_music(file_path):
    import pygame
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("Playing music...")
    print("****************************")

def pause_music():
    import pygame
    pygame.mixer.music.pause()
    print("Music paused.")
    print("****************************")

def unpause_music():
    import pygame
    pygame.mixer.music.unpause()
    print("Music resume.")
    print("****************************")

def stop_music():
    import pygame
    pygame.mixer.music.stop()
    print("Music stopped.")
    print("****************************")
    
def main1():

    import os
    import main
        
    a = main.y
    all_contents = os.listdir(a)
    nu_of_files = len(all_contents)
    print("****************************")
    for x in range(0, nu_of_files):
        print(f"{x+1}. {all_contents[x]}")
    print("****************************")

    b = intch(f"Choose an option from 1- {nu_of_files}: ")
    print("****************************")

    song = os.path.join(a, all_contents[b-1])

    while True: 
        command = input("Enter command (play, pause, chother, exit): ").strip().lower()
        
        if command == 'play':
            play_music(song)

        elif command == 'pause':
            pause_music()

        elif command == 'chother':
            main1()

        elif command == 'exit':
            stop_music()
            break


        else:
            print("Invalid command. Please enter 'play', 'pause', 'exit'")
    
    