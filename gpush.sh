# gpush.sh
#!/bin/zsh

git add .
git commit -m "${1:-quick update}"
git push