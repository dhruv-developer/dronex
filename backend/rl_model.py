import pickle

with open("./rl_model.pkl", "rb") as f:
    rl_model = pickle.load(f)

def plan_mission(data):
    return rl_model.predict(data)
