# Si vous souhaitez créer une nouvelle fenêtre qui apparait à l'écran,
# ajoutez cette fonction avec les autres qui y ressemblent :
# instr = visual.TextStim(win=win, name='instr', text='Dans ce mini-jeu, appuyez sur "a" si la flèche centrale est en direction de la gauche, \n et sur "p" si elle l\'est vers la droite.',
#                                   font='Arial',
#                                   units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
#                                   color='white', colorSpace='rgb', opacity=1,
#                                   languageStyle='LTR',
#                                   depth=0.0)
# The, you will need to add, where you want the stimulus to appear
#         instr.draw()
# to draw the stimulus in its relevant window ;
# Then
#         win.flip()
# to show the relevant window in question


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

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    # Store info about the experiment session
    expName = 'Flanker'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001', 'date': data.getDateStr(), 'expName': expName}
dlg = gui.DlgFromDict(expInfo, title='Flanker', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = expInfo['participant'] + '_' + expInfo['date']
dataFile = open('Flankercsv/' + fileName + '.csv', 'w')  # a simple text file with 'comma-separated-values'
dataFile.write('no_trial, id_candidate, id_first_im, id_second_im, good_ans, ans_candidate, keyboard_pressed, '
               'correct, task, practice, reaction_time, time_stamp\n')

filename = _thisDir + os.sep + u'Flankerlog/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# faire en sorte qu'on puisse changer facilement ?
# importer et preparer tout
# fonctions
# definir toutes les foncitons d'abord
# class
# practice : dans le practice : etre indulgent, si "faux" dire "attention, il faut faire ceci..." si vrai, "bravo !"
# voulez-vous vous entraîner une autre fois ? (oui/non)
# run
# à la fin, faire runavec le temps de depart etc.


class Flanker:
    # create init w/ users data
    def __init__(self, start):
        self.start = start
        self.keys = ['a', 'p']
        # self.list_cmaps = list()

    def run(self):
        L = ["<<<<<<<<<", ">>>><>>>>", ">>>><>>>>", ">>>>>>>>"]
        win = visual.Window(
            size=[1920, 1080], fullscr=False, units="pix", screen=0, allowStencil=False,    # if needed, change the size in correspondance with your monitor
            monitor='testMonitor', color='black', colorSpace='rgb')
        win.winHandle.set_fullscreen(True)
        win.flip()
        win.mouseVisible = False
        bienvenue = visual.TextStim(win=win, name='bienvenue',
                                  text="Bienvenue",
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        instr = visual.TextStim(win=win, name='instr',
                                text='Dans ce mini-jeu, appuyez sur "a" si la flèche centrale est en direction de la gauche, \n et sur "p" si elle l\'est vers la droite.',
                                font='Arial',
                                units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        exemple = visual.TextStim(win=win, name='exemple',
                                text='Commençons par un exemple',
                                font='Arial',
                                units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        attention = visual.TextStim(win=win, name='attention',
                              text="S'il-vous-plaît, veillez à n'appuyer qu'une seule fois sur les boutons \n pour ne pas fausser les résultats",
                              font='Arial',
                              units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                              color='white', colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=0.0)
        attention2 = visual.TextStim(win=win, name='attention2',
                                    text="S'il-vous-plaît, n'appuyez que lorsqu'on vous le demande \ ou lors du mini-jeu",
                                    font='Arial',
                                    units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                    color='white', colorSpace='rgb', opacity=1,
                                    languageStyle='LTR',
                                    depth=0.0)
        doigts = visual.TextStim(win=win, name='doigts',
                                  text='Placez vos doigts sur les touches "a" et "p" s\'il-vous-plaît',
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        prêt = visual.TextStim(win=win, name='prêt',
                                 text='Appuyez sur "a" ou "p" lorsque vous vous sentez prêt(e)',
                                 font='Arial',
                                 units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                 color='white', colorSpace='rgb', opacity=1,
                                 languageStyle='LTR',
                                 depth=0.0)
        bonne_chance = visual.TextStim(win=win, name='bonne_chance',
                               text='Bonne chance :)',
                               font='Arial',
                               units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                               color='white', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0)
        croix = visual.TextStim(win=win, name='croix',
                                         text="+",
                                         font='Arial',
                                         units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                         color='white', colorSpace='rgb', opacity=1,
                                         languageStyle='LTR',
                                         depth=0.0)
        silence = visual.TextStim(win=win, name='silence',
                               text="",
                               font='Arial',
                               units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                               color='white', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0)
        arrows = visual.TextStim(win=win, name='arrows',
                                text=L[rnd],
                                font='Arial',
                                units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        congrats = visual.TextStim(win=win, name='congrats',
                                text="Bravo ! \n Vous avez" + str(score) + "/" +str(i),
                                font='Arial',
                                units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        missed = visual.TextStim(win=win, name='missed',
                                   text="Dommage... \n Vous avez" + str(score) + "/" + str(i),
                                   font='Arial',
                                   units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)
        results = visual.TextStim(win=win, name='results',
                                 text="Vous avez obtenu" + str(score) + "/3",
                                 font='Arial',
                                 units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                 color='white', colorSpace='rgb', opacity=1,
                                 languageStyle='LTR',
                                 depth=0.0)
        pret_V2 = visual.TextStim(win=win, name='pret_V2',
                                   text='Appuyez sur entrée si vous voulez recommencer le turoriel, \n et sur "a" ou "p" pour commencer le mini-jeu',
                                   font='Arial',
                                   units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)
        pressure = visual.TextStim(win=win, name='pressure',
                                  text="Le mini-jeu va maintenant commencer, \n c'est comme tout à l'heure \n  alors pas de pression",
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        end = visual.TextStim(win=win, name='end',
                                  text='Le mini-jeu est désormais terminé',
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        good_day = visual.TextStim(win=win, name='goo day',
                                  text="Merci, et bonne journée :)",
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        bonjour = visual.TextStim(win=win, name='bonjour',
                                text="Bonne chance !",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        bonjour.draw()
        win.flip()
        core.wait(2)
        instr = visual.TextStim(win=win, name='instr', text='Dans ce mini-jeu, appuyez sur "a" si la flèche centrale est en direction de la gauche, \n et sur "p" si elle l\'est vers la droite.',
                                  font='Arial',
                                  units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)
        instr.draw()
        win.flip()
        core.wait(5)
        commencer = visual.TextStim(win=win, name='commencer',
                                text="Puisqu’une image vaut mieux que "
                                     "mille mots, commençons par un petit entraînement ! ",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        commencer.draw()
        win.flip()
        core.wait(3)
        pret = visual.TextStim(win=win, name='pret',
                                 text="Appuyez sur 'a' ou 'p' "
                                      "dès que vous êtes prêt(e).",
                                 font='Arial',
                                 units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                 color='white', colorSpace='rgb', opacity=1,
                                 languageStyle='LTR',
                                 depth=0.0)
        pret.draw()
        win.flip()

        if event.waitKeys(keyList=['a', 'p']):
            for i in range(5):
                compt=0
                rnd = randint(0, 3)
                if (rnd == 0) or (rnd == 1):
                    good_ans = "a"
                else:
                    good_ans = "p"
                if ((rnd == 0) or (rnd == 4)) :
                    condition = "Congruent"
                else :
                    condition = "Incongruent"
                fixation_cross = visual.TextStim(win=win, name='fix_cr',
                                                 text="+",
                                                 font='Arial',
                                                 units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                                 color='white', colorSpace='rgb', opacity=1,
                                                 languageStyle='LTR',
                                                 depth=0.0)
                fixation_cross.draw()
                win.flip()
                core.wait(5)
                wait = visual.TextStim(win=win, name='wait',
                                                 text="",
                                                 font='Arial',
                                                 units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                                 color='white', colorSpace='rgb', opacity=1,
                                                 languageStyle='LTR',
                                                 depth=0.0)
                wait.draw()
                win.flip()
                rnd_time = randint(8,14)
                core.wait(rnd_time)
                fixation_cross = visual.TextStim(win=win, name='fix_cr',    #potentiellement créer tous les fix_cross etc et juste faire appel à eux
                                                 text="+",
                                                 font='Arial',
                                                 units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                                 color='white', colorSpace='rgb', opacity=1,
                                                 languageStyle='LTR',
                                                 depth=0.0)
                fixation_cross.draw()
                win.flip()
                core.wait(5)
                chain = visual.TextStim(win=win, name='chain',
                                         text=L[rnd],
                                         font='Arial',
                                         units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                         color='white', colorSpace='rgb', opacity=1,
                                         languageStyle='LTR',
                                         depth=0.0)
                chain.draw()
                win.flip()
                if event.waitKeys(keyList=['a', 'p']):
                    resp = self.keys[i+1]                       # attention au cas ou la personne refait l'entrainement, metre un compteur pour le nbr d'entrainements
                    if resp == good_ans:
                        compt = compt+1
                        good_answer = True
                    if resp != good_ans:
                        good_answer = False
                    else:
                        core.wait(2)
                    dataFile.write(str(i) + ',' + expInfo['participant'] + ',' + str(condition) + str(good_answer) + ','
                                    + str(resp) + ',' + str(good_ans) + ',' +
                                   str(task) + ',' + 'no' + ',' + str(round(rt, 2)) + ',' + str(round(time.time() - start, 2))
                                   + '\n')
                i = i + 1
                res = visual.TextStim(win=win, name='res',
                                                    text="Merci ! \n Vous avez obtenu un score de " + str(compt) + "/5",
                                                    font='Arial',
                                                    units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                                    color='white', colorSpace='rgb', opacity=1,
                                                    languageStyle='LTR',
                                                    depth=0.0)
                res.draw()
                win.flip()


    def practice(self, win, i):
        # start of instructions
        cpt = 0
        instr = visual.TextStim(win=win, name='instr',
                                text="Dans ce mini-jeu, vous devez choisir à l’aide des flèches le côté où le schéma "
                                     "affiché est différent du premier schéma.\n Puisqu’une image vaut mieux que "
                                     "mille mots, commençons par un petit entraînement ! \n Appuyez sur  ‘espace’ dès "
                                     "que vous êtes prêts.",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        resp = event.getKeys(keyList=['space'])
        instr = visual.TextStim(win=win, name='instr',
                                text="Bienvenue dans l'entraînement !",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()

        for j in range(3):
            name_list_prac = []
            core.wait(2)
            bgmain = visual.ImageStim(
                win=win, name='bgMain', units='height',
                image='practice/pract_cmap_' + str(j) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))
            bgmain.draw(win)
            win.flip()
            core.wait(0.7)
            win.flip()
            fixation_cross = visual.TextStim(win=win, name='fix_cr',
                                             text="+",
                                             font='Arial',
                                             units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                             color='white', colorSpace='rgb', opacity=1,
                                             languageStyle='LTR',
                                             depth=0.0)
            fixation_cross.draw()
            win.flip()
            core.wait(2)
            win.flip()
            choice_pos = randint(0, 1)
            pics = [pic for pic in range(2)]
            c = choice(pics)
            pics.remove(c)
            name_list_prac.extend((str(i), str(c)))
            if i == 0:
                task = 'DNMS'
                if choice_pos == 0:
                    good_ans = 'a'
                else:
                    good_ans = 'p'
            elif i == 4:
                task = 'DMS'
                if choice_pos == 0:
                    good_ans = 'p'
                else:
                    good_ans = 'a'

            targ_0 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/pract_cmap_' + str(j) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            targ_1 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/test_cmap_' + str(c) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            if choice_pos == 0:
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                win.flip()
            else:
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                win.flip()

            resp, rt = self.get_response()
            if resp == good_ans:
                cpt += 1
                correct = True
                im_chosen = c
                instr = visual.TextStim(win=win, name='instr',
                                        text="Bonne réponse !",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='green', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()
            else:
                correct = False
                im_chosen = j
                instr = visual.TextStim(win=win, name='instr',
                                        text="Faux ! \n (Rappel : il faut choisir le schéma différent de celui montré "
                                             "en premier lieu ! \n Prenez votre temps si nécessaire :) ) \n",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='red', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()

            dataFile.write(
                str(j) + ',' + expInfo['participant'] + ',' + str(name_list_prac[0]) + ',' + str(name_list_prac[1]) +
                ',' + str(c) + ',' + str(im_chosen) + ',' + str(good_ans) + ',' + str(correct) + ',' + task + ', oui'
                + ',' + str(round(rt, 2)) + ',' + str(round(time.time() - start, 2)) + '\n')

        core.wait(4.0)
        if cpt == 3 or cpt == 2:
            instr = visual.TextStim(win=win, name='instr',
                                    text="Bravo, vous avez marqué " + str(cpt) + " points sur 3 ! \n Taux de réussite "
                                                                                 ": " + str(
                                        round(cpt * 100 / 3, 2)) + " % \n",
                                    font='Arial',
                                    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                    color='white', colorSpace='rgb', opacity=1,
                                    languageStyle='LTR',
                                    depth=0.0)
            instr.draw()
            win.flip()
        elif cpt == 0 or cpt == 1:
            instr = visual.TextStim(win=win, name='instr',
                                    text="Vous avez marqué " + str(
                                        cpt) + " points sur 3, mais vous avez à présent compris le principe !  \n",
                                    font='Arial',
                                    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                    color='white', colorSpace='rgb', opacity=1,
                                    languageStyle='LTR',
                                    depth=0.0)
            instr.draw()
            win.flip()
        core.wait(2)
        instr = visual.TextStim(win=win, name='instr',
                                text="Fin de l'entraînement. \n Passons à la tâche cognitive ! \n",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        core.wait(5)

    def pause(self):
        # after 15 experiments, break of 10 seconds
        core.wait(15)

    def quit_experiment(self):
        exit()

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        keys = self.keys + ['q']
        resp = event.getKeys(keyList=keys, timeStamped=rt_timer)

        if 'q' in resp[0]:
            self.quit_experiment()
        return resp[0][0], resp[0][1] * 1000  # key and rt in milliseconds


start = time.time()
exp = Flanker(start)
exp.run()
