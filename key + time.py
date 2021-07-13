import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

clock = psychopy.core.Clock()

keys = psychopy.event.waitKeys(timeStamped=clock)

print keys

win.close()


###################

if event.waitKeys(keyList=['a', 'p'], maxWait=2)[len(event.waitKeys(keyList=['a', 'p'], maxWait=2))-1] == good_ans:
    compt = compt + 1
    good_answer = True
else:
    good_answer = False
dataFile.write(str(i) + ',' + expInfo['participant'] + ',' + str(condition) + str(good_answer) + ','
                   + str(resp) + ',' + str(good_ans) + ',' +
                   str(task) + ',' + 'no' + ',' + str(round(rt, 2)) + ',' + str(round(time.time() - start, 2))
                   + '\n')
res = visual.TextStim(win=win, name='res',
                      text="Merci ! \n Vous avez obtenu un score de " + str(compt) + "/5",
                      font='Arial',
                      units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                      color='white', colorSpace='rgb', opacity=1,
                      languageStyle='LTR',
                      depth=0.0)
res.draw()
win.flip()
core.wait(5)