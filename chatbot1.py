


def greet(bot_name,birth_year):
    print("hello! my name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))

def remind_name():
    print("please, remind me your name")
    name=input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print("Lets me guess your age")
    print("Enter remainders of dividing your name by 3,5 and 7")

    rem3=int(input())
    rem5=int(input())
    rem7=int(input())
    age=(rem3*70+rem5*21+rem7*15)%105

    print("your age is {0}; thats a good".format(age))   

def count():
    print("Now i can show you that i can count upto any no you want")
    num=int(input())
    counter=0
    while(counter<=num):
        print("{0}!".format(counter))
        counter+=1
def end():
    print("nice to meet you!!!")    

greet('Sbot','2022')
remind_name()
guess_age()
count()
end()