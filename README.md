# DazedMTLTool - A script that translates RPGMaker JSON files using ChatGPT API

![image](https://user-images.githubusercontent.com/96628874/230908699-adacb5e1-1548-4116-a0ea-a33297cdafa4.png)

Currently in development. Goal is to eventually have a tool that utilizes ChatGPT API to translate text. I've deemed a fully automatic process impossible for production of quality MTLs since games are so different. Instead, this should be used to translated large masses of text (Dialogue, Choices, Battle Text, Etc) that would require months of work. Then the translator can focus on editing, fixing, and formatting instead to release a quality MTL. It is not meant to be used as an easy 'Translate Everything' and forget about it option since this results in a poor buggy translation.

## Currently Supported:
* RPGMaker MZ, MV, ACE, TyranoBuilder
* CSV Files

## Required:
 * API Key: https://platform.openai.com/account/api-keys
 * Organization Key: https://platform.openai.com/account/org-settings
 * Python3.11+: https://www.python.org/downloads/

## Setup:
1. Navigate to the project folder and open a terminal by Shift+Right Clicking the background. Install the dependencies with `pip install -r requirements.txt`
2. Add your API key and Organization Key to a .env file. An example can be found in the repo.
3. Add a prompt.txt file using prompt.example as a template. (See ChatGPT Prompt Section)
4. Untranslated JSON files go in `/files`. Anything translated will end up in `/translated`
5. Run `start.py` script either with VSCode or by running `python .\start.py` in Terminal.

See [Guide Section](https://github.com/dazedanon/DazedMTLTool#how-i-translate-games) to get a full breakdown on the process.

## ChatGPT Prompt:

`prompt.txt` will decide what and how ChatGPT translates the text. This is where you can customize it's output. This is extremely useful for when ChatGPT gives you a translation that you don't want. You can use this to tell him what to do, give examples of how you want things translated, etc. The example included is what I use currently, but you should tailor it to the game you are trying to translate.

Note that the bigger the prompt, the more $$$ its going to cost to translate.

## Troubleshooting Errors:
In its current state, you will very likely run into errors. There hasn't been enough testing with enough games to get it in a stable state. Often ChatGPT won't know how to translate something and will timeout. Currently the timeout is pretty long so the program may hang for a while. NEVER CLOSE THE PROGRAM FORCEFULLY unless you wish to lose your translation data, which might as well be you losing money. 

If the ChatGPT times out or hits any other error, what has already been translated will always be saved as long as you let it fail on its own. The file will still be placed in /translated on success or fail. That way you don't have to worry about the program failing and you wasting money on bugs.

### Common Errors:
#### ChatGPT timing out due to not knowing how to translate something 
1. Go into ChatGPT Playground https://platform.openai.com/playground?mode=chat and enter the text it failed on. If it comes out clean, likely the prompt may just need some adjusting or the string may need to be formatted in some way.
2. Create an example for that specific text. At the bottom of prompt.txt are examples you can enter which will give the AI training data on how to translate. This pretty much works 100% of the time but the downside is it will make your prompt.txt file bigger and your translation more expensive.

#### ChatGPT randomly hangs
1. Unsure what causes this. I recommend you just let it fail on its own and give you the error message. The error handler will tell you what line of text threw the error and what error it received.

### General Debugging:
You'll need VSCode or something similar:

# How I Translate Games
The goal of this section is to get you learnt and ready to translate the game of your choice. I'll be walking you through every step of my process so that you can get an idea of what I do to get things working. This will not go over setup, go do the setup steps at the top to make sure the tool works properly before continuing.

A couple of requirements.

* [VSCode](https://code.visualstudio.com/) (It's going to be be your main tool for running the scripts. When installing make sure you enable the context menu options)
* [Python 3](https://www.python.org/downloads/)
* [API Key](https://platform.openai.com/account/api-keys)
* [PowerToys](https://f95zone.to/threads/windows-supported-ocr-tool-microsoft-powertoys.163509/) (Very useful for non-japanese speakers)
* Willingness to learn (No programming experience required)

1. First download the repository. You can do this by just downloading the zip on the main page or using Git to clone it, either works.
2. Right click on the project folder and click `Open with Code`.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/df6adca7-1d6f-44a2-aab7-dfffeab91b02)

3. Here is where the magic happens. This will be your main workspace which you can use to do everything you need to MTL a game.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/68aedaf7-c915-4531-b76b-291a5d1487ff)

A breakdown of what all the different files are, this is important.
* /files - Where you place files that need to be translated.
* /translated - Where files go after they are translated.
* /scripts - ignore (This is old stuff and will be deleted soon)
* /modules - The script files, the cogs of the machine, what creates the translation.
  * main.py - Responsible for determining what engine gets run based on user choices
  * rpgmakermvmz.py - Translation Script for the RPGMaker MV/MZ Engine.
  * rpgmakerace.py - Translation Script for the RPGMaker ACE Engine. (Requires rvpacker to unpack rvdata files)
  * csvtl.py - Translation Script for CSV Files. Requires at least 2 columns to work.
  * TXT.py - Translation Script for Other game engines. (More of a custom script I change depending on the game)
* .env.example - An example env file. This gets renamed to .env and holds your PRIVATE API and Organization key. Do not EVER upload this information.
* RPGMakerEventCodes.info - Information on the various types of event codes in RPGMaker. More on this later.
* prompt.example - Holds an example prompt ChatGPT uses to determine what to do with text you give it. Change this as you please.
* requirements.txt - Used for setup, ignore.
* start.py - Used as a starting point for running the script. This is what you run to start everything up.

4. Now that you have an idea of what each file does, lets decide on a game to translate. For this guide I'm going to stick with a game I've done before to make things easy. Bounty Hunter Kyouka.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/a9a11955-b975-4f71-a75d-804cc75cf368)

First lets analyze what type of game this is. It's made using RPGMaker MZ which is basically the same as MV. You can tell by the game.exe icon. The two main folders we care about for MTL purposes are `data` and `js`.

* data - Will have all the main text files where majority of stuff will need to be translated.
* js - Will have the scripts the game uses to run. This is how you can change certain things like the font, size of windows, etc.

Rule of thumb, **always backup the game folder**. When you mess something up its nice to be able to go back and reference the original files. It will also be helpful when something breaks to have something to fallback on.

5. So the first thing I always translate with a new game are the menus. To do this go into /data and find System.json. (Sort by name while you are at it too.) Copy this file, and place it in your project `/files` folder. Then open VSCode and look to see that its there. **I like to translate things step by step. It will make it way easier to debug when things break.**

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9cff0041-134c-4c9c-b31c-f8ce7548f2a4)

6. Now we are ready to translate System.json. But wait, before you do a tip.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9076e82d-4436-408b-b34c-ea0ac581d50c)

PRO TIP: Sometimes, you want to make sure that things are getting translated RIGHT before you invest into the translation. To do this, open up `rpgmakermvmz.py` in VSCode. There's a lot of code in here, ignore it and scroll all the way down until you find the function `def translateGPT(t, history, fullPromptFlag):`. This is what actually sends text to the API for translation.

* t - Text that is going to be translated
* history - Previously translated text OR context (Improves translation)
* fullPromptFlag - Decides whether to use prompt.txt (True) or to ignore it (False). Ignore this for now.

In order to check what is getting translated, click LEFT of the line number with the following text `return [translatedText, tokens]`

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/f00c88e4-3eb9-4ade-85dc-76d77e4e33ea)

