import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imageio

data = pd.read_csv('SampleData.csv', 'r', delimiter = ',')


count = 59
outfile_list = []
for val in range(1,59):
    outfile = str(val) + '.png'
    datasub = data[data['rank'] >= count]
    count -= 1
    ax = datasub.plot(kind = 'line', x = 'rank', y = 'consumption', color = 'red')
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.subplots_adjust(left=0.2)
    plt.gca().invert_xaxis()
    ax.set_xlabel('account rank')
    ax.set_ylabel('kwk')
    plt.savefig(outfile)
    outfile_list.append(outfile)
    #plt.savefig('power_consumption.png')
    plt.close('all')

# make the GIF file
with imageio.get_writer('consumption.gif', mode = 'I', duration = 1) as writer:
    for filename in outfile_list:
        image = imageio.imread(filename)
        writer.append_data(image)
