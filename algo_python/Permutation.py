def permutation(items: str, pocket = ''):
    if len(items)==0:
        print(pocket)
    else:
        for i in range(len(items)):
            letter = items[i]
            front = items[0:i]
            back = items[i+1:]
            together = front + back
            permutation(together, letter+pocket)

    
permutation('abc')