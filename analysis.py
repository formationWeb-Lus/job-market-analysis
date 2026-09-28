
import pandas as pd
import matplotlib.pyplot as plt
import os


# ============================================================
# JOB MARKET DATA ANALYSIS
# ============================================================
#
# This program analyzes a free job market dataset.
#
# The program answers two questions:
#
# Question 1:
# Which technical skills are most demanded in the job market?
#
# Question 2:
# What is the average salary for each job family?
#
# The program demonstrates:
# - Data conversion
# - Filtering
# - Aggregation
# - Sorting
# - Grouping
# - Data visualization
# ============================================================


# ============================================================
# 1. LOAD THE DATASET
# ============================================================

# Path to the Excel dataset
data_path = "data/job_market.xlsx"


# Check whether the dataset exists
if not os.path.exists(data_path):
    print("ERROR: Dataset not found.")
    print(f"Expected file: {data_path}")
    raise SystemExit


# Read the Excel file using Pandas
df = pd.read_excel(data_path)


print("=" * 70)
print("JOB MARKET DATA ANALYSIS")
print("=" * 70)

print(f"\nDataset loaded successfully.")
print(f"Number of job postings: {len(df)}")
print(f"Number of columns: {len(df.columns)}")


# ============================================================
# 2. EXPLORE THE DATASET
# ============================================================

print("\n" + "=" * 70)
print("DATASET EXPLORATION")
print("=" * 70)


# Display the column names
print("\nColumns in the dataset:")
print(df.columns.tolist())


# Display the first five rows
print("\nFirst five job postings:")
print(df.head().to_string())


# ============================================================
# 3. DATA CLEANING AND CONVERSION
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)


# ------------------------------------------------------------
# Convert salary_average to numeric
# ------------------------------------------------------------

if "salary_average" in df.columns:

    # Convert salary values to numbers.
    # Invalid values are converted to NaN.
    df["salary_average"] = pd.to_numeric(
        df["salary_average"],
        errors="coerce"
    )

    print("\nSalary values converted to numeric format.")


# ------------------------------------------------------------
# Handle missing job family values
# ------------------------------------------------------------

if "job_family" in df.columns:

    # Replace missing job family values with "Unknown"
    df["job_family"] = df["job_family"].fillna("Unknown")


# ============================================================
# 4. QUESTION 1
# ============================================================
#
# Which technical skills are most demanded in the job market?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1")
print("Which technical skills are most demanded in the job market?")
print("=" * 70)


# Find columns containing technical skill information.
# The dataset uses the "skill_" prefix.
skill_columns = [
    column
    for column in df.columns
    if column.startswith("skill_")
]


if len(skill_columns) == 0:

    print("\nNo technical skill columns were found.")

else:

    # --------------------------------------------------------
    # DATA CONVERSION
    # --------------------------------------------------------
    #
    # Convert each skill column to numeric values.
    #
    # 1 means that the skill is required.
    # 0 means that the skill is not required.
    # --------------------------------------------------------

    for column in skill_columns:

        df[column] = (
            pd.to_numeric(
                df[column],
                errors="coerce"
            )
            .fillna(0)
        )


    # --------------------------------------------------------
    # AGGREGATION
    # --------------------------------------------------------
    #
    # Sum each skill column.
    #
    # Example:
    # If Python has a sum of 45,
    # Python is required by 45 job postings.
    # --------------------------------------------------------

    skill_counts = (
        df[skill_columns]
        .sum()
    )


    # --------------------------------------------------------
    # SORTING
    # --------------------------------------------------------
    #
    # Sort skills from most demanded to least demanded.
    # --------------------------------------------------------

    skill_counts = (
        skill_counts
        .sort_values(ascending=False)
    )


    # Convert technical column names into readable names.
    #
    # Example:
    # skill_python -> Python
    # skill_javascript -> Javascript
    skill_counts.index = (
        skill_counts.index
        .str.replace(
            "skill_",
            "",
            regex=False
        )
        .str.replace(
            "_",
            " ",
            regex=False
        )
        .str.title()
    )


    # Select the top 10 skills
    top_10_skills = skill_counts.head(10)


    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    print("\nTop 10 most demanded technical skills:\n")


    for skill, count in top_10_skills.items():

        percentage = (
            count / len(df)
        ) * 100

        print(
            f"{skill:<25}"
            f"{int(count):>5} postings "
            f"({percentage:.1f}%)"
        )


    # --------------------------------------------------------
    # ANSWER QUESTION 1
    # --------------------------------------------------------

    most_demanded_skill = skill_counts.index[0]

    most_demanded_count = (
        skill_counts.iloc[0]
    )

    most_demanded_percentage = (
        most_demanded_count / len(df)
    ) * 100


    print("\nANSWER TO QUESTION 1:")

    print(
        f"The most demanded technical skill is "
        f"{most_demanded_skill}."
    )

    print(
        f"It appears in "
        f"{int(most_demanded_count)} out of "
        f"{len(df)} job postings "
        f"({most_demanded_percentage:.1f}%)."
    )


