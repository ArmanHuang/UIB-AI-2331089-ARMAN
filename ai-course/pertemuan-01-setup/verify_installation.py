# verify_installation.py
import sys
import importlib

packages = ["numpy", "pandas", "sklearn", "skfuzzy", "cv2", "matplotlib", "nltk"]

for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        print(f"{pkg}: OK, version = {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"{pkg}: ERROR → {e}")

print("Python:", sys.version)


import sys, numpy as np, pandas as pd, sklearn, skfuzzy, cv2

print("Python:", sys.version)
print("numpy:", np.__version__)
print("pandas:", pd.__version__)
print("sklearn:", sklearn.__version__)
print("skfuzzy:", skfuzzy.__version__)
print("opencv:", cv2.__version__)

print ("Python:", sys.version)  
