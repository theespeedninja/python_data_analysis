# Student Performance Data Analysis

A comprehensive Python data analysis project that explores student academic performance using the UCI Student Performance Dataset. This project demonstrates data loading, cleaning, statistical analysis, and visualization techniques using pandas, matplotlib, and seaborn.

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Components](#analysis-components)
- [Visualizations](#visualizations)
- [Project Structure](#project-structure)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes student performance data to uncover insights about academic achievement patterns. The analysis focuses on various factors that might influence student grades, including demographics, study habits, and attendance patterns.

## 📊 Dataset

The project uses the **Student Performance Dataset** (Mathematics course) from the UCI Machine Learning Repository:
- **File**: `student-mat.csv`
- **Format**: CSV with semicolon (`;`) separator
- **Records**: 395 students
- **Features**: 33 attributes including demographics, social factors, and academic performance

### Key Variables Analyzed:
- `G3`: Final grade (target variable, 0-20 scale)
- `school`: Student's school (GP or MS)
- `sex`: Student's gender (F or M)
- `age`: Student's age (15-22)
- `studytime`: Weekly study time (1-4 scale)
- `absences`: Number of school absences
- `guardian`: Student's guardian (mother, father, or other)

## ✨ Features

- **Robust Data Loading**: Automatic file path detection and error handling
- **Data Cleaning**: Missing value detection and treatment
- **Statistical Analysis**: Descriptive statistics and group comparisons
- **Multiple Visualizations**: 5 different chart types for comprehensive insights
- **Error Handling**: Comprehensive exception handling for common data issues

## 🔧 Prerequisites

- Python 3.7+
- Required libraries:
  ```
  pandas
  matplotlib
  seaborn
  numpy (dependency of pandas)
  ```

## 🚀 Installation

1. Clone or download this repository
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Ensure the dataset file `student-mat.csv` is in the `student/` directory
4. Run the analysis script:
   ```bash
   python data_analysis.py
   ```

## 💻 Usage

### Basic Execution
```bash
python data_analysis.py
```

### Expected Output
The script will generate:
- Console output with data summary and statistics
- 5 visualization plots displayed sequentially
- Success/error messages for each operation

### Sample Console Output
```
✅ File loaded successfully!
✅ No missing values found.
✅ Data types fixed where necessary.
   school sex  age address famsize Pstatus  Medu  Fedu     Mjob      Fjob  ...
0      GP   F   18       U     GT3       A     4     4  at_home   teacher  ...
[Additional data preview and statistics]
```

## 🔍 Analysis Components

### 1. Data Loading & Cleaning
- **File Reading**: Handles CSV files with semicolon separators
- **Missing Values**: Automatic detection and filling with appropriate defaults
- **Data Types**: Ensures correct data types (especially numeric fields)
- **Duplicates**: Removes duplicate entries

### 2. Statistical Analysis
- **Descriptive Statistics**: Mean, median, standard deviation for all numeric variables
- **Group Analysis**:
  - Average final grades by school
  - Average final grades by gender
  - Average absences by guardian type

### 3. Data Exploration
- Dataset structure and information
- Data type verification
- Basic data quality checks

## 📈 Visualizations

The project generates five distinct visualizations:

### 1. Line Chart: Grade Trends
- **Purpose**: Shows final grade patterns across all students
- **Insights**: Identifies overall grade distribution and outliers

### 2. Bar Chart: Gender Comparison
- **Purpose**: Compares average final grades between male and female students
- **Colors**: Pink (Female), Sky Blue (Male)

### 3. Histogram: Absence Distribution
- **Purpose**: Shows frequency distribution of student absences
- **Insights**: Reveals attendance patterns and common absence ranges

### 4. Scatter Plot: Study Time vs Grades
- **Purpose**: Explores correlation between study time and academic performance
- **Insights**: Identifies potential relationship between effort and results

### 5. Box Plot: Grade Distribution by Gender
- **Purpose**: Shows grade distribution, median, and outliers by gender
- **Features**: Uses seaborn for enhanced statistical visualization

## 📁 Project Structure

```
project/
│
├── data_analysis.py          # Main analysis script
├── student/
│   └── student-mat.csv       # Dataset file
├── README.md                 # This file
└── requirements.txt          # Python dependencies (optional)
```

## 🛡️ Error Handling

The script includes comprehensive error handling for:

- **File Not Found**: Clear message if dataset file is missing
- **Parser Errors**: Handles CSV parsing issues (wrong separator, format)
- **Data Type Conversion**: Manages conversion errors for numeric fields
- **Missing Values**: Automatic detection and handling
- **General Exceptions**: Catches unexpected errors with informative messages

### Error Messages Examples:
```
❌ Error: File not found. Please check the file path.
❌ Error: File could not be parsed. Check the separator or file format.
⚠️ Missing values found. Filling with defaults...
```

## 🎨 Customization Options

### Modify File Path
```python
file_path = "your_path/student-mat.csv"  # Update this line
```

### Change Visualization Colors
```python
# Bar chart colors
grades_by_gender.plot(kind="bar", color=["your_color1", "your_color2"])

# Scatter plot color
plt.scatter(df["studytime"], df["G3"], color="your_color")
```

### Add New Analysis
```python
# Example: Add analysis by age groups
df.groupby("age")["G3"].mean()
```

## 🔬 Potential Extensions

- **Correlation Analysis**: Examine relationships between multiple variables
- **Predictive Modeling**: Build models to predict student performance
- **Interactive Visualizations**: Use Plotly for interactive charts
- **Statistical Tests**: Perform hypothesis testing for group differences
- **Feature Engineering**: Create new variables from existing ones

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions:
- Check the error handling messages in the console
- Ensure all dependencies are properly installed
- Verify the dataset file path and format
- Review the prerequisites section

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Student Performance Dataset
- Python data science community for excellent libraries (pandas, matplotlib, seaborn)
- Contributors and maintainers of open-source visualization tools

---

**Happy Analyzing! 📊✨**