def checkSingle(string):
    check_Single = True
    lenstr = len(string) 
    for i1 in range(0,lenstr-1):
        for i2 in range(i1+1,lenstr):
            if string[i1]==string[i2]:
                check_Single = False
                continue
    return check_Single
for i in range(203,986):
    son1=str(i)
    if not checkSingle(son1):
        continue
    for j  in range(i+1,987):
        check = True
        son2=str(j)
        if not checkSingle(son2):
            check = False
            continue
        for k in son2:
            if k in son1:
                check = False
                continue
        if check:
            ress = j+i
            ress1 = str(ress)
            if len(ress1)<4:
                check = False
                continue
            if not checkSingle(ress1):
                check = False
                continue
            for m in range(0,3):
                if son1[m] in ress1 or son2[m] in ress1:
                    check = False
                    break
            if check:
                print(i,j,ress)
        
