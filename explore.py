import pandas as pd

# Specify the file name
file_name = "DictionaryVSLHamNoSys.txt"

# Read the file into a pandas DataFrame
df = pd.read_csv(file_name, sep='\t', header=0)

# Specify the output file name
output_file_name = "Dict_VSL_HamNoSys.xlsx"

# Write the DataFrame to an Excel file
with pd.ExcelWriter(output_file_name, engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

print(f'DataFrame has been saved to {output_file_name}')
