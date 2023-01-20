#!/bin/bash

file=$1

cat $file | dalfox pipe --mass
