import pandas as pd
import numpy as np

survey_data_df = pd.read_csv(r'/home/coho/Desktop/Work/Discussion_Survey_Analysis.csv')

total_response_by_unit = survey_data_df.fillna(0).groupby(['Unit'])[['Timestamp']].count()

# print(survey_data_df)

declination_response_by_unit = survey_data_df.fillna(0).groupby(['Unit'])[
    'What are you taking away from the vaccine discussion?'].apply(lambda x: x[x.str.contains(
        'This did not change my mind, I am not getting it', na=False)].count())

percent_by_unit = pd.concat([declination_response_by_unit.value_counts(),
                             declination_response_by_unit.value_counts(normalize=True).mul(100)], axis=1, keys=(
                                'raw', 'percentage'
))

# print(percent_by_unit)
print(declination_response_by_unit)
# print(total_response_by_unit)
