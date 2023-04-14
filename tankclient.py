

import pygame, requests

api_url = "http://localhost:8000/execute"
command = {"passphrase": "1234"}

# Count the joysticks the computer has
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    j = pygame.joystick.Joystick(0)
    j.init()
    left = 0
    right = 0
    previous_left = 0
    previous_right = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION and event.axis == 1:
                left = -int(event.value * 10) * 10     
            if event.type == pygame.JOYAXISMOTION and event.axis == 3:
                right = -int(event.value * 10) * 10
        if (previous_right != right or previous_left != left):
            command["left"] = left
            command["right"] = right
            previous_left = left
            previous_right = right
            response = requests.post(api_url, json=command)
            # print(response.json())
            # print(response.status_code)