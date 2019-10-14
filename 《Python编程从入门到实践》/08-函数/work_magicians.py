#coding = utf-8

def show_magicians(magicians):
    for magician in magicians:
        print("Hello, " + magician + ".")

def make_great(magicians):
    mag = []
    for magician in magicians:
        magician = "theGreat " + magician.title()
        mag.append(magician)
    return mag
    



magicians = ['eric', 'lycy', 'lily', 'nowa']

#传入列表的副本，不会改变原来的值
mag = make_great(magicians[:])
print("\nThe New :")
show_magicians(mag)
print("\nThe Old :")
show_magicians(magicians)
