# Frybot 1.0.0

This is a Slack bot made in Python for the Python course @HE-ARC, based on Matt Groening's Futurama.

## Commands 

  - help 
  
  - fquote: sends a random quote (hard coded)

  - fgif  : sends a random gif (powered by Giphy)

  - fpict : sends a random pict (it can take an argument, but it's not necessary)
  
### How to use the bot

```
@frybot: help
@frybot: fquote
@frybot: fgif
@frybot: fpict [arg]
```

## Download

You can download it directly from here, but the file doesn't contain the Slack token nor the Google API key (config.py).

__OR__

You can download it from the command prompt (as it is on Pypi and the token has been kept \* ) :
```
pip install frybot
```
## Installation

You have to create a virtual environment like this : 
```
	> python -m venv frybot
	> cd frybot
	> C:\path_to_file\frybot\Scripts\activate.bat
```

put your newly downloaded bot files here and a this is ok, you can launch the bot with run.bat like this :
```
	> C:\path_to_file\frybot\run.bat
```

and if you cannot find the run.bat, all you have to do is : 

- create a new file you will name 'run.bat' in the frybot directory
- open it with a notepad
- and write this in it :

```
cd bot
python frybot.py
```

## Documentation

You can see the Sphinx documentation here : 

- [Frybot on ReadTheDocs.com] (frybot-100.rtfd.io) \*

althought I am still trying to figure out how to make this site understand where my doc is...

\* up from Saturday the 4th of June 2016, from early to later in the the morning

## Misc information

This is a school project and the bot is far from being perfect, it sure needs some refactor and further improvement.
