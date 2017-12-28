# -*- coding: utf-8 -*-
# -*- author: nik -*-
import matplotlib.pyplot as plt

class EdaUtils:

    def __init__(self):
        pass
    def desc_data(self, data_frame):
        print("\n---------------desc data start ------------------------\n")
        print("\nObject.shape: \n", data_frame.shape)
        print("\n-----------------------------------------------\n")
        print("\nObject.describe(): \n", data_frame.describe())
        print("\n-----------------------------------------------\n")
        # print("\nObject.info(): \n", data_frame.info)
        # print("\n-----------------------------------------------\n")
        print("\nObject.head(): \n", data_frame.head())
        print("\n-----------------------------------------------\n")
        print("\nObject.tail(): \n",data_frame.tail())

        print("\n----------------desc data end-------------------------\n")

    def plot_data(self,X,Y):
        ax1 = plt.subplot(311)
        plt.plot(X,Y, label="plot")

        leg = plt.legend(loc='best', ncol=4, mode="expand", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        ax2 = plt.subplot(312)
        plt.bar(X, Y, label="bar")

        ax3 = plt.subplot(313)
        plt.scatter(X,Y)
        plt.show()

