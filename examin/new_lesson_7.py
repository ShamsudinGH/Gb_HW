def press(lis: list = None):
    fir = []
    sec = []
    for x1, y1 in lis:
        fir.append(x1)
        sec.append(y1)
    correct = True
    for i in range(len(lis)):
       for j in range(i + 1, len(lis)):
           if fir[i] == fir[j] or sec[i] == sec[j] or abs(fir[i] - fir[j]) == abs(sec[i] - sec[j]):
                correct = False
    return correct




