import matplotlib.pyplot as plt

def millions(x, pos):
    return f'{x*1e-6:1.1f}M'

def generate_bar_char(name, labels, values):
  fig, ax = plt.subplots()
  ax.yaxis.set_major_formatter(millions)
  ax.bar(labels,values)
  plt.savefig(f'/home/lago/py-project/app/img/bar{name}.png')
  plt.close()
def generate_pie_bar(name,labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  plt.savefig(f'/home/lago/py-project/app/img/pie{name}.png')
  plt.close()