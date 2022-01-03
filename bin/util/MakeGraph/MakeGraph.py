import matplotlib.pyplot as plt
from random import randrange
from typing import Union
import configparser

class MakeGraph:
    '''This class  makes graphs.'''

    def __init__(self,
                 data: dict) -> None:

        # Info from second graph
        self.graph_data = data[0]

        # Info from first grpah
        self.graph_args = data[1]['arguments']
        self.graph_name = data[1]['name']

        # Configuration
        self.__CONFIG_PATH = 'util\\config\\config.ini'

        self.line_plot_path = self.get_line_plot_path()

        # Graph Settings
        self.style = 'fivethirtyeight'

        self.fig_size = (22, 10)


    def smart_settings(self,
                       x_axis: Union[list, tuple]) -> None:
        '''
            This function finds the best settings
            for our line plot.

            We need to find the x axis label sizes
            because it would be undreadable if the
            labels were too large.
        '''
        # Plot Style
        plt.style.use(self.style)

        # Find the size of the x axis labels
        if len(x_axis) > 55:
            plt.rcParams['xtick.labelsize'] = 8
            plt.figure(figsize = (25, 10))

        else:
            plt.rcParams['xtick.labelsize'] = 12
            plt.figure(figsize = (17, 8))


    def find_axis(self) -> tuple:
        '''
            This function finds the y axis & x axis.
            We also reverse the y axis because we
            recive it in the wrong order.
        '''
        y_axis = self.graph_args[0]
        y_axis = self.graph_data[y_axis]

        y_axis.reverse()

        x_axis = [str(arg) for arg in range(len(y_axis))]

        return (y_axis, x_axis)


    def line_plot(self) -> None:
        '''This function makes line plots'''
        # Find Axis
        y_axis, x_axis = self.find_axis()

        # Get y label
        y_label = self.graph_args[0]

        # Get best settings
        self.smart_settings(x_axis)

        # Make Plot
        plt.plot(x_axis, y_axis, '.-',
                 color='#f95d6a', linewidth=1.4,
                 label=y_label, alpha=0.9)

        # ASSIGN Plot Labels, Grid & Legend
        plt.xlabel('Games')
        plt.ylabel(y_label)
        
        plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2)

        route = f'{self.line_plot_path}{randrange(1, 30)}'
        plt.savefig(route)

        plt.show()


    def get_line_plot_path(self) -> str:
        '''
            This function returns the path for the
            line plot folder from the config.ini
            file.
        '''
        config = configparser.ConfigParser()
        config.read(self.__CONFIG_PATH)

        line_plot_path = config['paths']['line_plot']

        return line_plot_path
