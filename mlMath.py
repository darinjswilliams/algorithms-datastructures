import numpy as np
from numpy.typing import NDArray
import math

class Solution:
    
    ## Gradient Descent
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        """
        put:

        iterations - how many gradient descent steps to execute. Can be zero (meaning return the initial value unchanged). iterations >= 0.
        learning_rate - the step-size multiplier 
        α
        α that scales each gradient update. Strictly between 0 and 1.
        init - the starting point for optimization. Can be any number (including zero) 
        
        return: the value of x that minimizes f(x) after performing the specified number of iterations of gradient descent, rounded to 5 decimal places.
        """
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return init
        
        current_val = init

        for _ in range(iterations):
            gradient = 2 * current_val  # calculate gradient
            current_val -= learning_rate * gradient 

        return round(current_val, 5)
    
       
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        Activation functions are what give neural networks the ability to learn complex patterns. Without them, 
        a neural network is just a series of linear transformations.
        No matter how many layers you stack, the output would still be a linear function of the input.
        
        Sigmoid: Squishes any input to a value between 0 and 1. Used for probabilities and binary classification.
        return: a 1D NumPy array where each element is the sigmoid of the corresponding element in z, rounded to 5 decimal places.
        
        """
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        current_val = 1 / (1 + np.exp(-z))

        return np.round(current_val, 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        ReLU (Rectified Linear Unit): Returns 0 for negative inputs and the input itself for positive values. The formula is: 
        ReLU(z) = max(0, z)
        ReLU is widely used in hidden layers of neural networks because it helps mitigate the vanishing gradient problem and allows for faster training. It introduces non-linearity while being computationally efficient.
        return: a 1D NumPy array where each element is the ReLU of the corresponding element in z, rounded to 5 decimal places.
        """
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        current_val = np.maximum(0, z)
        return np.round(current_val, 5)
                        
                        
    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        Softmax converts a vector of raw scores (called logits) into a probability distribution. 
        The output values are all positive and sum to 1, making them interpretable as probabilities.

        This is how models like GPT decide which token comes next. The final layer outputs a score for every possible token, 
        and softmax turns those scores into probabilities.
            
        return: a 1D NumPy array where each element is the softmax of the corresponding element in z, rounded to 4 decimal places.
        """
            
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_z =  np.max(z)
        exp_z = np.exp(z - max_z)

        results = exp_z/np.sum(exp_z)

        return np.round(results, 4)

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        if len(y_true) != len(y_pred):
            raise ValueError("Length of input arrays are not same length")

        tot = 0
        eps = 1e-7

        for t, p in zip(y_true, y_pred):
            p = max(min(p, 1-eps), eps)
            tot += -(t * math.log(p) + (1-t) * math.log(1-p))

        results = tot/len(y_true)

        return round(results, 4)

        

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        """
        Softmax gives you probabilities, the model's confidence for each class. But how do you tell the model how wrong it was? That's what cross-entropy loss does. It compares the predicted distribution to the actual answer and produces a single number: high when the model is confidently wrong, low when it's right.
        This is the loss function behind almost every classifier and every token prediction in GPT.
    
        """
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)

        eps = 1e-7

        log_preds = np.log(np.clip(y_pred, eps, 1-eps))
        loss = -np.sum(y_true * log_preds) / len(y_true)
        return round(float(loss), 4)
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        """
            Linear regression is the "Hello World" of machine learning, and it turns out to be
            a single neuron without an activation function.
        """
        
        # Compute Y_hat = X @ W (matrix multiplication)
        # X is (n, 3), weights is (3,) -> result is (n,) predictions
        # Return np.round(result, 5)
        y_hat = X @ weights

        return np.round(y_hat, 5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute MSE = mean((predictions - truth)^2)
        # Use np.mean() and np.square()
        # Return round(result, 5)
        mse = [(t-p)**2 for t,p in zip(model_prediction, ground_truth)]

        mse =  sum(mse)/len(mse)

        return np.round(mse[0], 5)
    
    def leaky_relu(self, z: NDArray[np.float64], alpha: float = 0.01) -> NDArray[np.float64]:
        """
        Leaky ReLU is a variant of the ReLU activation function that allows a small, non-zero gradient when the input is negative. 
        This helps prevent the "dying ReLU" problem, where neurons can get stuck outputting zero and stop learning.
        The formula is: LeakyReLU(z) = max(0.01 * z, z)
        return: a 1D NumPy array where each element is the Leaky ReLU of the corresponding element in z, rounded to 5 decimal places.
        """
        # z is a 1D NumPy array
        # Formula: max(0.01 * z, z) element-wise
        return [ v if v >= 0 else alpha * v for v in z]
    
    def tanh(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        Tanh (hyperbolic tangent) is another activation function that squishes input values, but it maps them to a range between -1 and 1. 
        This can be useful for certain types of data where negative values are meaningful. The formula is: tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))
        return: a 1D NumPy array where each element is the tanh of the corresponding element in z, rounded to 5 decimal places.
        """
        # z is a 1D NumPy array
        # Formula: (e^z - e^(-z)) / (e^z + e^(-z)) element-wise
        exp_z = np.exp(z)
        exp_neg_z = np.exp(-z)
        tanh_z = (exp_z - exp_neg_z) / (exp_z + exp_neg_z)
        return np.round(tanh_z, 5)
    
    def tanh_pure_python(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        Tanh (hyperbolic tangent) is another activation function that squishes input values, but it maps them to a range between -1 and 1. 
        This can be useful for certain types of data where negative values are meaningful. The formula is: tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))
        return: a 1D NumPy array where each element is the tanh of the corresponding element in z, rounded to 5 decimal places.
        """
        output = []
        for v in z:
            if v >= 0:
                z = math.exp(-2 * v)
                t = (1 - z) / (1 + z)
            else:
                z = math.exp(2 * v)
                t = (z - 1) / (z + 1)
            output.append(round(t, 5))
        return output
    
    def linear_backward(X, W, b, dY):
        """
        Backpropagation is the process of computing gradients for all parameters in a neural network, starting from the output layer and moving backwards to the input layer. 
        This allows us to update the weights and biases in a way that minimizes the loss function.
        For a linear layer, the backward pass involves computing the gradients with respect to the inputs (dX), weights (dW), and biases (db) given the gradient of the loss with respect to the output (dY).
        return: dX, dW, db
        """
        # X is (n, 3), W is (3,), b is scalar, dY is (n,)
        # dX = dY @ W.T
        # dW = X.T @ dY
        # db = sum(dY)
        # Return np.round(dX, 5), np.round(dW, 5), round(db, 5)
        
        dX = dY @ W.T
        dW = X.T @ dY
        db = np.sum(dY)

        return np.round(dX, 5), np.round(dW, 5), round(db, 5)
    
    
    def linear_backward_pure_python(X, W, b, dY):
        """
        Backpropagation is the process of computing gradients for all parameters in a neural network, starting from the output layer and moving backwards to the input layer. 
        This allows us to update the weights and biases in a way that minimizes the loss function.
        For a linear layer, the backward pass involves computing the gradients with respect to the inputs (dX), weights (dW), and biases (db) given the gradient of the loss with respect to the output (dY).
        return: dX, dW, db
        """
        n = len(X)          # batch size
        d_in = len(X[0])    # input dimension
        d_out = len(W[0])   # output dimension

        # ---- dX = dY @ W.T ----
        dX = [[0.0 for _ in range(d_in)] for _ in range(n)]
        for i in range(n):
            for j in range(d_in):
                s = 0.0
                for k in range(d_out):
                    s += dY[i][k] * W[j][k]
                dX[i][j] = s

        # ---- dW = X.T @ dY ----
        dW = [[0.0 for _ in range(d_out)] for _ in range(d_in)]
        for i in range(d_in):
            for j in range(d_out):
                s = 0.0
                for k in range(n):
                    s += X[k][i] * dY[k][j]
                dW[i][j] = s

        # ---- db = sum over batch ----
        db = [0.0 for _ in range(d_out)]
        for i in range(n):
            for j in range(d_out):
                db[j] += dY[i][j]

        return dX, dW, db
    
