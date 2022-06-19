export PS1="\[\033[38;5;93m\][\u\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;99m\]\W\[$(tput sgr0)\]\[\033[38;5;93m\]]\[$(tput sgr0)\]\$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\\$ \[$(tput sgr0)\]"
set -o vi
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'
