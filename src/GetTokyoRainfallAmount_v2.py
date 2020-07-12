import requests
from bs4 import BeautifulSoup
import csv

url = ("https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662&year=&month=&day=&view=p5")

r = requests.get(url)

TokyoRA_html = BeautifulSoup(r.content, "html.parser")
# print(TokyoRA_html.text)


table = TokyoRA_html.findAll("table", {"class":"data2_s"})[0]
rows = table.findAll("tr")

encoding = 'shift-jis'
fileName = 'TokyoRA_v2.csv'

with open(fileName, "w", newline = '', encoding=encoding) as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for i,cell in enumerate(row.findAll(['td', 'th'])):
            if i == 0:
                getText = cell.get_text()[:4]
            else:
                getText = cell.get_text()
            csvRow.append(getText.replace(']', '').replace(')', ''))
        writer.writerow(csvRow)