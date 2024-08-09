# import openpyxl
#
#
# def create_excel_sheet(file_name, sheet_name, data):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = sheet_name
#
#     # Write data to the sheet
#     for row_idx, row_data in enumerate(data, start=1):
#         for col_idx, cell_value in enumerate(row_data, start=1):
#             sheet.cell(row=row_idx, column=col_idx, value=cell_value)
#
#     # Save the workbook
#     workbook.save(file_name)
#     print(f"Excel sheet '{sheet_name}' created successfully in '{file_name}'")
#
#
# file_name = "example.xlsx"
# sheet_name = "Sheet1"
# data = [
#     ["Name", 7],
#     ["Alice", 30],
#     ["Bob", 25],
#     ["Charlie", 35]
# ]
#
# create_excel_sheet(file_name, sheet_name, data)