This tells the program "Hey, when you get to this line STOP everything and show me the goods.". We are going to use this to check text after it's translated. Now we can start the translation. 

In VSCode Click Terminal > New Terminal to open up the terminal. Open up `start.py` by double clicking it. Then press `F5` and select Python file to startup the program. Then in the tool select `Translate` and `MV/MZ` to start the translation. The tool will begin translating everything inside. As soon as it hits that line it will stop like so.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/91735200-98d7-4aa9-85b6-fbe613e2dd37)

Couple of things to notice here. 
* At the top right are your debug options. Press play to have the program continue, F5 also works.
* At the bottom left is your text thats being translated. `t` is the original text and `translatedText` is your translated text. This is how I QA to make sure translation looks good before I continue.

Anyway, if you are satisfied with the results, click the breakpoint again to remove it and press F5 to continue with the translation. You can add that breakpoing anywhere in the code at anytime, its very helpful for learning what does what.

7. Now that System.json is finished translating, I like to go through it and fix any obvious issues I see. It will be in `/translated`. Lets open it up in VSCode and take a look.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/7ac3311a-575f-4398-8371-68e7321fad6e)

You can see that some things didn't translate. This happens sometimes as a safe guard when the API returns something that is clearly wrong. You can either manually fix these or adjust to prompt. I'm just going to manually fix them. Also notice `Translation:` and `Translated Text:` which we don't want. You can use CTRL+F to find how many instances of this issue we have and fix them.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/ed0e41f8-5fac-4dea-9f6c-4b0fdaf41be4)

