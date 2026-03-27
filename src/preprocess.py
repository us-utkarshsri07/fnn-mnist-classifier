from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def load_and_preprocess():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Normalize
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    # Split validation
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.1, random_state=42
    )

    # One-hot encoding
    y_train = to_categorical(y_train, 10)
    y_val = to_categorical(y_val, 10)
    y_test = to_categorical(y_test, 10)

    return X_train, X_val, X_test, y_train, y_val, y_test