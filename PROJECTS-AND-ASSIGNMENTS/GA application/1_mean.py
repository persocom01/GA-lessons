# Demonstrates reading an excel file with the pandas module.
import pandas as pd

# If you wish to open a file dialog option instead, use:
# filedialog.askopenfilename()
import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
# To get specific columns.
df = pd.DataFrame(data, columns=['pledged'])

# To get just the mean, use df['column_name'].mean()
print(df.describe())
