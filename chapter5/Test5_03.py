def score_out(x):
    score_dic = {6: "D",
                 7: "C",
                 8: "B",
                 9: "A",
                 }
    grade = x/10
    if grade in score_dic:
        print score_dic[grade]
    else:
        print "%d is F" %x
