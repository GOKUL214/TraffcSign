import pandas as pd
import os
def importDataInfo(path):
    coloums = ['Center', 'Left', 'Right', 'Steering', 'Throttle', 'Break', 'Speed']
    data = pd.read_csv(os.path.join(path, 'driving_log.csv'), names = coloums)
    print(data.head())
