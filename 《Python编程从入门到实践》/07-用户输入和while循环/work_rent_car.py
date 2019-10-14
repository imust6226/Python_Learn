#coding = utf-8


def rent_car():
    question = input("Please tell me what car do you want to rent:\t")

    print("Let me see if I can find you a " + question.title() + " .")

def book_seat():
    question = input("Will you let me know how many people I'll have to keep: ")
    number = int(question)
    if number > 8:
        print("Sorry,I don't get an available table to service you like as many as " + str(number) + ".")

    else :
        print("I'll keep that.")


def even_or_odd():
    num = input("Give a number,I'll tell you if this can be division by ten with nothing left.")
    num = int(num)
    if num % 10 ==0:
        print("Sucessful")
    else :
        print("Failure")
#rent_car()
#book_seat()
even_or_odd()
 
