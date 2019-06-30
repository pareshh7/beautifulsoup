import xlrd     # import pacakge neccesary to read file



# open workbook by specifying the file name and the file shoul be present at the working directory. 

workbook = xlrd.open_workbook('first-file.xlsx')



# get sheet using sheet_by_index method.Single parameter that is the sheet number.

worksheet = workbook.sheet_by_index(0)


# find total no of rows using : .nrows

rows = worksheet.nrows


# read rows using row_values(row number)

for row in range(rows):
    first_col,second_col = worksheet.row_values(row)
    print(first_col,'    ',second_col)
