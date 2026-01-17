import numpy as np
import pandas as pd
import glob
import sys
import matplotlib.pyplot as plt

r = 102303631
print(f"{r}")

a = 0.05 * (r % 7)
b = 0.3 * ((r % 5) + 1)
print(f"a={a}, b={b}")

f = glob.glob("*.csv")
if not f:
    sys.exit(1)

try:
    d = pd.read_csv(f[0])
except:
    try:
        d = pd.read_csv(f[0], encoding='latin1')
    except:
        sys.exit(1)

c = 'NO2'
if 'no2' in d.columns:
    c = 'no2'
    
x = d[c].dropna().values

z = x + a * np.sin(b * x)

m = np.mean(z)
v = np.var(z)
s = np.std(z)

l = 1 / (2 * v)
k = 1 / (s * np.sqrt(2 * np.pi))

print(f"m={m}")
print(f"l={l}")
print(f"c={k}")

plt.figure()
plt.hist(z, bins=100, density=True, alpha=0.5)
t = np.linspace(min(z), max(z), 1000)
plt.plot(t, k * np.exp(-l * (t - m)**2), 'r')
plt.savefig('res.png')
print("saved")
