import os

import matplotlib
import matplotlib.pyplot as plt

import argparse as ap
import pandas as pd

parser = ap.ArgumentParser(description="Program for checking")
parser.add_argument("--bestfile", dest="best_file", type=str, required=True)
parser.add_argument("--sdfile", dest="sd_file", type=str, required=True)
parser.add_argument("--resalts", dest="resalts", type=str, required=True)

args = parser.parse_args()
# matplotlib.use("pgf")
# matplotlib.rcParams.update({
    # "pgf.texsystem": "pdflatex",
    # 'font.family': 'serif',
    # 'text.usetex': True,
    # 'pgf.rcfonts': False,
# })
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def get_value(f):
  line = f.readline()
  value = num(line.split(":")[1])
  return value

def get_vector(f):
  line = f.readline()
  strings = line.split()
  values = list(map(lambda x: float(x), strings))
  return values

def vector_to_float(vector):
  mapper = map(lambda x: float(x), vector)
  return list(mapper)

path = args.resalts

files = os.listdir(path)
batches: list = []
standard_deviations: list = []

for file in files:
    with open(f"{path}/{file}", "r") as f:
      df = pd.read_csv(f"{path}/{file}", sep="\t+", skiprows = 7)
      batch = {
      "function": (f.readline()).rstrip(),
      "iteration": get_value(f),
      "imporvisations": get_value(f),
      "hms": get_value(f),
      "hmcr": get_value(f),
      "pitch_adjust_radius": get_value(f),
      "pitch_adjust_ratio": get_value(f),
      }
      f.readline()
      batch["best"] = get_vector(f);
      df.batch_info = batch
      # print(df.batch_info)
      standard_deviations.append(df.std()["f(x,y)"])
      print(df.std()["f(x,y)"])
      batches.append(df)

# print("iteracja minimum")
# for batch in batches:
  # print(f"{batch.batch_info['iteration']} {batch.batch_info['best'][2]}")

best = map (lambda x: x.batch_info['best'][2], batches)
iteration = map(lambda x: x.batch_info["iteration"], batches)

print(standard_deviations)

best = list(best)
iterations = list(iteration)

plt.plot(iterations, best, '-o')
# plt.title("F")
plt.ylabel("Znalezione minnimumm")
plt.xlabel("numer iteracji")
plt.savefig(f'{args.best_file}.png', dpi=400)

plt.clf()
# plt.savefig('best.pgf')
# plt.close()

plt.plot(iterations, standard_deviations, '-o')
# plt.title("F")
plt.ylabel("Odchylenie standardowe f(X)")
plt.xlabel("numer iteracji")
plt.savefig(f'{args.sd_file}.png', dpi=400)
# plt.savefig('best.pgf')