import pandas as pd

df = pd.read_csv(r'/home/coho/Desktop/Work/DFAC_Survey/PX_Food_Court.csv', error_bad_lines=False, engine='python',
                 sep=',')

# Partial Matching hobbies
hiking = df['hobbies'].str.contains('hiking').sum()
fishing = df['hobbies'].str.contains('fishing').sum()
running = df['hobbies'].str.contains('running or biking').sum()
sightseeing = df['hobbies'].str.contains('sightseeing').sum()
Gym = df['hobbies'].str.contains('Gym').sum()

hobby_total = {'Hobby': ['hiking', 'fishing', 'running/biking', 'sightseeing', 'gym'],
               'Count': [hiking, fishing, running, sightseeing, Gym]
               }
df_hobby_total = pd.DataFrame(hobby_total, columns=['Hobby', 'Count'])


# Partial Matching Org Awareness
AFFAP = df['Org Awareness'].str.contains('Armed Forces Family Action Plan').sum()
FAP = df['Org Awareness'].str.contains('Family Advocacy Program (FAP)').sum()
Finance = df['Org Awareness'].str.contains('Financial Readiness & Emergency Assistance').sum()
FRC = df['Org Awareness'].str.contains('Family Resource Center').sum()
MFLC = df['Org Awareness'].str.contains('Military & Family Life Counselors').sum()
EFMP = df['Org Awareness'].str.contains('Exceptional Family Member Program').sum()
SUDDC = df['Org Awareness'].str.contains('Substance Use Disorder Clinical Care').sum()
AER = df['Org Awareness'].str.contains('Army Emergency Relief').sum()

Org_total = {
                'Organization': ['AFFAP', 'FAP', 'Finance', 'FRC', 'MFLC', 'EFMP', 'SUDDC', 'AER'],
                'Count': [AFFAP, FAP, Finance, FRC, MFLC, EFMP, SUDDC, AER]
            }

df_org_total = pd.DataFrame(Org_total, columns=['Organization', 'Count'])

# print(df_org_total)
# Best Summary Thus Far
rollup = df[['Sex', 'Own Car', 'Personality', 'Friends', 'Reenlist',
             'Drinking Habits', 'Tragic Events', 'Time Waiting',
             'Times Off Post', 'Leadership at DFAC', 'Video Games', 'Education',
             'Monthly Payments']].apply(pd.Series.value_counts)


rollup_percent = df[['Sex', 'Own Car', 'Personality', 'Friends', 'Reenlist',
                     'Drinking Habits', 'Tragic Events', 'Time Waiting',
                     'Times Off Post', 'Leadership at DFAC', 'Video Games', 'Education',
                     'Monthly Payments']].apply((lambda x: pd.Series.value_counts(x, normalize=True)))

sex_rollup = pd.concat([rollup['Sex'].dropna(), rollup_percent['Sex'].dropna()], axis=1)
sex_rollup.columns = ['Raw', 'Percent']

owncar_rollup = pd.concat([rollup['Own Car'].dropna(), rollup_percent['Sex'].dropna()], axis=1)

# print(sex_rollup)

for column in rollup:

    columnsSeriesObj = rollup[column]
    combined = pd.concat([columnsSeriesObj.values, rollup_percent], axis=1)

# Make a plot
# plot = df['Time Waiting'].value_counts().plot(kind='bar')
# plt.show()
# Option for value_counts() of all columns at once
# cleanStack = df.apply(lambda x: x.value_counts()).T.stack()

# rollup.to_csv('../Desktop/Work/DFAC_Survey/Submission/PX_Food_Court', sep=',')
# rollup_percent.to_csv('../Desktop/Work/DFAC_Survey/Submission/PX_Food_Court_percent', sep=',')
# df_hobby_total.to_csv('../Desktop/Work/DFAC_Survey/Submission/PX_Food_Court_hobby', sep=',')
# df_org_total.to_csv('../Desktop/Work/DFAC_Survey/Submission/PX_Food_Court_org', sep=',')

