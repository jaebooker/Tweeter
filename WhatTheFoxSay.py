fox_word = ""
#Image below thanks to some guy named Todd Vargo... so thanks, Todd
fox = ["   /\   /\  /","\
  //\\_//\\  /","\
  \_     _/    /   /","\
   / * * \    /^^^]","\
   \_\O/_/    [   ]","\
    /   \_    [   /","\
    \     \_  /  /","\
     [ [ /  \/ _/","\
    _[ [ \  /_/"]
def what_the_fox_say(fword):
    fox_word = fword
    new_string = ""
    if len(fox_word) < 65:
        print("___________________________________________________________________")
        for i in range(0,65-len(fox_word)):
            new_string += " "
        print("| " + fox_word + new_string + "|")
        print("|__________________________________________________________________|")
    elif len(fox_word) >= 65:
        print("_______________________________________________________________________________________________________")
        new_foxy = fox_word.split()
        fox_index = 0
        while fox_index < len(new_foxy)-1:
            fox_number = 0
            fox_string = ""
            while fox_number < 90 and fox_index < len(new_foxy)-1:
                if len(new_foxy[fox_index]) < 40:
                    fox_string += " "
                    fox_string += new_foxy[fox_index]
                    fox_index += 1
                    fox_number += 1
                else:
                    fox_string += "big words"
                fox_number += len(new_foxy[fox_index])
            for n in range(0,100-len(fox_string)):
                fox_string += " "
            print("| " + fox_string + new_string + " |")
        print("_______________________________________________________________________________________________________")
    print(fox[0])
    print(fox[1])
    for i in range(2,9):
        print(fox[i])
