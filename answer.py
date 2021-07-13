# coding=utf-8
import time
from typing import List

import psychopy

from psychopy import core, visual, gui, data, event, logging
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random, randint, choice
import matplotlib
import matplotlib.pyplot as plt
import os


class Flanker:
    # create init w/ users data
    def __init__(self, start):
        self.start = start
        self.keys = ['a', 'p']
        self.colors = 'red yellow'.split()
        # self.list_cmaps = list()

    def run(self):
        cpt = 0
        win = visual.Window(
            size=[1920, 1080],  # if needed, change the size in correspondance with your monitor
            fullscr=False,
            units="pix",
            screen=0,
            allowStencil=False,
            monitor='testMonitor',
            color='black',
            colorSpace='rgb')
        win.winHandle.set_fullscreen(True)
        win.flip()
        win.mouseVisible = False
        pret = visual.TextStim(
            win=win,
            name='prêt',
            text='Appuyez sur "a" ou "p" lorsque vous vous sentez prêt(e)',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)


        win.flip()
        pret.draw()
        win.flip()
        event.waitKeys(keyList=['a','p'], timeStamped=10)
        instr = visual.TextStim(win=win, name='instr',
                            text="test",
                            font='Arial',
                            units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                            color='white', colorSpace='rgb', opacity=1,
                            languageStyle='LTR',
                            depth=0.0)
        instr.draw()
        win.flip()

    def quit_experiment(self):
        exit()

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        keys = self.keys + ['q']
        resp = event.waitKeys(keyList=keys, timeStamped=rt_timer)

        if 'q' in resp[0]:
            self.quit_experiment()
        return resp[0][0], resp[0][1] * 1000  # key and rt in milliseconds


start = time.time()
exp = Flanker(start)
exp.run()
