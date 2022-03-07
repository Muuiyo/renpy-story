# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define X = Character("...")
define MC = Character("You", color="#a64270")
define JT = Character("Jett", color="#42a669")
define LI = Character("Leroy")
define A = Character("Aaron")

# The game starts here.

label start:

    scene bg room
    
   X "Jett brings you to the place of the chef that bakes satisfying bread"

   # This ends the game.

   return
