#!/bin/bash

cd coco-caption
#python myeval.py $1
python cocolangeval.py $1
cd ../
