import pandas as pd

# Task 1: Load the datasets
# Error handling sapce:
file_path = "student\student-mat.csv"
try:
    # Try reading the file with the correct separator
    df = pd.read_csv(file_path, sep=";")
    print("✅ File loaded successfully!")

    # Handle missing values
    if df.isnull().values.any():
        print("⚠️ Missing values found. Filling with defaults...")
        df = df.fillna(0)  # Example: fill NaN with 0 (you could also drop them)
    else:
        print("✅ No missing values found.")

    # Handle incorrect data types
    try:
        # Example: ensure 'age' is integer
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        # Fill any conversion errors with 0
        df["age"] = df["age"].fillna(0).astype(int)
        print("✅ Data types fixed where necessary.")
    except Exception as e:
        print("⚠️ Error converting data types:", e)

except FileNotFoundError:
    print("❌ Error: File not found. Please check the file path.")
except pd.errors.ParserError:
    print("❌ Error: File could not be parsed. Check the separator or file format.")
except Exception as e:
    print("❌ An unexpected error occurred:", e)

print(df.head()) # Displaying the first few rows of the dataset to inspect it
# More dataset exploration:
print(df.info()) # Displaying the structure and data types of the dataset
df.drop_duplicates() # Removing duplicate entries if any

# Task 2: Basic Data Analysis
print(df.describe()) # Displaying summary statistics of the dataset
#performing groupings and calculating mean
# Mean final grade (G3) per school
df.groupby("school")["G3"].mean()
# Mean final grade (G3) per gender
df.groupby("sex")["G3"].mean()
# Mean absences per guardian
df.groupby("guardian")["absences"].mean()

#Task 3: Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Line chart: student index vs final grade
plt.plot(df.index, df["G3"], color="blue", marker="o")
plt.title("Final Grades Trend Across Students")
plt.xlabel("Student Index")
plt.ylabel("Final Grade (G3)")
plt.show()

# BarChart(comparison between categories): Average final grade
grades_by_gender = df.groupby("sex")["G3"].mean()
grades_by_gender.plot(kind="bar", color=["pink", "skyblue"])
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Grade (G3)")
plt.show()

#Histogram(distribution of numeric data): Distribution of absences
plt.hist(df["absences"], bins=20, color="green", edgecolor="black")
plt.title("Distribution of Absences")
plt.xlabel("Number of Absences")
plt.ylabel("Frequency")
plt.show()

# Scatter plot(relationship between two numeric variables): Study time vs final grade
plt.scatter(df["studytime"], df["G3"], color="purple")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time (1–4 scale)")
plt.ylabel("Final Grade (G3)")
plt.show()

# Boxplot: Final grade distribution by gender
sns.boxplot(x="sex", y="G3", hue="sex", data=df, palette="Set2", legend=False)
plt.title("Distribution of Final Grades by Gender")
plt.xlabel("Gender")
plt.ylabel("Final Grade (G3)")
plt.show()
