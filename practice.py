def practice(self, win, i):
    # start of instructions
    cpt = 0
    instr = visual.TextStim(win=win, name='instr',
                            text="Dans ce mini-jeu, vous devez choisir à l’aide des flèches la direction de la "
                                 "flèche centrale.\n Puisqu’une image vaut mieux que "
                                 "mille mots, commençons par un petit entraînement ! \n Appuyez sur  ‘espace’ dès "
                                 "que vous êtes prêt(e)s.",
                            font='Arial',
                            units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                            color='white', colorSpace='rgb', opacity=1,
                            languageStyle='LTR',
                            depth=0.0)
    instr.draw()
    win.flip()
    resp = event.waitKeys(keyList=['space'])
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

        L = ["<<<<<<<<<", ">>>><>>>>", ">>>><>>>>", ">>>>>>>>"]
        rnd = rand(0, 4)
        targ = visual.ImageStim(
            win=win, name='targ', units='height',
            text='L[rnd]', mask=None,
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