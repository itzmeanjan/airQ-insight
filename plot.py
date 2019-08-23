#!/usr/bin/python3

from functools import reduce
from datetime import datetime
from os.path import join
try:
    import matplotlib.pyplot as plt
    from matplotlib.dates import DateFormatter, HourLocator
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)

'''
    A utility method ( which you're not supposed to directly invoke externally ),
    for plotting **time vs. processed pollutant reading** data, and finally exporting
    to a `./data/*.svg` file, for further usage
'''


def __plotter__(x_axis, y_axis_min, y_axis_max, y_axis_avg, label, pollutantId, target_path):
    try:
        with plt.style.context(('ggplot')):
            # common font style
            font = {
                'family': 'serif',
                'color': '#264040',
                'weight': 'normal',
                'size': 12
            }
            # A figure of size 2400x1200
            plt.figure(figsize=(24, 12), dpi=100)
            # along x-axis date formatter e.g. `Mon 12:00 PM`
            plt.gca().xaxis.set_major_formatter(DateFormatter('%a %I:%M %p'))
            # data collected in hourly fashion, so we need hourly locator,
            # which will place ticks along x-axis seperated by 1 hour timespan
            plt.gca().xaxis.set_major_locator(HourLocator())
            # here we're first plotting data using a single line syntax and
            # then returned list of handles are used for drawing legend of graph
            plt.legend(plt.plot(x_axis, y_axis_min, 'b-',
                                x_axis, y_axis_avg, 'g-', x_axis, y_axis_max, 'r-', lw='1'), ('Minimum Reading', 'Average Reading', 'Maximum Reading'))
            # x-axis label setter
            plt.xlabel('Time', fontdict=font, labelpad=16)
            # y-axis label setter
            plt.ylabel('{} Reading'.format(pollutantId),
                       fontdict=font, labelpad=16)
            # sets title of graph
            plt.title('{} at {}'.format(
                pollutantId, label), fontdict=font)
            # asks matplotlib to autoformat dates placed along x-axis
            plt.gcf().autofmt_xdate()
            # asks matplotlib to save a copy of generated graph into a target file
            # which is `./data/*.svg`, and uses tight fitting
            plt.savefig(target_path, bbox_inches='tight', pad_inches=.5)
            # closes this figure, otherwise it may lead to huge memory usage
            plt.close()
        return True
    except Exception:
        return False


'''
    Takes all data collected over last 24 hours time period for a certain place,
    i.e. a monitoring station, and classifies all readings for different pollutant(s),
    in ascending order which is then vectorized using numpy array 
    ( so that manipulation becomes easier )

    Then for every `pollutantId`, we plot a **time vs. pollutant reading**
    graph using collected data of last 24 hour(s), which is eventually 
    exported into a `*.svg` file, for further usage, place in `./data` directory

    Input parameter `dataObject` is generally an instance of `model.categorizedData.Station`
    class, holding all data collected over last 24 hour time period from this
    monitoring station
'''


def plotIt(dataObject, target_path):
    try:
        # label consists of comma seperated station name, city, state & country
        label: str = '{}, {}, {}, {}'.format(
            dataObject.name, dataObject.city, dataObject.state, dataObject.country)
        # classifying data as per different pollutant type ( by id ), is done here
        # and returned iterator is used to iterate over each of them, and that is passed
        # to __plotter__(), which plots dataset for a certain pollutant type ( for this specific monitoring station )
        for k, v in dict(reduce(lambda acc, cur: reduce(lambda accInner, curInner: dict([(i, j) for i, j in accInner.items()] + [(curInner.pollutantId, accInner.get(curInner.pollutantId, []) + [(cur[0], curInner.pollutantMin, curInner.pollutantMax, curInner.pollutantAvg)])]),
                                                        cur[1], acc), dataObject.pollutionStat, {})).items():
            # we need it to be in descending order
            # converted to numpy array, so that it can be
            # manipulated easily i.e. picking up from a certain column
            data = plt.np.array(sorted(v, key=lambda e: e[0]))
            __plotter__(list(map(lambda e: datetime.fromtimestamp(
                e), data[:, 0])), data[:, 1], data[:, 2], data[:, 3], label, k, join(target_path, '{}_{}.svg'.format('_'.join(map(lambda e: e.strip(), label.split(','))), k)))
        else:
            return True
    except Exception:
        return False


if __name__ == "__main__":
    print('[!]This method is expected to be used as a backend handler')
