def plusMinus(arr):
    total = len(arr)
    positive = [i for i in arr if i > 0]
    print(len(positive)/total)
    negative = [i for i in arr if i < 0]
    print(len(negative)/total)
    zero = [i for i in arr if i ==0]
    print(len(zero)/total)
            