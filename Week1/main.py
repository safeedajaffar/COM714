
def second_question():
    choice= input("Who sees me rolling (cops, wardens, other)?\n")
    if choice == "cops":
        print("They see me rolling. They hating. They hoping they gonna catch me riding dirty!")
    elif choice == "wardens":
        print("My music's so loud. I'm swanging. They hoping they gonna catch me riding dirty!")
    else:
        print("Trying to catch me riding dirty!")


def first_question():
    name=input("Who broke my heart?\n")
    out="My first love, "+ name + ", broke my heart for the first time."
    print(out)
    print("And I was like baby, baby, baby oh.")


if __name__ == '__main__':
    first_question()
    second_question()