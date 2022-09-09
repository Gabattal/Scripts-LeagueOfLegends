# Auto-Champ-Select : Draft / Ranked

# The concept
By using OCR (Optical Character Recognition), the script is able to :
* Accept your match
* Prepick the champion you want
* Ban the champion you want
* Pick the champion you want
* Alert you when your game started

The script pays attention to your allies' picks and will not ban their champion

# How do you use it ?

## Step 1 :
* You need to install **[Python](https://www.python.org/)** on your computer
## Step 2 :
* You need to install the library **[Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)** as well.
* Once this is done you should find the folder in a path that looks like  : <br/> 
```<C:\Users\<Username>\AppData\Local\Tesseract-OCR``` <br>
Take this folder and put it in the script. <br>
In the end you should have something like that :<br>
![image](https://user-images.githubusercontent.com/26858750/188023950-a5b231b5-c53a-4728-b9ff-0f0b60c1fb7f.png) <br>
## Step 3 :
* You modify the txt files to fill the data you want (picks, bans and the music that will be launched once the game start) <br>
PS : Order in the files is important, for example in this case :
![image](https://user-images.githubusercontent.com/26858750/188025339-2d1f0245-c3f1-4275-8165-46b53c66dbe4.png) <br>
If Yone and Jax are banned, it will pick Aatrox.
* You execute the launch.bat 
## Step 4 :
* You pick your roles, and you start searching for a game.
* You take a nap, you call your grandmother to check up on her, you kill these f*cking mosquitoes around you
* You play :)
# Concerning the runes
Depending on the pick you may need different runes, in my case I am using the [Porofessor App](https://porofessor.gg/) 
which automatically import the right runes for your champion.
# Problems you can encounter
* It works only if you have the game in English and you didn't change the size of the lobby's window.
* If you can't execute the installation of the Tesseract-OCR, just rename the file and remove the .dll
* Make sure that you have the autoplay activated on YouTube / your browser otherwise the music won't start.
