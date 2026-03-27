from src.preprocess import load_and_preprocess
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.utils import plot_history

def main():

    X_train, X_val, X_test, y_train, y_val, y_test = load_and_preprocess()

    model = build_model()

    history = train_model(model, X_train, y_train, X_val, y_val)

    plot_history(history)

    evaluate_model(model, X_test, y_test)

    model.save("outputs/fnn_mnist_model.h5")

if __name__ == "__main__":
    main()