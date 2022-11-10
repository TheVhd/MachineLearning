
def duplicateCheck():
    text = input('Please write your strinng: ')
    out = ''
    c = 1
    for i in range(len(text)):
        if i < len(text) - 1 and text[i] == text[i + 1]:
            c += 1
        else:
            out += text[i] + str(c)
            c = 1
    print(out)


duplicateCheck()
