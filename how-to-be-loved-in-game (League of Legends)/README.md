# How to be loved in game (League of Legends)

## The concept

By using the live client I'm able to detect when I kill or die in game.

![image](https://user-images.githubusercontent.com/26858750/187098626-f514492e-e675-459d-9a0b-5bc582e8bdd5.png)

Depending on if I die or if I kill someone, the script will write a sentence for me. Here is an exemple when I die :

![image](https://user-images.githubusercontent.com/26858750/187040026-dbe07060-dd25-42c5-a32a-92dd63dbdbde.png)

## How do you use it ?

You just have to install the packages and put your pseudo here


```python
 try:
        response_API = requests.get('https://127.0.0.1:2999/liveclientdata/playerscores?summonerName=YOUR_PSEUDO_HERE',
                                     verify=False)

