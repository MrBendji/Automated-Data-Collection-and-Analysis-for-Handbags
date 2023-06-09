import json
from collections import OrderedDict
import csv
import os

with open("/home/deep/Bureau/fashionWebScraping/csvFiles/jsonFiles.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        jsonFile = row['jsonFile_raw']

        with open(jsonFile) as json_file:
            data = []
            i = 0
            seen = OrderedDict()

            for d in json_file:
                seen = json.loads(d)

                try:
                    if seen["productId"] is not None:
                        for key, value in seen.items():
                            print("ok")

                    i = i + 1
                    data.append(json.loads(d))

                except KeyError:
                    print("nok")

            print(i)
            baseFileName = os.path.splitext(jsonFile)[0]

            with open('/home/deep/Bureau/fashionWebScraping/jsonFiles/'+row['file_name_prep'], 'w') as out:
                json.dump(data, out)
