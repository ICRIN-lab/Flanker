L = ["<<<<<<<<<", ">>>><>>>>", ">>>><>>>>", ">>>>>>>>"]
for i in range (6) :
    for j in range (6) :
        rnd = rand(0, 4)
        if (rnd == 0) or (rnd == 1):
            good_ans = "a"
        else:
            good_ans = "p"
        print(L[rnd])
        ans = input()
        if ans = good_ans :
            good_answer = True
        else :
            good_answer = False
        results = results + [good_answer]
        j+ = 1
    # change timing
    i+ = 1

#get_events