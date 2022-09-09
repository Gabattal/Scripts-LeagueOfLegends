# Auto-Champ-Select

As you can see there are two files here. Each contains a script that uses a different technique :

### Auto-Champ-Select-LCU

This script uses the League Client Update : it will send request to the server to execute every action, this will work
regardless of your window size or language. However, it works less well than the script using OCR in the sense that it
doesn't pay attention to allied picks and the prepick doesn't work ( I plan to fix these bugs as soon as I have the
opportunity )

### Auto-Champ-Select-OCR

This scripts uses the Optical Character Recognition : it will take screenshots at specific locations to determine what
phase you are in, then it will simulate clicks and keyboard keys to execute every action. Currently, it only works if
you have the default size of the window's client and have the game in English (I can also add the language of your
choice if
you open an issue.)

You can find a detailed readme in each file.