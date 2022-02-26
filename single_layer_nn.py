#Program to implement Neural Network from scratch with single layer.
#Input layer -> Output Layer

import numpy as np

class SingleLayerNN(object):
    def __init__(self, input_dimensions=2,number_of_nodes=4):
        #initializing the input_dimensions and number of nodes in the output layer
        self.input_dimensions = input_dimensions
        self.number_of_nodes = number_of_nodes
        self.initialize_weights()


    def initialize_weights(self,seed=None):
        #initializing weights randomly using numpy
        if seed != None:
            np.random.seed(seed)
            self.weight = np.random.randn(self.number_of_nodes,self.input_dimensions+1)
        else:
            self.weight = np.random.randn(self.number_of_nodes,self.input_dimensions+1)
        #print(self.weight.ndim)

    def set_weights(self, W):
        #If wewights are given manually, set the weights and cross check with the input_dimensions and number_of_nodes
        #NOTE: Here bias is included in weight matrix, hence number_of_nodes + 1
        nodes = self.number_of_nodes +1
        d = self.input_dimensions
        self.weight = W
        if self.weight.shape != (nodes,d):
          return -1
        else:
          return None

    def get_weights(self):
        #Function to get weight matrix
        return self.weight
    def predict(self, X):
        #Function for predicting the output once model is trained
        #X is the input
        #NOTE: Here bias is included in weight matrix, hence np.vstack(X,ones) to add extra ones to multiply with bias
        m,n = np.shape(X)
        weight = self.weight
        hidden_output = np.dot(weight,np.vstack((np.ones(n),X)))
        #print(hidden_output)
        output = []
        for i in range(len(hidden_output)):
          for j in range(len(hidden_output[0])):
            if hidden_output[i][j] <= 0:
              output.append(0)
            else:
              output.append(1)
        #print(output)
        return np.reshape(output,(self.number_of_nodes,n))



    def train(self, X, Y, num_epochs=10,  alpha=0.1):
        #Function to train neural network weights and bias
        #NOTE: Here bias is included in weight matrix, hence np.vstack(X,ones) to add extra ones to multiply with bias
        """
        :param X: Array of input [input_dimensions,n_samples]
        :param y: Array of desired (target) outputs [number_of_nodes ,n_samples]
        :param num_epochs: Number of times training should be repeated over all input data
        :param alpha: Learning rate
        """
        m,n = np.shape(X)
        X = np.vstack((np.ones(n),X))
        for i in range(num_epochs):
          for j in range(n):
            input = X[:,j].reshape(self.input_dimensions+1,1)
            output = Y[:,j].reshape(self.number_of_nodes,1)
            predicted = np.dot(self.weight,input)
            predicted[predicted > 0] = 1
            predicted[predicted <= 0] = 0
            self.weight = self.weight + (alpha * np.dot((output - predicted),input.transpose()))

    def calculate_percent_error(self,X, Y):
        #Function to calculate wrong prediction
        e = 0
        prediction = self.predict(X)
        """print('prediction: ')
        print(prediction)
        print('Y: ')
        print(Y)"""
        m,n = np.shape(X)
        for i in range(n):
            if (prediction[0][i] == Y[0][i]) and (prediction[1][i] == Y[1][i]) :
                e += 1
        #print(e)
        return (e/n)*100


if __name__ == "__main__":
    input_dimensions = 2
    number_of_nodes = 2

    model = SingleLayerNN(input_dimensions=input_dimensions, number_of_nodes=number_of_nodes)
    model.initialize_weights(seed=2)
    X_train = np.array([[-1.43815556, 0.10089809, -1.25432937, 1.48410426],
                        [-1.81784194, 0.42935033, -1.2806198, 0.06527391]])

    print(model.predict(X_train))
    Y_train = np.array([[1, 0, 0, 1], [0, 1, 1, 0]])
    print("****** Model weights ******\n",model.get_weights())
    print("****** Input samples ******\n",X_train)
    print("****** Desired Output ******\n",Y_train)
    percent_error=[]
    for k in range (20):
        model.train(X_train, Y_train, num_epochs=1, alpha=0.1)
        percent_error.append(model.calculate_percent_error(X_train,Y_train))
    print("******  Percent Error ******\n",percent_error)
    print("****** Model weights ******\n",model.get_weights())
