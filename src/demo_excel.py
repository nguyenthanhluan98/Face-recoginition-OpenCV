import pandas as pd

data = pd.read_excel (r"diemdanh.xlsx") 
df = pd.DataFrame(data)

print(len(df.columns))


print(len(df.columns))

#for i in range(len(data)):
   # print(data["Họ và tên"][i])

#print(data.head())
'''
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
print(len(df.columns))
'''
# Close the Pandas Excel writer and output the Excel file.
#writer.save()