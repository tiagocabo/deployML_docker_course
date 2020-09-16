
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd
# loading dataset
iris = load_iris()
X = iris.data
y = iris.target

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

test_df = pd.DataFrame(X_test)
test_df['4'] = y_test
test_df.to_csv('/home/local/FARFETCH/tiago.cabo/Documents/private_projects/deployML_docker_course/API_data.csv')

# Build the model
clf = RandomForestClassifier(n_estimators=10)

# train the classifier
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Check accuracy
print("accuracy", accuracy_score(y_test, y_pred))


with open("/home/local/FARFETCH/tiago.cabo/Documents/private_projects/deployML_docker_course/rf.pkl", "wb") as model_pkl:
    pickle.dump(clf, model_pkl)

