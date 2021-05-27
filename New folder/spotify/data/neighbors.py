from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np
from sklearn.metrics import classification_report , confusion_matrix
from sklearn.model_selection import cross_val_score


def spotify_prediction(acousticness,danceability, duration_ms, energy, 
               explicit, instrumentalness, key, liveness, loudness, mode,
               popularity, speechiness, tempo, valence):
               prediction = nn.predict([[acousticness,danceability, duration_ms, energy, 
               explicit, instrumentalness, key, liveness, loudness, mode,
               popularity, speechiness, tempo, valence]])
               return df["target_names"][prediction][0]



scaler = StandardScaler()

df = pd.read("spotify.csv")

scaler.fit(df.drop('Target'))

X_train, X_test, y_train, y_test = train_test_split(scaled_features, df["Target"], test_size=0.30)  

scaled_features = scaler.transform(df.drop('Target'))

nn = KNeighborsClassifier(n_neighbors=1)

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

pred = nn.predict(X_test)

nn.fit(y_train,y_test)

print(classification_report(y_test,pred))

# choosing K value 
accuracy_rate = []

for i in range(1,40):

    nn = KNeighborsClassifier(n_neighbors=i)
    score = cross_val_score(nn,df_feat, df["Target"],cv=10)
    accuracy_rate.append(score.mean())

error_rate = []
for i in range(1,40):

    nn = KNeighborsClassifier(n_neighbors=i)
    score = cross_val_score(nn,df_feat, df["Target"],cv=10)
    error_rate.append(1-score.mean())
    
error_rate_rate = []    
for i in range(1,40):

    nn = KNeighborsClassifier(n_neighbors=i)
    nn.fit(X_train,y_train)
    preb_i = nn.predict(X_test)
    error_rate_rate.append(np.mean(preb_i != y_test))

    



