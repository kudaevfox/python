string = input("Введите строку:")
#rgbvgrb = string.count(" ")
word = []
i = 1
for i in range(string.count(" ") + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f"{i} {word[i]}")
        i += 1
    else:
        print(f" {i} {word[i][0:10]}")
        i += 1
