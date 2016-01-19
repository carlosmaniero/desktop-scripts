# Virtual env options
export VIRTUAL_ENV_DISABLE_PROMPT=1
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh

# Django autocomplete
source $HOME/.django_bash_completion.sh

# Scripts
PATH="$PATH:/home/carlos/scripts/"

# Set default option
export VISUAL=vim
export EDITOR="$VISUAL"


# get current branch in git repo
function parse_git_branch() {
    BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
    if [ ! "${BRANCH}" == "" ]
    then
        STAT=`parse_git_dirty`
        echo " ⑃ ${BRANCH}${STAT} "
    else
        echo ""
    fi
}

# get current status of git repo
function parse_git_dirty {
    status=`git status 2>&1 | tee`
    dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
    untracked=`echo -n "${status}" 2> /dev/null | grep "Untracked files" &> /dev/null; echo "$?"`
    ahead=`echo -n "${status}" 2> /dev/null | grep "Your branch is ahead of" &> /dev/null; echo "$?"`
    newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
    renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
    deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
    bits=''
    if [ "${renamed}" == "0" ]; then
        bits=">${bits}"
    fi
    if [ "${ahead}" == "0" ]; then
        bits="*${bits}"
    fi
    if [ "${newfile}" == "0" ]; then
        bits="+${bits}"
    fi
    if [ "${untracked}" == "0" ]; then
        bits="?${bits}"
    fi
    if [ "${deleted}" == "0" ]; then
        bits="x${bits}"
    fi
    if [ "${dirty}" == "0" ]; then
        bits="!${bits}"
    fi
    if [ ! "${bits}" == "" ]; then
        echo "${bits}"
    else
        echo ""
    fi
}

ORIGINAL_PS1="${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \$\[\033[00m\] "
GIT_PS1="\[$(tput bold)\]\[\033[48;5;8m\]\`parse_git_branch\`\[$(tput sgr0)\]"
COMUNIST_PS1="\[\e[31;47m\]☭\[\e[m\]\[\e[47m\] \[\e[m\]"
export ENV_PS1=""
function show_env {
    if [[ -z "$VIRTUAL_ENV" ]] ; then
        export ENV_PS1=""
    else
        export ENV_PS1="\[$(tput bold)\]\[\e[37;41m\] `basename $VIRTUAL_ENV` \[\e[m\]\[$(tput sgr0)\]"
    fi
    export PS1="$COMUNIST_PS1$GIT_PS1$ENV_PS1 $ORIGINAL_PS1"
}

export PROMPT_COMMAND=show_env

eval "$(thefuck --alias)"
# You can use whatever you want as an alias, like for Mondays:
eval "$(thefuck --alias FUCK)"


alias editor=$EDITOR
alias e=$EDITOR
alias manage=./manage.py
alias pyclean='find . -name "*.pyc" -exec rm -rf {} \;'
