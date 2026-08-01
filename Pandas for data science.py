import pandas as pd

# Create data
students = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [20, 19, 21],
    "Grade": ["A", "B", "A"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(students)

# Save DataFrame to CSV
df.to_csv("students.csv", index=False) # Index = False removes the index columns
print(pd.read_csv("students.csv"))
# Writing into a files using pandas
# to_csv()
# to_excel()
# to_json()
# reading into files using pandas

print(df.head()) # Reading the first 5 elements of the list, By default it's set to 5 lines, but we can set a value inside the bracket
print(df.tail()) # Reading the last elements of the list, By default it's still set to the last 5 lines
print(df.sample()) # Return a sample of our data, It chooses a random value
df.info() # Gives info about your data set
df.describe() # Gives statistical information about numerical columns.
df.shape # It gives the numbers of row and column
df.columns # gives the names of all columns
df.columns = ["Student", "Years", "Marks"] # Rename colums

# The main difference:
# loc → selects using labels (names)
# iloc → selects using positions (numbers)
print(df.loc[1,'Student'])
# df.loc[row_position, column_position]
print(df.loc[0:2])
print(df.loc[:, ["Name", "Score"]])
# df.loc[df["Score"] > 80]
# df.iloc[row_position, column_position]
print(df.iloc[0])
df.drop(columns="column_name") # Drop is used to remove a column or a row in a data set
df.drop(columns=["Age", "Score"]) # Removing multiple columns
df.drop(index=0) # To remove a row we use the index method
df.drop(index=[1,3]) # To remove multiple rows
df.rename(columns={"Student": "Name", "Years": "Years"}, inplace=True) # inplace = True, Permanently renaming it, we can also use it for the drop() method
df.drop(2, axis=0) # axis means column
df.rename(columns={"old_name": "new_name"}) # Renaming a column
df.rename(columns={
    "Name": "Student", # Renaming multiple columns
    "Score": "Marks"
})
df.rename(index={
    0: "A",
    1: "B", # Renaming rows
    2: "C" # rename() does not modify the original DataFrame by default
    # To replace it forever we use the inplace = True
})
df.sort_values(by="Age") # Used to sort values by specific objects
df.isnull() #checks whether a value is missing.
df.notnull()# The opposite of isnull()
df.fillna("unknow") # Instead of removing missing values, you can replace them.
df.dropna()# Instead of replacing missing values, remove them
df.duplicated() # Finds duplicates
df.drop_duplicates() # Remove duplicates
df.groupby("Name")# is used to group rows that have the same value.
df.groupby("Department")["Salary"].mean() # Calculating the mean from a list
df.groupby("Department")["Salary"].sum() # Calculating the sum
df.groupby("Department")["Employee"].count() # Counting the numbers of values
df.groupby("Department")["Salary"].max()
df.groupby("Department")["Salary"].min()
# df.merge() combines two DataFrames based on a common column.
student = {"Name": ["John", "Alice", "Bob"],
           "ID": [1,2,3]}
score = {
    "score":[16,19,18],
     'ID': [1,2,3]
   }
pd.DataFrame([student,score])
print(pd.merge(student, score, on="ID"))
df.apply(lambda x: x * 1.1)# Help us to use our own functions on the pandas
df.str.contains() # Checks if a string contains a certain word or letter.