# coding=utf-8
import time
from typing import List

import psychopy

from psychopy import core, visual, gui, data, event, logging
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random, randint, choice



class Flanker:
    # create init w/ users data
    def __init__(self, start):
        self.start = start
        self.keys = ['a', 'p']


    def run(self):
        L = ["<<<<<<<<<", ">>>><>>>>", ">>>><>>>>", ">>>>>>>>"]
        rnd = 0
        score=0
        i=0
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

        bienvenue = visual.TextStim(
            win=win,
            name='bienvenue',
            text="Bienvenue",
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
        instr = visual.TextStim(
            win=win,
            name='instr',
            text='Dans ce mini-jeu, appuyez sur "a" si la flèche centrale est en direction de la gauche, \n et sur "p" si elle l\'est vers la droite.',
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
        exemple = visual.TextStim(
            win=win,
            name='exemple',
            text='Commençons par un exemple',
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
        attention = visual.TextStim(
            win=win,
            name='attention',
            text="S'il-vous-plaît, veillez à n'appuyer qu'une seule fois sur les boutons \n pour ne pas fausser les résultats",
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
        attention2 = visual.TextStim(
            win=win,
            name='attention2',
            text="S'il-vous-plaît, n'appuyez que lorsqu'on vous le demande ou lors du mini-jeu",
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
        doigts = visual.TextStim(
            win=win,
            name='doigts',
            text='Placez vos doigts sur les touches "a" et "p" s\'il-vous-plaît',
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
        bonne_chance = visual.TextStim(
            win=win,
            name='bonne_chance',
            text='Bonne chance :)',
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
        croix = visual.TextStim(
            win=win,
            name='croix',
            text="+",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        silence = visual.TextStim(
            win=win,
            name='silence',
            text="",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        arrows = visual.TextStim(
            win=win,
            name='arrows',
            text=L[rnd],
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        congrats = visual.TextStim(
            win=win,
            name='congrats',
            text="Bravo ! \n Vous avez" + str(score) + "/" + str(i),
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        missed = visual.TextStim(
            win=win,
            name='missed',
            text="Dommage... \n Vous avez" + str(score) + "/" + str(i),
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        results = visual.TextStim(
            win=win,
            name='results',
            text="Vous avez obtenu" + str(score) + "/3",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        tutoriel_end = visual.TextStim(
            win=win,
            name='tutoriel',
            text="Le tutoriel est désormais terminé",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        pret_V2 = visual.TextStim(
            win=win,
            name='pret_V2',
            text='Appuyez sur entrée si vous voulez le recommencer, \n et sur "a" ou "p" pour commencer le mini-jeu',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        pressure = visual.TextStim(
            win=win,
            name='pressure',
            text="Le mini-jeu va maintenant commencer, \n c'est comme tout à l'heure \n  alors pas de pression",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        end = visual.TextStim(
            win=win, name='end',
            text='Le mini-jeu est désormais terminé',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        good_day = visual.TextStim(
            win=win,
            name='good day',
            text="Merci, et bonne journée :)",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.2,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)

        bienvenue.draw()
        win.flip()
        core.wait(2)
        instr.draw()
        win.flip()
        core.wait(5)
        exemple.draw()
        win.flip()
        core.wait(3)
        attention.draw()
        win.flip()
        core.wait(3)
        attention2.draw()
        win.flip()
        core.wait(3)
        doigts.draw()
        win.flip()
        core.wait(5)
        pret.draw()
        win.flip()
        event.waitKeys(keyList=['a', 'p'], maxWait=10)
        bonne_chance.draw()
        win.flip()
        core.wait(2)
        for i in range(3):
            rnd = randint(0, 3)
            if (rnd == 0) or (rnd == 1):
                good_ans = "a"
            else:
                good_ans = "p"
            if ((rnd == 0) or (rnd == 3)):
                condition = "Congruent"
            else:
                condition = "Incongruent"
            croix.draw()
            win.flip()
            core.wait(5)
            silence.draw()
            win.flip()
            rnd_time = randint(8, 14)
            core.wait(rnd_time)
            croix.draw()
            win.flip()
            core.wait(5)
            arrows.draw()
            win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                good_answer=True
                score = score + 1
            if resp != good_ans:
                good_answer=False
            else:
                good_answer=None
            dataFile.write(
                str(i)
                +
                ','
                +
                expInfo['participant']
                +
                ','
                +
                str(condition)
                +
                str(good_ans)
                +
                ','
                +
                str(resp)
                +
                ','
                +
                str(good_answer)
                +
                ','
                +
                'no'
                +
                ','
                +
                str(round(rt, 2))
                +
                ','
                +
                str(round(time.time() - start, 2))
                +
                '\n')
        results.draw()
        win.flip()
        core.wait(5)
        tutoriel_end.draw()
        win.flip()
        core.wait(3)

        # mettre pret_V2

        doigts.draw()
        win.flip()
        core.wait(5)
        pressure.draw()
        win.flip()
        core.wait(5)
        bonne_chance.draw()
        win.flip()
        core.wait(2)

        # là vrai test

        end.draw()
        win.flip()
        core.wait(2)
        good_day.draw()
        win.flip()
        core.wait()

    def quit_experiment(self):
        exit()

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        keys = self.keys + ['q']
        resp = event.waitKeys(keyList=keys, timeStamped=rt_timer, maxWait=2)

        if 'q' in resp[0]:
            self.quit_experiment()
        return resp[0][0], resp[0][1] * 1000  # key and rt in milliseconds

start = time.time()
exp = Flanker(start)
exp.run()
