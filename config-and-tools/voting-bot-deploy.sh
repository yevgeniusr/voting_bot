#!/bin/bash

PROJECT_DIR=/srv/projects/voting_bot/
VIRTUAL_ENV_NAME="voting-bot"
BOT_FILE="voting-bot.py"

# git pull in the server workspace dir
cd ${PROJECT_DIR}
git pull

# enable virtualenv (called 'discord-bot') for discord-bot
source /home/auto-deployer/.local/bin/virtualenvwrapper.sh
workon ${VIRTUAL_ENV_NAME}

# restart discord-bot
pid=$(pgrep -f ${BOT_FILE})
echo "pid of discord bot to kill: ${pid}"


if [ ! -z "${pid}" ];   # if there is a pid of an existing discord bot
then
    kill ${pid}
fi

python ${BOT_FILE} &

exit 0;
