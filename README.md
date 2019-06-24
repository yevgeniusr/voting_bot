# voting_bot


## Prerequisites

You need Python 3.5+ for this. The `discord.py` library used in this project does not support Python2.

## Running

### Bot Token

Create a file called `creds.py` in the same directory as `voting-bot.py`.

Add a line with your discord bot token like this:

```python
bot_token = "YOUR_DISCORD_BOT_TOKEN_HERE"
```

To get the actual, correct bot token value, ask anyone on the Discord server,
preferably *theratulz* or *KnifeAndFawkes* or *anattaguy*.

### VirtualEnv

Create a [VirtualEnvironment](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) for this project, activate it, and install the dependencies like so on the command line:

```
pip install -r requirements.txt
```

This will install the `discord.py` module into the virutal environment.


### Run Forrest, Run!

Now you should be able to run the bot like so:


```
$ python voting-bot.py
Logged in as:
Voting Bot
590257854452203558
-----------
```
