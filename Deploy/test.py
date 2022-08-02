# import joblib

# load = joblib.load(open('dt.sav','rb'))
# lis = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# pred = load.predict([lis])
# print(pred)

import pickle

# pick = pickle.load(open('dt.sav','rb'))
with open('model.pkl' , 'rb') as f:
    lr = pickle.load(f)

lis = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

pred = lr.predict([lis])
# lr.predict(lis)
print(pred)
