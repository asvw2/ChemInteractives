
import openpyxl

# Create a new workbook
wb = openpyxl.Workbook()
ws = wb.active

# Write header rows
ws.append(['Surname', 'Year 12 Set', 'Year 13 Set', '1a', '2a'])
ws.append(['', '', '', 'CP1', 'CP2'])


# Write data rows
ws.append(['StudentA', '12A', '13A', 'y', 'wt'])
ws.append(['StudentB', '12B', '13B', 'wt', 'n'])
ws.append(['StudentC', '12A', '13A', 'n', 'y'])

# Save the workbook
wb.save('test_data.xlsx')

print("Dummy excel file 'test_data.xlsx' created successfully.")
