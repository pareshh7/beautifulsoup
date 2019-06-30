from xlsxwriter import Workbook     # neccessary import



# make workbook using Workbook class, specify the file name

workbook = Workbook('first_file.xlsx')

#an excel file with the name 'first_file gets created

# add work sheet to the workbook

worksheet = workbook.add_worksheet()


# write function parameters (row,column,value)

for row in range(200):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)


# close workbook

workbook.close()
