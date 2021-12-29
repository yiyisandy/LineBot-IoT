import pygsheets
gc = pygsheets.authorize(service_file='googlesheet.json')

sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1DflljkJf-o_dZy9Td-3c03_bAfocSfRWbgjT3t9C1ig/'
)
wks_list = sht.worksheets()
#print(wks_list)
wks = sht[0]
A1 = wks.cell('E1')
A1.value
#print(A1.value)
