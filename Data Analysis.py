import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")
# pd.DataFrame(data) # Checking which Product generates the most revenue
data["Revenue"] = data["Price"] * data["Quantity Purchased"]
# print(data.columns) # Gives us the numbers of columns of the data
test = data.groupby("Product Name")['Revenue'].sum()
print(test.sort_values(ascending=False)) # Giving us items with the highest revenue
# print(data.head())
# print(data.tail())
# print(test)

# Looking for the category that performs best
Done = data.groupby("Product Category")["Revenue"].sum()
print(Done.sort_values(ascending=False))

# Which Customer spends the most money
data['Spend'] = data["Revenue"] - data["Discount"]
text = data.groupby('Customer ID')['Spend'].sum()
# OR print(text.idxmax())
# print(text.max()) For it to print only one value
print(text.sort_values(ascending=False))

# What age group buy the most
exploit = data.groupby("Customer Age")["Revenue"].sum()
print(exploit.sort_values(ascending=False))

# Which payment method is preferred
payment = data.groupby("Payment Method")["Payment Method"].count()
print(payment.sort_values(ascending=False))

# Which Location generates the highest sales
# I think we can interpret this question in 2 ways
# 1. The total amount a group age can buy or
# 2. The number of customers in a given group ages
# Please ChatGPT I'm confused here make sure you explain the question
sales = data.groupby("Location")["Spend"].count()
print(sales.sort_values(ascending=False))


# Are there seasonal sales patterns
date = data.groupby("Date of Purchase")["Revenue"].sum()
print(date.sort_values(ascending=False))

# Are disocunts increasing sales
Discount = data.groupby("Discount")["Revenue"].sum()
print(Discount.sort_values(ascending=False))

# Are there unusual transactions?
# I don't really understand this part please ChatGPT explain for me when reading

# Provide recommendations to improve business performance.
# Add more discounts

# Visual representation
plt.figure()
plt.plot(data["Product Name"], data["Revenue"] )
plt.title("What products generate the most revenue")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.grid()
plt.show()
plt.figure()
sns.barplot(x=data["Product Category"],y=data["Revenue"])
plt.title("Which categories perform best")
plt.xlabel("Product Categories")
plt.ylabel("Revenue")
plt.grid()
plt.show()
plt.figure()
plt.barh(data["Discount"],data["Revenue"])
plt.title("Which customers spend the most money")
plt.xlabel("Revenue")
plt.ylabel("Discount")
plt.grid()
plt.show()
plt.figure()
sns.barplot(x=data["Customer Age"],y=data["Spend"])
plt.title("What age group buys the most")
plt.xlabel("Customer Age")
plt.ylabel("Spend")
plt.grid()
plt.show()
plt.figure()
sns.barplot(x=data["Customer ID"],y=data["Payment Method"])
plt.title("Which payment method is preferred")
plt.xlabel("Customer ID")
plt.ylabel("Payment Method")
plt.grid()
plt.show()
plt.figure()
plt.bar(data["Location"],data["Revenue"])
plt.title("Which locations generate the highest sales")
plt.xlabel("Location")
plt.ylabel("Revenue")
plt.grid()
plt.show()
plt.figure()
plt.bar(data["Date of Purchase"],data["Revenue"])
plt.title("Are there seasonal sales patterns")
plt.xlabel("Date of Purchase")
plt.ylabel("Revenue")
plt.grid()
plt.show()
plt.figure()
plt.scatter(data["Discount"],data["Revenue"])
plt.grid()
plt.show()

# bins = [0,25,35,45,100]
# labels = [
#     "18-25",
#     "26-35",
#     "36-45",
#     "46+"
# ]
# df["Age Group"] = pd.cut(
#     df["Age"],
#     bins=bins,
#     labels=labels
# )
# print(df)