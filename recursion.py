def countdown(i):
    print(i)
    if i < 1:
        return
    else:
        countdown(i-1)

i = 10
countdown(i)