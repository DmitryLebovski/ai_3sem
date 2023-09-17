from sklearn.feature_extraction import DictVectorizer

data_dict = [{'карий': 2, 'серый': 4},
             {'карий': 5, 'голубой': 4},
             {'карий': 10, 'зеленый': 1}]
dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(data_dict)
features