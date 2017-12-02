from sklearn import tree

# Creation of Data to make models of, Contains: Height, Weight, Shoe Size
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

# Gender of the individuals
Y= ['male','female','female','female','male','male','male', 'female', 'male', 'female', 'male']

# Instantiation of decision tree
clf = tree.DecisionTreeClassifier()

# Fit model to data
clf = clf.fit(X,Y)

# Retrieval of User data
height = int(input('Enter your height: '))
weight = int(input('Enter your weight: '))
shoeSize = int(input('Enter Your Shoe Size: '))
newPrediction = [height, weight, shoeSize]

# Gender classification prediction
prediction = clf.predict([newPrediction])

print(prediction)