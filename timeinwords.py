def timeInWords(h, m):
    num_words=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty"]
    if m == 0:
        return f"{num_words[h]} o' clock "
    elif m == 1:
        return f"{num_words[m]} minute past {num_words[h]}"
    elif m==15:
        return f"quarter past {num_words[h]}"
    elif m==30:
        return f"half past {num_words[h]}"
    elif m < 30 :
        return f"{num_words[m]} minutes past {num_words[h]}" 
    elif m==45:
        return f"quarter to {num_words[h+1]}"
    else:
        return f"{num_words[60-m]} minutes to {num_words[h+1]}" 