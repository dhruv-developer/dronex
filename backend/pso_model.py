import pickle

with open("./pso_model.pkl", "rb") as f:
    pso_model = pickle.load(f)

def optimize(data):
    return pso_model.predict(data)
