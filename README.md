# 🧹 Youth Unemployment Data Cleaner – Butterworth Edition

This project simulates a real-world data cleaning task using a fictional dataset of unemployed youth in Butterworth, South Africa.

The messy dataset includes common issues like inconsistent casing, invalid age entries, poorly formatted phone numbers, and typos in province names. The goal is to clean, validate, and standardize the data for further analysis or policy use.

---

## 🧪 Sample Dataset Columns

- `Name`
- `Last Name`
- `Age`
- `Phone Number`
- `Province`
- `Contribution (%)` (estimated contribution to unemployment rate)

---

## 🛠️ What This Script Does

- ✅ Standardizes names and surnames
- ✅ Validates and filters age values
- ✅ Cleans and formats South African phone numbers
- ✅ Normalizes province names
- ✅ Converts contribution values to numeric format
- ✅ Outputs a cleaned dataset: `cleaned_youth_unemployment.csv`
- ✅ Prints a summary report of total entries, average age, and contribution stats

---

## 🧰 Tech Stack

- Python 3
- pandas
- regex
- (Runs well on Pydroid 3 mobile IDE)

---

## 📊 Summary Report Example
📊 Summary Report: 🧑 Total records after cleaning: 38 📍 Provinces in dataset: ['Eastern Cape', 'Gauteng', 'Western Cape'] 📈 Average age: 25.6 years 📊 Average contribution to unemployment: 6.42% 👥 Number of people per province: Eastern Cape    21 Gauteng         10 Western Cape     7

---

## 📎 How to Use

1. Place all files in the same directory
2. Run `clean_youth_unemployment.py`
3. View output and summary in terminal
4. Check `cleaned_youth_unemployment.csv` for the final dataset

---

## 📍 Author

**Pumlani Masebe**  
Software Developer | AI + Automation Learner | Based in South Africa  
[GitHub Profile](https://github.com/Pumlani) | [LinkedIn](https://linkedin.com/in/pumlanimasebe)


---