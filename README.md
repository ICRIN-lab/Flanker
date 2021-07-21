# Flanker task

## What is the Flanker task?

In cognitive psychology, the Eriksen Flanker Task is a set of response inhibition tests used to assess the ability to suppress responses that are inappropriate in a particular context. The target is flanked by non-target stimuli which correspond either to the same directional response as the target (congruent flankers) or to the opposite response (incongruent flankers). 
In the tests, a directional response (usually left or right) is assigned to a central target stimulus.
In this Flanker task, nine arrows appear on the screan and the middle arrow points either to the left or the right, and the subject is instructed to press one of two buttons indicating the direction of the arrow in the middle. If it’s pointing to the left, the subject presses the “left” button; if it’s pointing to the right, the subject presses the “right” button. 
The middle arrow is flanked by other arrows which either point in the same direction as the middle arrow (Congruent), or point in the opposite direction from the middle arrow (Incongruent). Hence the name.

## What is the objective of the Flanker task?

The Flanker task is designed to tap into a mental process known as cognitive control.
One can imagine that the task is easier if the central arrow points in the same direction as the flanking arrow (Congruent), and more difficult if it points in the opposite direction (Incongruent). 
Subjects are typically slower and less accurate in the Incongruent condition, and faster and more accurate in the Congruent condition. 
Since the difference in reaction times is robust and reliable, it follows that in our fMRI data we should see a noticeable difference in the BOLD signal as well.
BOLD is an acronym which stands for Blood Oxygenation-Level Dependent Signal. Nearby oxygenated blood interferes less with the signal emitted by Hydrogen atoms than does deoxygenated blood.
Our goal is to estimate the magnitude of the BOLD signal to each condition, and then contrast (i.e., take the difference of) the two conditions to see whether they are significantly different from each other.

## What do I have to do before running the code?
For this experiment, one should create a folder called Flankercsv in order to store the data.
We recommend looking at the code before running it, as some changes will be needed - do not worry, the comments on the code are made in English -.
The main change is the fact that the directory of the folder has to be changed, as the folder Flankercsv will not be stored at the same location from one's computer to another.
Another common change is that the experiment is ran in French. However, it is very basic French and Google Translate should be able to help perfectly.
(We are planning to make other languages versions of this task and we will post it on our GitHub whenever that is done however, if you did it before us, do not hesitate to share it with us [on our email](mailto:contact@icrin.fr), same goes for any changes that you may have made :).)
The last main change is people wanting to either change the keyboards's keys for the user inputs, or the people wanting to use a response pad.
We also recommend checking at the size of the monitor one uses. By default, we used the size of ours, which is 1920x1080px, one should change it to better fit the screen used.

## How does the experiment work?
Once one has set everything, one just has to run the code.
Some instructions will be shown on the screen for the user to read.
In order to make sure that the patient has understood the task perfectly, a practice of three trials will start once the user clicks on "**a**" or "**p**".
Once the practice is over, the user will be shown his score, some other instructions will be shown and the real experiment will start, once the user has clicked on "**a**" or "**p**", once again.
The experiment is simple: the user has two seconds for each chain of arrows to say if the central arrow is pointing towards left, or right.
If the arrow points towards the left, the user has to press the "**a**" key on the keyboard, if it points right, he has to point the "**p**" key.
The data captured is saved as a csv, and one is free to analyse it however he pleases.

## How does the code work?
First, a window corresponding to the size of one's screen is created.
Then, we create all of the screens that we will use, for example, one simply states "*Bonne chance :)*" or "*Good luck :)*" in French.
During the task, for each trial, one of the following: "**<<<<<<<<<**", "**>>>><>>>>**", "**<<<<><<<<**" or "**>>>>>>>>>**" is chosen randomly.
Depending on which chain it is, we store the good answer (either "**a**" or "**p**") and also if the Congruence of the chain.
The chain is then shown to the user, who has two seconds to either click "**a**" or "**p**" depending on the answer that he wants to give.
Here, we store the data corresponding to this perticular trial (see below in "*What data do you retrieve from this experiment?*").
There are three practice trials and then ten non-practice trials.

## Frequently Asked Questions (FAQ)

### Why can't I run the code?
In order to run the code, one needs a compiler to execute it, but one also needs to create a Flankercsv folder and change the directory in the code so the data can be storred correctly.

### How is the data saved?
The data is storred as a CSV, so it is compatible with any spreadsheet software.

### What data do you retrieve from this experiment?
In this experiment, there are ten outputs:
1. *no_trial*: this corresponds to the number of the trial (be careful, the value starts at 0 so the third answer of the experiment will ne after "2"), 
2. *id_candidate*: this corresponds to the name that a candidate has entered at the beginning of the experiment, 
3. *visual*: this corresponds to the chain of arrows shown to the user, 
4. *condition*: this corresponds to **Congruent** if all the arrows pointed in the same direction and **Incongruent** otherwise, 
5. *ans_candidate*: this corresponds to the answer given by the user,
6. *good_ans*: this corresponds to the good answer, 
7. *correct*: this corresponds to **True** if the user was right, **False** otherwise or **None** if he did not answer, 
8. *practice*: this corresponds to **yes** if the answer was given during the tutorial and **no** othrwise, 
9. *reaction_time*: this corresponds to the time thr user took to give his answer, 
10. *time_stamp*: this corresponds to the absolute time when the user gave his answer.

One should feel free to add or remove outputs, if needed.

### Do I need a compiler to run the experiment?
Yes, one needs a compiler to run the experiment.

### Can I convert the code into an desktop app?
Of course, if one wishes to simply double-click on a desktop app in order to run the experiment, it is possible.
One simply needs to use a package such as Pyinstaller, which works for Windows, MAC and Linux.

### How should I run the experiment?
To answer this question, I will suppose that one managed to run the code correctly.
In order to run the experiment with a user who is willingly participating and sharing the results from his experiment, one should simply change the code accordingly to the experiment tha they wish to do (language, increasing/decreasing time,...) and run the code.
Then, once enough experiments have been ran, collect the data and analyse it however one wants.
If some interesting things are found, do not hesitate to contact us [on our email](mailto:contact@icrin.fr) :).

### Do you mind if I run the experiment differently?
One should feel free to change the task, there is some papers online of slightly different Flanker Tasks or one could come up with its own experiment.
One could maybe use an EEG to capture the electrical activity of the user during the task.
If you do so, feel free to send us the code and/or the results from your experiments [on our email](mailto:contact@icrin.fr) :).

### Do you recommend a response pad?
At the lab, we use the Cedrus Response Pad RB740, which works perfectly fine. But one could simply use a keyboard, it should work just as fine.

### Where are you guys located?
This task was developped and the experiments were held at the [ICRIN Lab](http://icrin.fr/), situated in the Brain Institute, at the Pitié-Salpêtrière Hospital.

### How can I contact you?
If needed, one can contact us through [this page](http://http://icrin.fr/contact.html).
