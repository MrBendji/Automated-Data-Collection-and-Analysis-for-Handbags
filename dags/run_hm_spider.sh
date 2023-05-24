#!/bin/bash

cd /home/deep/Bureau/fashionWebScraping/fashionWebScraping
echo "HM SPIDER START"
scrapy crawl -o rawdata_HM.json -t jsonlines fashionHM
