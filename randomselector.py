import random
def randomize(list_of_names):
    final = {}
    random.shuffle(list_of_names)
    for name in list_of_names:
        if list_of_names.index(name) == (len(list_of_names) - 1):
            i = 0
        else:
            i = (list_of_names.index(name) + 1)
        final[name] = list_of_names[i]
    return final

if __name__ == '__main__':
    print(randomize('alpha beta charlie delta enigma foxtrot gamma'.split()))
