import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visual_scan_result(file_path):
    df = pd.read_csv(file_path)
    df = df[['name', 'title', 'type']]
    title_counts = df['title'].value_counts()
    title_type = df['type'].value_counts()
    print(title_counts)
    print("==========================")
    print(title_type)

if __name__ == '__main__':
    visual_scan_result('./scan_result/eth_exchange.csv')