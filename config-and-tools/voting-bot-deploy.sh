#!/bin/bash

PROJECT_DIR=/srv/projects/voting-bot/
BOT_FILE="voting-bot.py"

# git pull in the server workspace dir
cd ${PROJECT_DIR}
git pull

# enable virtualenv (called 'discord-bot') for discord-bot
source /home/auto-deployer/.local/bin/virtualenvwrapper.sh
workon voting-bot

# restart discord-bot
pid=$(pgrep -f discord-bot.py)
echo "pid of discord bot to kill: ${pid}"


if [ ! -z "${pid}" ];   # if there is a pid of an existing discord bot
then
    kill ${pid}
fi

python ${BOT_FILE} &

exit 0;
