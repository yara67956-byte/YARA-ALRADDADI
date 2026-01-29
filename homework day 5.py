import json
from pathlib import Path
config={
   "model": {"name": "LogisticRegression"},
   "training": {
       "batch_size": 32,
       "epochs": 10,
       "learning_rate": 0.001
   }
}
with open ("config.json","w")as f: 
    json.dump(config, f, indent=4)


with open("config.json", "r") as f:
    config = json.load(f)

print(config)


results = {"accuracy": 0.95, "loss": 0.05}

try:
    with open("results.json","w") as f:
        json.dump(results, f, indent=4)
        print("yara")
except Exception as e :
    print(f'Error saving results')

    