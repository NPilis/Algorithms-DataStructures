
class Series:

    def __init__(self, series):
        self.series = series

    def insertionSort(self):
        for i in range(1,len(self.series)):
            while i > 0 and self.series[i] < self.series[i-1]:
                self.series[i-1], self.series[i] = self.series[i], self.series[i-1]
                i -= 1
