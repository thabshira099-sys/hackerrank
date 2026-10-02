def encryption(s):
    l = len(s)
    rows = math.floor(math.sqrt(l))
    columns = math.ceil(math.sqrt(l))
    if rows*columns<l:
        rows+=1
    result=[]
    for col in range(columns):
        word=""
        for row in range(rows):
            indx=row*columns+col
            if indx<l:
                word+=s[indx]
        result.append(word)
    return" ".join(result)