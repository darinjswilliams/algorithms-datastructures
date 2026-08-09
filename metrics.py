import math

class Metrics:

    @staticmethod
    def mean_squared_error(y_true, y_pred) -> float:
        """
        Compute the mean squared error between two lists of numbers, y_true and y_pred. The mean squared error is defined as the average of the squared differences between corresponding 
        elements in the two lists.

        return the mean squared error as a single float value. If the input lists have different lengths, raise a ValueError.
        """
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length.")

        squared_diffs = [(t - p) ** 2 for t, p in zip(y_true, y_pred)]
        mse = sum(squared_diffs) / len(squared_diffs)
        return mse


    @staticmethod
    def mean_absolute_error(y_true, y_pred) -> float:
        """
        Mean Absolute Error (MAE) is a measure of the average magnitude of errors between two lists of numbers, y_true and y_pred. 
        It is calculated as the average of the absolute differences between corresponding elements in the two lists.
        """
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length.")
        
        absolute_diffs = [abs(t-p) for t, p in zip (y_true, y_pred)]
        mae = sum(absolute_diffs) / len(absolute_diffs)

        return mae
    

    @staticmethod
    def root_mean_squared_error(y_true, y_pred) -> float:
        """
        Root Mean Squared Error (RMSE) is a measure of the average magnitude of errors between two lists of numbers, y_true and y_pred. 
        It is calculated as the square root of the average of the squared differences between corresponding elements in the two
        """
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length.")
        squared_diffs = [(t-p) ** 2 for t, p in zip(y_true, y_pred)]
        mse = sum(squared_diffs) / len(squared_diffs)
        rmse = mse ** 0.5
        return rmse
    

    @staticmethod
    def cosine_similarity(vec1, vec2) -> float:
        """
        compute cosine similarity between two vectors represented as lists of numbers. 
        The cosine similarity is defined as the dot product of the two vectors divided by the product of their magnitudes.

        return the cosine similarity as a single float value. If the input vectors have different lengths, raise a ValueError.
        """
        if len(vec1) != len(vec2):
            raise ValueError("Input vectors must have the same length.")
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude_vec1 = sum(a ** 2 for a in vec1) ** 0.5
        magnitude_vec2 = sum(b ** 2 for b in vec2) ** 0.5
        
        if magnitude_vec1 == 0 or magnitude_vec2 == 0:
            return 0.0
        
        cosine_sim = dot_product / (magnitude_vec1 * magnitude_vec2)
        return cosine_sim


    @staticmethod
    def cosine_similarity_v2(vec1, vec2) -> float:
        if len(vec1) != len(vec2):
            raise ValueError("Input vectors must have the same length.")
        
        dot = 0.0
        mag1 = 0.0
        mag2 = 0.0
        
        for a, b in zip(vec1, vec2):
            dot += a * b
            mag1 += a * a
            mag2 += b * b
        
        if mag1 == 0.0 or mag2 == 0.0:
            return 0.0
    
        return np.dot / ((mag1 * mag2) ** 0.5)

    

    @staticmethod
    def r2_score(y_true, y_pred) -> float:
        """
        R2 Coefficient of Determination is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s). 
        It is calculated as 1 minus the ratio of the residual sum of squares (SS_res) to the total sum of squares (SS_tot). The formula is:
        """
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length.")
        
        mean_y = sum(y_true)/len(y_true)

        ss_res = sum((t_true - t_pred) ** 2 for t_true, t_pred in zip(y_true, y_pred))
        ss_tot = sum((t_true - mean_y)  ** 2 for t_true in y_true)

        if ss_tot == 0:
            return 0.0 

        return 1 - (ss_res / ss_tot)
    


    @staticmethod
    def binary_cross_entropy(y_true, y_pred, eps=1e-15) -> float:
        """
        Compuate binary cross entropy loss between two lists of numbers, y_true and y_pred. The binary cross entropy loss is defined as:
        BCE = - (1/n) * Σ [y_true[i] * log(y_pred[i]) + (1 - y_true[i]) * log(1 - y_pred[i])]
        Note: y_pred values should be clipped to avoid taking the log of 0 or 1.
        """
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length.")
        
        total = 0.0

        for t, p in zip(y_true, y_pred):
            p = max(min(p, 1 - eps), eps)
            total += -(t * math.log(p) + (1 - t) * math.log(1 - p))

        return total / len(y_true)
    

    @staticmethod
    def adjusted_r2(y_true, y_pred, n_features):
        """
        Compute the Adjusted R-squared (Adjusted R²) score using pure Python.

        Adjusted R² penalizes the addition of unnecessary features and is defined as:

            Adjusted R² = 1 - (1 - R²) * (n - 1) / (n - p - 1)

        where:
            n = number of samples
            p = number of features (predictors)
            R² = coefficient of determination

        Parameters
        ----------
        y_true : list of float
            Actual target values.
        y_pred : list of float
            Predicted target values.
        n_features : int
            Number of features (p) used in the model.

        Returns
        -------
        float
            The Adjusted R² score.
        """
        n = len(y_true)

        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

        # Compute R² manually
        mean_y = sum(y_true) / len(y_true)
        ss_total = sum((yt - mean_y) ** 2 for yt in y_true)
        ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))

        # Handle edge case: no variance in y_true
        if ss_total == 0:
            return 0.0

        # Compute R2
        r2 = 1 - (ss_res / ss_total)

        # Compute Adjusted R²
        if n_features >= n - 1:
            raise ValueError("n_features must be less than n - 1 for Adjusted R²")

        adj_r2 = 1 - (1 - r2) * (n - 1) / (n - n_features - 1)
        return adj_r2
    
    @staticmethod   
    def accuracy_score(y_true, y_pred):
        """
        Calculate the classification accuracy between true labels and predicted labels.

        Accuracy is defined as the proportion of predictions that match the true labels:
            accuracy = correct_predictions / total_predictions

        Parameters
        ----------
        y_true : list
            A list of ground‑truth labels.
        y_pred : list
            A list of predicted labels. Must be the same length as y_true.

        Returns
        -------
        float
            The accuracy value between 0 and 1. Returns 0 if the input lists are empty.

        Notes
        -----
        - This implementation uses only pure Python (no NumPy).
        - If y_true and y_pred have different lengths, only the overlapping pairs
        are compared (based on zip).
        """
        correct = 0
        total = len(y_true)

        for yt, yp in zip(y_true, y_pred):
            if yt == yp:
                correct += 1

        return correct / total if total > 0 else 0


    @staticmethod
    def precision_score(y_true, y_pred, positive_label=1):
        """
        Precision is defined only for one specific class—the class you consider the “positive” outcome.
        In binary classification, you usually have two labels, for example:
        1 = positive
        0 = negative
        But your labels might also be:
        "spam" vs "not_spam"
        "cat" vs "dog"
        5 vs 7 
        """
        tp = 0
        fp = 0
        
        for yt, yp in zip(y_true, y_pred):
            if yp == positive_label:
                if yt == yp:
                    tp += 1
                else:
                    fp += 1
        
        if tp + fp == 0:
            return 0  # avoid division by zero
        
        return tp / (tp + fp)
    
    
    @staticmethod
    def recall(y_true, y_pred):
        """
        Compute recall = TP / (TP + FN)

        y_true: iterable of true labels (0 or 1)
        y_pred: iterable of predicted labels (0 or 1)
        """
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

        tp = 0  # true positives
        fn = 0  # false negatives

        for t, p in zip(y_true, y_pred):
            if t == 1 and p == 1:
                tp += 1
            elif t == 1 and p == 0:
                fn += 1

        if tp + fn == 0:
            return 0.0  # or float('nan'), depending on your convention

        return tp / (tp + fn)
    
    @staticmethod
    def f1_score(y_true, y_pred):
        """
        Compute F1-score = 2 * (precision * recall) / (precision + recall)

        y_true: iterable of true labels (0 or 1)
        y_pred: iterable of predicted labels (0 or 1)
        """
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

        tp = fp = fn = 0

        for t, p in zip(y_true, y_pred):
            if p == 1 and t == 1:
                tp += 1
            elif p == 1 and t == 0:
                fp += 1
            elif p == 0 and t == 1:
                fn += 1

        # Avoid division by zero
        if tp == 0:
            return 0.0

        precision = tp / (tp + fp)
        recall = tp / (tp + fn)

        return 2 * (precision * recall) / (precision + recall)

    @staticmethod
    def euclidean_distance(p, q):
        """
        Compute the Euclidean distance between two points p and q.
        Points must be iterables of equal length (e.g., lists or tuples).

        Parameters:
            p (iterable): First point (e.g., [x1, y1, z1])
            q (iterable): Second point (e.g., [x2, y2, z2])

        Returns:
            float: The Euclidean distance between p and q.
        """
        if len(p) != len(q):
            raise ValueError("Points must have the same dimension")

        total = 0
        for a, b in zip(p, q):
            diff = a - b
            total += diff * diff

        return total ** 0.5


