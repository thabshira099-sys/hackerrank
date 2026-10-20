n = int(input())
    arr = map(int, input().split())
    second_score=sorted(list(set(arr)))
    print(second_score[-2])