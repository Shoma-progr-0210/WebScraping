import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = ("https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662&year=&month=&day=&view=p5")

r = requests.get(url)

TokyoRA_html = BeautifulSoup(r.content, "html.parser")
# print(TokyoRA_html.text)


table = TokyoRA_html.findAll("table", {"class":"data2_s"})[0]
rows = table.findAll("tr")

# encoding = 'shift-jis'
fileName = 'TokyoRA_v2.xlsx'

def readTable():
    for row in rows:
        xlsxRow = []
        for i,cell in enumerate(row.findAll(['td', 'th'])):
            if i == 0:
                getText = cell.get_text()[:4]
            else:
                getText = cell.get_text()
            xlsxRow.append(getText.replace(']', '').replace(')', ''))
        xlsxList.append(xlsxRow)

def writeList2D(sheet, list2D, startRow, startCol):
    for y, row in enumerate(list2D):
        for x, cell in enumerate(row):
            sheet.cell(row=startRow + y,
                       column=startCol + x,
                       value=list2D[y][x])

xlsxList = []
readTable()

wb = Workbook()
ws = wb.active
writeList2D(ws, xlsxList, 1, 1)

wb.save(fileName)