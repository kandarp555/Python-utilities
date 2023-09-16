# Write a program to create a dataframe "student_data" using
# pandas with the following details; provide at least 10
# sample data and display the same.
# Student name, enrollment number, date of birth, city, CPI
import pandas as pd

df = pd.DataFrame(
    {
        "StudentName": [
            "Kandarp",
            "Yash",
            "Gaurav",
            "Nikhil",
            "Gautam",
            "Yash2",
            "Mihir",
            "Kevin",
            "Hemal",
            "Dev",
        ],
        "EnrollmentNo": [1, 2, 9, 14, 15, 11, 12, 18, 17, 20],
        "Dob": [
            "05/05/2003",
            "01/01/2002",
            "02/02/2002",
            "03/03/2003",
            "04/04/2002",
            "06/06/2002",
            "07/072003",
            "08/08/2002",
            "09/09/2002",
            "10/10/2002",
        ],
        "City": [
            "Kalol",
            "Ahmedabad",
            "Disa",
            "Surat",
            "Ahmedabad1",
            "Ahmedabad2",
            "Ahmedabad3",
            "Ahmedabad4",
            "Ahmedabad5",
            "Jamnagar",
        ],
        "CPI": [8, 8.2, 8.3, 8.5, 8.6, 8.8, 8.9, 9.1, 9.3, 9.4],
    }
)
print(df)
print(df[["StudentName", "CPI"]])
print(df.sort_values(by=["CPI"], ascending=False))
print(df.sort_values(by=["StudentName"]))
df.drop("City", axis=1, inplace=True)
print(df)
df["Hobby"] = [
    "Singing",
    "TT",
    "Reading",
    "Markeing",
    "Gaming",
    "Dancing",
    "Cricket",
    "Badmilton",
    "Writing",
    "Coding",
]
print(df)