8. After you fix everything, move System.json back to /files and add the breakpoint. This time add two like so.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/c01a65e9-260a-4861-955c-3c38e75ddf3c)

This will ensure that no matter what translation pops up the program stops first so you can check it. `return [t, response.usage.total_tokens]` essentially runs IF the API returns some garbage. Our goal for rerunning System.json is to have it finish with a cost of 0.00 so that we know everything is translated.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9cb74fa8-3781-4921-bd30-f84fc368f7e8)

As you can see that's exactly what I got when I tried running it again, which tells me there isn't anymore untranslated text in the file. This one is good to go and you can go ahead and copy it back to the /data folder in the game project. Restart the game by either closing it, or hitting F5 while it's open.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/e536db7f-8d8b-48c8-82ae-c8af62453dbc)

9. Tadah! Translated text. Baby Steps... Baby Steps... However notice that piece of text that isn't translated? That means that text is located somewhere other than System.json. We have to find it, but there are so many files... how are we supposed to find something like that? The easiest way to do this is using a Text Scanner like [PowerToys](https://f95zone.to/threads/windows-supported-ocr-tool-microsoft-powertoys.163509/).

Using this, we can simply use Windows+Shift+T to scan the text. But first, in your game folder, right click on the /data folder and click Open in VSCode. Then Click Search at the top left and now scan the text in the game. Paste that text into the search bar.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9242cbd7-3931-4f83-bb61-bf78b058c3df)

Uh oh, no results found means its not anywhere in data either. Usually that means there's only one other place it could be. Right click on the /js folder and open in VSCode. Follow the same steps.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/396265d2-6f34-40bb-a550-22a1cfe883c5)

2 results! Much better. Check them both to see which one is the culprit. Usually it's the one in plugins.js (Which holds the settings for all of the plugins in the game).

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/51b6f05e-88ea-463e-8453-9347da99ad80)

As you can see this is a custom menu option added by the plugin. Lets go ahead and translate that and see if it changes.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9ae7b27c-8c53-4e88-b5d9-64e6a7b417e0)

Yup! That did the trick. Now we can move onto the next one.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/f5bfa278-4f2b-4189-a23b-a0e914f8b49a)

10. Starting the game, there are still a couple of menu options to translate. None of these are in System.json so they must be in /js. Go ahead and manually fix those using the same method as before. Since I've already done this game, I'm going to go ahead and skip this step.

11. Lets try doing list items. This means Actors, Armors, Classes, Enemies, Items, Skills, States, Weapons. No need to think to hard for these, move them out of the /data folder and into the files folder in the project. Then simply start the translation up like you did with System.json.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/b9950e35-a5a4-4e78-b1de-6e58b1905990)

12. Once again repeat the process of checking for mistakes in /translated results, moving them back to /files, and trying to hit the goal of getting a 0 for every file. You can make whatever improvments you like to the prompts, you can find them scattered around in the different functions of the code. For example

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/9b3bfd57-0e2f-49ba-981c-a047961e8518)

Adjusting these when you get bad responses helps.
![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/16fb648e-42a1-4b3e-b37e-c04aa805a1d0)

13. Now to move onto the hard part. Map Files and the Common Events File.

* Map Files - Contain all the maps and random NPC conversation you run into. Usually has majority of common text.
* Common Event Files - Contains all the event files (H-Scenes and such).

There are two things to know when translating these types of files. In each of them, the type of text contained in each one is ususally designated by a specific RPG code. For example, dialogue uses code 401, Choices use code 102, names use code 101, etc. This is useful for translating ONLY the text we need to translate.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/1c2de0f0-5ad5-4162-86a7-505079913d1c)