# ============================================================
# 5. QUESTION 2
# ============================================================
#
# What is the average salary for each job family?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2")
print("What is the average salary for each job family?")
print("=" * 70)


if (
    "salary_average" not in df.columns
    or "job_family" not in df.columns
):

    print(
        "\nThe required salary or job family column "
        "was not found."
    )

else:

    # --------------------------------------------------------
    # FILTERING
    # --------------------------------------------------------
    #
    # Remove missing salaries and unrealistic salaries.
    #
    # We use $20,000 as the minimum annual salary
    # for this analysis.
    # --------------------------------------------------------

    MINIMUM_SALARY = 20000


    salary_data = df[
        df["salary_average"].notna()
        & (df["salary_average"] >= MINIMUM_SALARY)
    ].copy()


    print(
        f"\nJob postings before salary filtering: "
        f"{len(df)}"
    )

    print(
        f"Job postings used for salary analysis: "
        f"{len(salary_data)}"
    )


    # --------------------------------------------------------
    # AGGREGATION
    # --------------------------------------------------------
    #
    # Group job postings by job family and calculate
    # the average salary.
    # --------------------------------------------------------

    average_salary = (
        salary_data
        .groupby("job_family")["salary_average"]
        .mean()
    )


    # --------------------------------------------------------
    # SORTING
    # --------------------------------------------------------
    #
    # Sort job families from highest average salary
    # to lowest average salary.
    # --------------------------------------------------------

    average_salary = (
        average_salary
        .sort_values(ascending=False)
    )


    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    print("\nAverage salary by job family:\n")


    for family, salary in average_salary.items():

        print(
            f"{family:<30}"
            f"${salary:,.2f}"
        )


    # --------------------------------------------------------
    # ANSWER QUESTION 2
    # --------------------------------------------------------

    highest_salary_family = (
        average_salary.index[0]
    )

    highest_average_salary = (
        average_salary.iloc[0]
    )


    print("\nANSWER TO QUESTION 2:")

    print(
        f"The job family with the highest average salary "
        f"is {highest_salary_family}."
    )

    print(
        f"The average salary for this job family is "
        f"${highest_average_salary:,.2f}."
    )


# ============================================================
# 6. ADDITIONAL REQUIREMENT
# ============================================================
#
# Draw a graph showing some of the results.
# ============================================================

print("\n" + "=" * 70)
print("DATA VISUALIZATION")
print("=" * 70)


if "top_10_skills" in locals():

    # Reverse the order so the most demanded skill
    # appears at the top of the chart.
    chart_data = (
        top_10_skills
        .sort_values(ascending=True)
    )


    # Create the graph
    plt.figure(figsize=(10, 6))


    plt.barh(
        chart_data.index,
        chart_data.values
    )


    # Add chart title
    plt.title(
        "Top 10 Most Demanded Technical Skills"
    )


    # Add axis labels
    plt.xlabel(
        "Number of Job Postings"
    )

    plt.ylabel(
        "Technical Skill"
    )


    # Add values to the bars
    for index, value in enumerate(
        chart_data.values
    ):

        plt.text(
            value + 0.2,
            index,
            str(int(value)),
            va="center"
        )


    # Adjust the layout
    plt.tight_layout()


    # Save the graph
    graph_file = (
        "top_10_technical_skills.png"
    )


    plt.savefig(
        graph_file,
        dpi=300,
        bbox_inches="tight"
    )


    print(
        f"\nGraph saved as: {graph_file}"
    )


    # Display the graph
    plt.show()


    # Close the figure
    plt.close()


# ============================================================
# 7. CONCLUSION
# ============================================================

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)


print(
    "\nThis analysis used Pandas to analyze job market data."
)

print(
    "Question 1 was answered by converting skill data, "
    "aggregating skill requirements, and sorting the results."
)

print(
    "Question 2 was answered by filtering salary data, "
    "grouping jobs by family, calculating average salaries, "
    "and sorting the results."
)

print(
    "A graph was also created to visualize the most demanded "
    "technical skills."
)


# ============================================================
# 8. LIMITATIONS
# ============================================================

print("\n" + "=" * 70)
print("LIMITATIONS")
print("=" * 70)


print(
    "\n1. The dataset contains a limited number of job postings."
)

print(
    "2. The dataset may not represent the entire job market."
)

print(
    "3. Salary can vary depending on location, experience, "
    "company, and other factors."
)

print(
    "4. The results describe the dataset and should not "
    "automatically be generalized to the entire job market."
)


print("\n" + "=" * 70)
print("ANALYSIS COMPLETED")
print("=" * 70)
