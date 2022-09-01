# Auto-Select (League of Legends)

# The concept

By using OCR (Optical Character Recognition), the script is able to :
* Accept your match
* Prepick the champ you want
* Ban the champ you want
* Pick the champ you want
* Alert you when your game started

The script pays attention to your allies' picks and will not banish their champion

# How do you use it ?

## Step 1 :
* You need to install **[Python](https://www.python.org/)** on your computer
## Step 2 :
* You need to install the library **[Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)** as well.
* Once this is done you should find the folder in a path that looks like  : <br/> 
```<C:\Users\<Username>\AppData\Local\Tesseract-OCR``` <br>
Take this folder and put it in the script. <br>
In the end you should have something like that :
![image](https://user-images.githubusercontent.com/26858750/188023950-a5b231b5-c53a-4728-b9ff-0f0b60c1fb7f.png)
## Step 3 :
* You modify the txt files to fill the data you want (picks, bans and the music that will be launched once the game start)
* You execute the launch.bat

# Problems you can encounter
* If you can't execute the installation of the Tesseract-OCR, just rename the file and remove the .dll
* Make sure that you have the autoplay activated on YouTube otherwise the music won't start.
