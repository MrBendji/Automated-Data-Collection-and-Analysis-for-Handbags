#!/bin/bash

cd /home/deep/Bureau/fashionWebScraping/fashionWebScraping
echo "DERIMOD SPIDER START"
scrapy crawl -o rawdata_DERIMOD.json -t jsonlines fashionDERIMOD
