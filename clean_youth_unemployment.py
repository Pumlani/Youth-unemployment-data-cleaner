
import pandas as pd
import re

# Load the data
df = pd.read_csv("youth_unemployment.csv")

# 1. Clean Name and Last Name
df['Name'] = df['Name'].str.strip().str.title()
df['Last Name'] = df['Last Name'].str.strip().str.title()

# 2. Clean Age - remove non-numeric, convert to int, drop unrealistic values
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df = df[df['Age'].between(15, 40)]

# 3. Format Phone Number - remove symbols, ensure 10-digit local format
def clean_phone(phone):
    phone = re.sub(r'\D', '', str(phone))  # remove all non-digit characters
    if phone.startswith('27'):
        phone = '0' + phone[2:]
    elif phone.startswith('83') and len(phone) == 9:
        phone = '0' + phone
    return phone if len(phone) == 10 else None

df['Phone Number'] = df['Phone Number'].apply(clean_phone)
df = df[df['Phone Number'].notnull()]

# 4. Standardize Province names
province_map = {
    'Eastern Cape': 'Eastern Cape',
    'E.Cape': 'Eastern Cape',
    'Eastern cape': 'Eastern Cape',
    'eastern Cape': 'Eastern Cape',
    'EC': 'Eastern Cape',
    ' Gauteng ': 'Gauteng',
    'Western Cape': 'Western Cape'
}
df['Province'] = df['Province'].map(lambda x: province_map.get(x.strip(), x.strip()))

# 5. Clean Contribution (%) column
df['Contribution (%)'] = df['Contribution (%)'].replace('NaN', '')
df['Contribution (%)'] = df['Contribution (%)'].str.replace('%', '', regex=False)
df['Contribution (%)'] = df['Contribution (%)'].str.replace(',', '.', regex=False)
df['Contribution (%)'] = pd.to_numeric(df['Contribution (%)'], errors='coerce')

# Drop rows with missing contribution
df = df[df['Contribution (%)'].notnull()]

# Save the cleaned dataset
df.to_csv("cleaned_youth_unemployment.csv", index=False)
print("✅ Cleaning complete. Saved to 'cleaned_youth_unemployment.csv'")
