import pickle

with open("./aco_model.pkl", "rb") as f:
    aco_model = pickle.load(f)

def optimize(data):
    return aco_model.predict(data)
