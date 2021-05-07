import pandas as pd

survey_data_df = pd.read_csv(r'/home/coho/Desktop/Work/Discussion_Survey_Analysis.csv')

total_response_by_unit = survey_data_df.fillna(0).groupby(['Unit'])['Timestamp'].count()

# print(survey_data_df)

declination_response_by_unit = survey_data_df.fillna(0).groupby(['Unit'])[
    'What are you taking away from the vaccine discussion?'].apply(lambda x: x[x.str.contains(
        'This did not change my mind, I am not getting it', na=False)].count())

percent = (declination_response_by_unit / total_response_by_unit) * 100

total = pd.concat([total_response_by_unit, declination_response_by_unit, percent], keys=['Total Participants',
                                                                                         'Stubborn Participants',
                                                                                         'Percent'], axis=1)


# print(percent_by_unit)
print(total)
total.to_csv('../Desktop/not_getting_vaccine.csv', sep=',')
# print(total_response_by_unit)


