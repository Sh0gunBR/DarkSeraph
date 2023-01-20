#!/bin/bash

clear
domain=$1
findomain --output -t $domain > subdoms.txt;
cat subdoms.txt | httprobe > subs.txt;
clear
