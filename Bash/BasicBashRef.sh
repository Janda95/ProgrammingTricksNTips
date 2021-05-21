#!/user/bin/env bash

echo Hello world

echo 'This is the first line'; echo 'This is the second line'

Variable="A string"

echo "$Variable"

echo ${Variable}


echo "Last program's return value: $?"
echo "Script's PID: $$"
echo "Number of arguments passed to script $#"
echo "All argumets passed to script: $@"
echo "Script's arguments seperated into different variables: $1 $2 ect"


echo "I am currently in $(pwd)"
echo "I am in $PWD"


echo "What is your favorite color?"
read favoriteColor
echo "I like the color: $favoriteColor as well!"

if [ $favoriteColor != "Yellow" ]
then
    echo "Yellow is the best"
else
    echo "You don't like yellow?"
fi # indicates end of conditional code


# alias ll="ls -al"

# alias ping='ping -c 5'
# \ping 192.168.1.1

# Useful for working accross directories
(echo "First, I'm here: $PWD") && (cd someDir; echo "Then, I'm here: $PWD")
(echo "First, I'm here: $PWD") && (cd someDir; echo "Then, I'm here: $PWD")