Usually you can get the game 95% translated by just translating the 401 and 102 codes. So that's what we are going to focus on in this guide. Let's start small, first go into the game and scan the first text you see.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/4b8f2a46-f355-49a9-a808-c35701a4200a)

As you can see Map117.json is the first encounter for text so lets start with that. Move it on over to files.

14. First we have to enable a code for translation. They are disabled by default to avoid accidentally translating things when you aren't ready. Look at the top of `rpgmakermvmz.py` for the flags section.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/904af926-58f2-4d8b-8053-b3af1d6e4840)

Let's start with dialogue, enable the 401 by setting it to `True`. Then you can go ahead and start the translation process like before.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/4ad27ccb-52e9-424b-8a35-b176e76783a3)

Afterwards, simple shoot for that 0 and move the translated file back to game folder to test it.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/154a9565-466e-439b-8afd-0e4a29034cce)

15. Yay! It's translated! but wait, I can't see shit. We are going to have to adjust the wordwrap (and maybe the font size but more on that later).

    Wordwrap is controlle by two variables `WIDTH` and `LISTWIDTH`.

    * WIDTH - Wordwrap for dialogue and most text
    * LISTWIDTH - Wordwrap for item descriptions and help text.
   
   In this case we are interested in WIDTH, go ahead and go to the top of the rpgmakermvmz.py script file to find it.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/1c0a8a73-0b05-4354-97d2-be9a3eae778b)

Right now its at 60 characters. Clearly this is to big so lets shrink it down to 50. After that move your translated Map117 file back into /files and run it through the machine once more. Then place it back into the game folder for another test.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/f9a717f8-d08e-47b8-91d0-01e4e28cc67e)

16. Looks good to me! But maybe you don't like the size of the text or maybe you want it bigger. This can be adjusted in the script files in /js. Let's open them up.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/35193c23-6714-42c4-8d8a-f6f15f414951)

Hmm, lots to unpack here. Changing the font size for a game can either be easy or hard. It varies from game to game, the first place I like to look is `rmmz_windows.js` since this is the file that handles all the code for dialogue windows.

Doing a CTRL+F for fontSize gives me the following.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/1bbc017d-873b-4fad-9e4e-88f8ac233c8a)

That looks like a good place set the font size. Lets go ahead and change that value of that and see what happens.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/ea395b12-febc-4c89-8847-f42d2d1d3b3d)
![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/a9e8e3cf-d0c6-454c-af92-a6b179b32250)

Yup, beautiful tiny text made for ants. Perfect.

17. At this point, you've pretty much learned all you need to learn in order to translate a game.
   
    TLDR:
    * You bring data files into /files.
    * Translate them until you hit 0.
    * Enable 401 and 102 codes for Map and CommonEvent files.
    * Use breakpoints to QA the translations
    * Use Powertoys to scan text and find out where it needs to be changed in the files.
    * Adjust wordwrap with the global variables WIDTH and LISTWIDTH
    * Edit JS files to adjust game behavior like font size, or window size, etc.
   
   Sometimes you'll run into crashes or bugs, but that comes with the territory. Knowing how these files work is essential to creating these translations. But if you stick to just translating codes 401 and 102 and other game files, crashes will be minimal if non-existent.

   If you do wish to translate more advanced text hidden in other codes, its setup so that you can enable them and give it a try. It may break your game though so make sure to QA the text you are translating thouroughly.

Some tips that help improve translation:
* (HIGH IMPACT) In the prompt, enter the name of the main character and other female characters. This is going to help massively with misgendering.

![image](https://github.com/dazedanon/DazedMTLTool/assets/96628874/0b0d3911-a7f5-4731-bf00-0f8b3a3145f1)

* (MEDIUM IMPACT) Use the find/replace function to fix repeating translation issues in the code. For example lets say their are 100 instances of `Price.:` and you want to get rid of that period. Just do a Replace on `Price.:` with `Price:` to get that fixed easy peasy. (Note be careful on what you replace as you can end up breaking things)

* (MEDIUM IMPACT) If games have a speaker in the 101 code, setting CODE101 to `True` while translating your 401's and 102's will improve the translation a bunch. Otherwise leave it off.

Anyway thats about it for now. If you do have any questions feel free to PM me. I am more than willing to help you along with the tool and giving other tips.























