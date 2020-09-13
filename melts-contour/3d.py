import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import scipy


# 特定のSiO2量におけるデータを抽出
def get_index(silica):
    data_name = 'input_20.csv'
    data = pd.read_csv(data_name)
    data = data[ data['SiO2'] == silica ]
    index = list( data['Title'] )
    return index


# get_indexで得た値から計算結果を絞り込む
def select_data(index):
    data_name = 'result_20.csv'
    data = pd.read_csv(data_name)
    data = data[ data['Title'].isin(index) ]
    data = data.query('Plg != 0')
    x = data['Temp(C)'].values
    y = data['Pressure'].values
    z1 = data['Plg'].values
    z2 = data['volPlg'].values
    return x, y, z1, z2


def plot_comp(silica, x, y, z1):
    plt.rcParams["font.size"] = 14
    plt.tight_layout()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    scatter = ax.scatter(x, y, c=z1, marker='s', cmap='turbo', norm=Normalize(vmin=40, vmax=95))
    plt.xlabel('Temperature [$^\circ$C]')
    plt.ylabel('Pressure [bar]')
    #plt.title('SiO$_2$ = '+str(silica)+'wt%, H$_2$O = 2.0wt%')
    pp = fig.colorbar(scatter)
    pp.set_label('An [mol.%]')
    plt.xlim(900, 1200)
    plt.ylim(0, 6500)
    plt.savefig('results/plg-'+str(silica)+'.jpg', bbox_inches="tight", dpi=300)
    plt.close()
    

def main():
    for silica in range(48, 71, 1):
        index = get_index(silica)
        x, y, z1, z2 = select_data(index)
        plot_comp(silica, x, y, z1)
        

if __name__ == '__main__':
    main()