class LinearRegressionGDPurePython:
    """
    Linear Regression (Batch Gradient Descent) — Pure Python
    """
    def __init__(self, learning_rate: float = 0.1, n_iters: int = 1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])

        # Initialize weights and bias
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.n_iters):
            # Compute predictions
            y_pred = [self._predict_row(row) for row in X]

            # Compute gradients
            dw = [0.0] * n_features
            db = 0.0

            for i in range(n_samples):
                error = y_pred[i] - y[i]
                db += error
                for j in range(n_features):
                    dw[j] += error * X[i][j]

            # Average gradients
            db /= n_samples
            dw = [d / n_samples for d in dw]

            # Update parameters
            self.bias -= self.lr * db
            self.weights = [w - self.lr * d for w, d in zip(self.weights, dw)]

    def _predict_row(self, row):
        # Dot product + bias
        return sum(w * x for w, x in zip(self.weights, row)) + self.bias

    def predict(self, X):
        return [self._predict_row(row) for row in X]


import numpy as np

class LinearRegressionGD:
    def __init__(self, learning_rate: float = 0.1, n_iters: int = 1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Number of samples and features
        X = np.array(X)
        y = np.array(y)
        
        n_samples, n_features = X.shape

        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        # Gradient descent
        for _ in range(self.n_iters):
            # Predictions: y_hat = Xw + b
            y_pred = np.dot(X, self.weights) + self.bias

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


if __name__ == "__main__":
    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    print("Mean Squared Error:", Metrics.mean_squared_error(y_true, y_pred))
    print("Mean Absolute Error:", Metrics.mean_absolute_error(y_true, y_pred))
    print("Root Mean Squared Error:", Metrics.root_mean_squared_error(y_true, y_pred))
    print("R2 Score:", Metrics.r2_score(y_true, y_pred))
    print("Adjusted R2 Score:", Metrics.adjusted_r2(y_true, y_pred, n_features=2))
    y_true_binary = [1, 0, 1, 1]
    y_pred_binary = [0.9, 0.1, 0.8, 0.7]
    print("Binary Cross Entropy:", Metrics.binary_cross_entropy(y_true_binary, y_pred_binary))
    y_true_class = [1, 0, 1, 1]
    y_pred_class = [1, 0, 0, 1]
    print("Accuracy Score:", Metrics.accuracy_score(y_true_class, y_pred_class))
    print("Precision Score:", Metrics.precision_score(y_true_class, y_pred_class))
    print("Cosine Similarity:", Metrics.cosine_similarity([1, 0, 0], [0, 1, 0]))
    print("Euclidean Distanc", Metrics.euclidean_distance([3, 4], [0, 0]))  # 5.0
    print("Euclidean Distance", Metrics.euclidean_distance([1, 2, 3], [4, 5, 6]))  # 5.196...


