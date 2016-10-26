import requests


json = [
    {'Age': 85, 'Sex': 'male', 'Embarked': 'S'},
    {'Age': 24, 'Sex': 'female', 'Embarked': 'C'},
    {'Age': 3, 'Sex': 'male', 'Embarked': 'C'},
    {'Age': 21, 'Sex': 'male', 'Embarked': 'S'}
    ]

res = requests.post("http://localhost:5566/predict", json = json)

print(res.text)