import random
list_hungman = []
list_hungman.append("0-6:")
list_hungman.append("1-6:________")
list_hungman.append("2-6:|      |")
list_hungman.append("3-6:|      O")
list_hungman.append("4-6:|     /|\\")
list_hungman.append("5-6:|     / \\")
list_hungman.append("6-6:|")

def hungman_put(x):
    i = 0
    #print(len(list_hungman))
    while i < x:
        print(list_hungman[i])
        i += 1

#hungman_put(5)
def answer_rand():
    list_answer = ["CAT","DOG","MITTION","AUTO","OR","POTION"]
    i = random.randrange(0,6)
    #print(i)
    return list_answer[i]
word = answer_rand() 
#print(word)

def hungman(word):
    wrong = 0
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンにようこそ！")
    while wrong < len(list_hungman) - 1:
        print("\n")
        msg = "１文字を予想してね :"
        char = input(msg)
        char = char.upper()
        #print(char)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            e = wrong + 1
            hungman_put(e)
        
        print(" ".join(board))
        
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        hungman_put(7)
        print ("あなたの負け！正解は"+word + ".")
            
hungman(word)