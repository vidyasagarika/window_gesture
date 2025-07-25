import os
import time
import numpy as np
import user_configs
import pydirectinput as pyd
from pynput.mouse import Button
from pynput.mouse import Controller as mouseController

actions = user_configs.gesture_binds.actions
program_paths = user_configs.paths.program_paths

mouse = mouseController()

class perform_task:
    def __init__(self, id, all_fingers_open, landmarks, img_size):
        self.id = id
        self.landmarks = landmarks
        self.img_size = img_size
        self.all_fingers_open = all_fingers_open
        self.clipboard_content = ''
        self.play_pause_vid = 0
        self.forward_vid = 0
        self.rewind_vid = 0
        self.activate_subtitles = 0
        self.copy = 0
        self.paste = 0
        self.screenshot = 0
        self.full_screen = 0
        self.click = 0

    def run_actions(self):
        action = actions[self.id]
        # print(action)
                
        if action.split(sep='_')[0] == 'open':
            program = action.split(sep='_')[1]
            os.startfile(program_paths[program])
            time.sleep(0.15)
     
        elif action == 'cursor':
            x, y = self.landmarks[8][1]*1.2, self.landmarks[8][2]*2.25

            mouse.position = (x,y)
            
        elif action == 'click':
            if self.click == 0:
                mouse.click(Button.left, 2)
                time.sleep(0.15)
                self.click += 1

        elif action == 'play_pause_vid':
            if self.play_pause_vid == 0:
                print(action)
                pyd.keyDown('space')
                time.sleep(0.15)
                pyd.keyUp('space')
                self.play_pause_vid += 1
        
        elif action == 'forward_vid':
            if self.forward_vid == 0:
                print(action)
                pyd.keyDown('right')
                time.sleep(0.15)
                pyd.keyUp('right')
                self.forward_vid += 1
        
        elif action == 'rewind_vid':
            if self.rewind_vid == 0:
                print(action)
                pyd.keyDown('left')
                time.sleep(0.15)
                pyd.keyUp('left')
                self.rewind_vid += 1

        elif action == 'activate_subtitles':
            if self.activate_subtitles == 0:
                print(action)
                pyd.keyDown('c')
                time.sleep(0.15)
                pyd.keyUp('c')
                self.activate_subtitles += 1
        
        elif action == 'full_screen':
            if self.full_screen == 0:
                print(action)
                pyd.keyDown('f')
                time.sleep(0.15)
                pyd.keyUp('f')
                self.full_screen += 1

        elif action == 'copy':
            if self.copy == 0:
                print(action)
                pyd.keyDown('ctrl')
                pyd.keyDown('c')
                time.sleep(0.15)
                pyd.keyUp('c')
                pyd.keyUp('ctrl')
                self.copy += 1    
        
        elif action == 'paste':
            if self.paste == 0:
                print(action)
                pyd.keyDown('ctrl')
                pyd.keyDown('v')
                time.sleep(0.15)
                pyd.keyUp('v')
                pyd.keyUp('ctrl')
                self.paste += 1  

        elif action == 'screenshot':
            if self.screenshot == 0:
                print(action)
                pyd.keyDown('alt')
                pyd.keyDown('prntscrn')
                pyd.keyUp('prntscrn')
                pyd.keyUp('alt')
                time.sleep(0.15)
                self.screenshot += 1                
