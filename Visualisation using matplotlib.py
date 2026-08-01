import matplotlib.pyplot as plt

x = [1,2,3,4,5]
boys = [2,4,6,8,10]
girls= [1,3,5,7,9]
y = [3,4,2,1,5]
# plt.plot(x, y)
# plt.title("Monthly Sales") # To name our graph
# plt.xlabel("Month") # Naming the x-axis
# plt.ylabel("Sales") # Naming the y-axis
# plt.scatter(x, y)
# plt.show()

months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,150,130]

plt.plot(months, sales,color = "red", linestyle = "-.", linewidth = 1,  marker = "o")
# "-"   Solid
# "--"  Dashed
# ":"   Dotted
# "-."  Dash-dot
# o Circle
# s Square
# ^ Triangle
# * Star
# x (Cross
# + Plus)
plt.grid() # Make graph easier to read by adding line all over the graph
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.plot(x, boys, label="Boys")
plt.plot(y, girls, label="Girls")
plt.legend() # Legend is there to indicate
plt.savefig("sales.png") # Save the image in the storage
plt.show()
# Types of charts
# bar chart(.bar())
# scatter (.scatter())
# line plot (.plot())
# Histogram (.hist())
# Horizontal bar (.barh())
# pie charts (.pie())
# plt.xlim(0,10) Gives the x-axis limits
# plt.ylim(0,100) y-axis limits
# plt.plot(x,y1) Plotting multiple
# plt.plot(x,y2)
# plt.legend()
# plt.show()
# To show several lines on one graph we use subplots
# plt.subplot(1,2,1)
# plt.plot(x,y1)
# plt.subplot(1,2,2)
# plt.plot(x,y2)
# plt.title("Sales", fontsize=20) changing the font size

# | Function        | Purpose              |
# | --------------- | -------------------- |
# | `plt.figure()`  | Create a new figure  |
# | `plt.plot()`    | Line graph           |
# | `plt.scatter()` | Scatter plot         |
# | `plt.bar()`     | Vertical bar chart   |
# | `plt.barh()`    | Horizontal bar chart |
# | `plt.hist()`    | Histogram            |
# | `plt.pie()`     | Pie chart            |
# | `plt.title()`   | Add title            |
# | `plt.xlabel()`  | Label x-axis         |
# | `plt.ylabel()`  | Label y-axis         |
# | `plt.legend()`  | Show legend          |
# | `plt.grid()`    | Show grid            |
# | `plt.xlim()`    | Set x-axis limits    |
# | `plt.ylim()`    | Set y-axis limits    |
# | `plt.savefig()` | Save figure          |
# | `plt.show()`    | Display figure       |
