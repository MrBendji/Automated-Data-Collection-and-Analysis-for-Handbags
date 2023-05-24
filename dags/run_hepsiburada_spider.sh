#!/bin/bash

cd /home/deep/Bureau/fashionWebScraping/fashionWebScraping
echo "HEPSIBURADA SPIDER START"
scrapy crawl -o rawdata_HEPSIBURADA.json -t jsonlines fashionHEPSIBURADA
