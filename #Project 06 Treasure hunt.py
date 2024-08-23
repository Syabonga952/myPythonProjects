#spm
print("welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

#make a variable of the direction of the user
direction = print(input('Which direction do you want to go? "Left" or "Right"?\n').lower())
if direction == "left":
    swim = print(input('You\'ve made it to the beach, please type "Wait" to wait for the boat or "Swim" ti swim across!\n').lower())
    if swim == "swim":
        color = print(input('You\'ve made it to the Islind, which door do you choose? "Red","Yellow" or "Blue"?\n').lower())
        if color == "red":
            print('You\'ve enter a room full of fire, Game Over!')
        elif color == "yellow":
            print('Congradulations! You\'ve found the Treasure!')
        elif color == "blue":
            print('You\ve entered a room with full of Pirates and you\'ve been captured, Game Over!')
        else:
            print('You\'ve chosen a door that does\'nt exist, Game Over!')
    else:
        print('You\'ve been eaten by a shark, Game Over!')
else:
    print('You\'ve fell into a hole, Game Over!')