import pandas as pd
import matplotlib.pyplot as plt
def load_and_plot(path='data/data_energy.csv'):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    df.set_index('timestamp', inplace=True)
    df['power_kW'].plot(title='Hourly Power (kW)', figsize=(12,4))
    plt.savefig('outputs/energy_timeseries.png')
    print('Saved outputs/energy_timeseries.png')
if __name__=='__main__':
    import os; os.makedirs('outputs', exist_ok=True)
    load_and_plot()
