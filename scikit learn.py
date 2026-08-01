# sklearn
# │
# ├── model_selection
# │      └── train_test_split
# │
# ├── linear_model
# │      └── LinearRegression
# │
# ├── tree
# │      └── DecisionTreeClassifier
# │
# ├── metrics
# │      └── accuracy_score
# │
# └── preprocessing
#        └── StandardScaler

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "Hours":[1,2,3,4,5],
    "Score":[40,50,60,75,90]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Score"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(prediction)