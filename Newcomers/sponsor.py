import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

df = pd.read_csv(r'/home/coho/Desktop/Work/Newcomers/Newcomers Survey.csv', error_bad_lines=False, engine='python',
                 sep=',')

new_df = df[~df['Unit'].str.contains('Other')]

sponsor_by_unit_yes = new_df.fillna(0).groupby(['Unit'])[
    'We strive for a smooth integration process so you and your family receive the information you need before ' \
    'reaching JBLM. Did your sponsor contact you before you arrived?'].apply(lambda x: x[x.str.contains(
        'Yes', na=False)].count())

sponsor_by_unit_no = new_df.fillna(0).groupby(['Unit'])[
    'We strive for a smooth integration process so you and your family receive the information you need before ' \
    'reaching JBLM. Did your sponsor contact you before you arrived?'].apply(lambda x: x[x.str.contains(
        'No', na=False)].count())

# Make a plot

plot = sponsor_by_unit_no.plot(kind='bar')
plt.xlabel('Unit', fontweight='bold', color='black', fontsize='17', horizontalalignment='center')
plt.ylabel('# Without Sponsor Contact', fontweight='bold', color='black', fontsize='17', horizontalalignment='center')
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()
plt.show()

