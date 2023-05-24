#!/bin/bash

cd /home/deep/Bureau/fashionWebScraping/fashionWebScraping
echo "KOTON SPIDER START"
scrapy crawl -o rawdata_KOTON.json -t jsonlines fashionKOTON
