#!/bin/bash

clear
figlet "Recon.sh" | lolcat
echo 'By: Sh0gun' | lolcat

domain=$1
gauplus -random-agent -o urls.txt $domain
cat urls.txt | grep '=' | sed 's/=.*/=/' > clean.txt
cat clean.txt | urldedupe -s > no_clones.txt
httpx -l no_clones.txt -mc 200 > actives.txt
