import pandas as pd

df = pd.read_csv(r'/home/coho/Desktop/Work/92G_survey.csv', error_bad_lines=False, engine='python',
                 sep=',')
filtered_df = df[df['In which Warrior Restaurant do you work?'].str.contains('Courage Inn', case=False)]
count = filtered_df[['Gender',
                     'Age',
                     'Rank',
                     'Which label describes you best?',
                     'Do you have friends from your restaurant that you spend time with outside of work?',
                     'How often do you leave base per week?',
                     'What recreational activities do you do off post? (Choose which is most applicable to you)',
                     'Do you anticipate reenlisting?',
                     'Do you feel like you are a part of your Squad - part of the team?',
                     'Do you feel like you are part of your Company - part of the team?',
                     'Do you feel like you are a part of your Battalion - part of the team?',
                     'On a scale of 1-5, rate your current level of job satisfaction.',
                     'If you had to choose one from the list below, which way can your command best support you?',
                     'What is your biggest concern / issue with your job as a Chef? (Choose what best describes your feelings)',
                     'Do you plan to get the Covid vaccine?',
                     'If you could make one change to the Warrior Restaurant, what would it be?',
                     'Have you been the victim of a sexual assault in the last 90 days?',
                     'When do you most often see leadership eating at your Warrior Restaurant? (PL/PSG and above)',
                     'In the past 90 days, have you experienced depression or had thoughts of harming yourself? '
                     '(Choose which most accurately describes you)',
                     'Do you think there is a difference between the quality of meals on weekdays vs weekends?',
                     'Before the Army, I lived in',
                     'What is your current level of education?',
                     'How many  hours a week do you spend playing video games? ',
                     'When do you play video games most?',
                     'On average, how much do you pay total per month? (Everything - rent/mortgage, car, insurance, medical bills, student loans, etc.) '
                     ]].apply(pd.Series.value_counts)

percent = filtered_df[['Gender',
                       'Age',
                       'Rank',
                       'Which label describes you best?',
                       'Do you have friends from your restaurant that you spend time with outside of work?',
                       'How often do you leave base per week?',
                       'What recreational activities do you do off post? (Choose which is most applicable to you)',
                       'Do you anticipate reenlisting?',
                       'Do you feel like you are a part of your Squad - part of the team?',
                       'Do you feel like you are part of your Company - part of the team?',
                       'Do you feel like you are a part of your Battalion - part of the team?',
                       'On a scale of 1-5, rate your current level of job satisfaction.',
                       'If you had to choose one from the list below, which way can your command best support you?',
                       'What is your biggest concern / issue with your job as a Chef? (Choose what best describes your feelings)',
                       'Do you plan to get the Covid vaccine?',
                       'If you could make one change to the Warrior Restaurant, what would it be?',
                       'Have you been the victim of a sexual assault in the last 90 days?',
                       'When do you most often see leadership eating at your Warrior Restaurant? (PL/PSG and above)',
                       'In the past 90 days, have you experienced depression or had thoughts of harming yourself? '
                       '(Choose which most accurately describes you)',
                       'Do you think there is a difference between the quality of meals on weekdays vs weekends?',
                       'Before the Army, I lived in',
                       'What is your current level of education?',
                       'How many  hours a week do you spend playing video games? ',
                       'When do you play video games most?',
                       'On average, how much do you pay total per month? (Everything - rent/mortgage, car, insurance, medical bills, student loans, etc.) '
                       ]].apply((lambda x: pd.Series.value_counts(x, normalize=True)))

gender = pd.concat([count['Gender'].dropna(), percent['Gender'].dropna()], axis=1)
age = pd.concat([count['Age'].dropna(), percent['Age'].dropna()], axis=1)
rank = pd.concat([count['Rank'].dropna(), percent['Rank'].dropna()], axis=1)
personality = pd.concat(
    [count['Which label describes you best?'].dropna(), percent['Which label describes you best?'].dropna()], axis=1)
friends = pd.concat(
    [count['Do you have friends from your restaurant that you spend time with outside of work?'].dropna(),
     percent['Do you have friends from your restaurant that you spend time with outside of work?'].dropna()], axis=1)
off_base = pd.concat([count['How often do you leave base per week?'].dropna(),
                      percent['How often do you leave base per week?'].dropna()], axis=1)
rec_activities = pd.concat(
    [count['What recreational activities do you do off post? (Choose which is most applicable to you)'].dropna(),
     percent['What recreational activities do you do off post? (Choose which is most applicable to you)'].dropna()],
    axis=1)
reenlist = pd.concat(
    [count['Do you anticipate reenlisting?'].dropna(), percent['Do you anticipate reenlisting?'].dropna()], axis=1)
squad = pd.concat([count['Do you feel like you are a part of your Squad - part of the team?'].dropna(),
                   percent['Do you feel like you are a part of your Squad - part of the team?'].dropna()], axis=1)
company = pd.concat([count['Do you feel like you are part of your Company - part of the team?'].dropna(),
                     percent['Do you feel like you are part of your Company - part of the team?'].dropna()], axis=1)
bn = pd.concat([count['Do you feel like you are a part of your Battalion - part of the team?'].dropna(),
                percent['Do you feel like you are a part of your Battalion - part of the team?'].dropna()], axis=1)
satisfaction = pd.concat([count['On a scale of 1-5, rate your current level of job satisfaction.'].dropna(),
                          percent['On a scale of 1-5, rate your current level of job satisfaction.'].dropna()], axis=1)
command_support = pd.concat(
    [count['If you had to choose one from the list below, which way can your command best support you?'].dropna(),
     percent['If you had to choose one from the list below, which way can your command best support you?'].dropna()],
    axis=1)
concern = pd.concat([count[
                         'What is your biggest concern / issue with your job as a Chef? (Choose what '
                         'best describes your feelings)'].dropna(),
                     percent[
                         'What is your biggest concern / issue with your job as a Chef? (Choose what '
                         'best describes your feelings)'].dropna()],
                    axis=1)
covax = pd.concat([count['Do you plan to get the Covid vaccine?'].dropna(),
                   percent['Do you plan to get the Covid vaccine?'].dropna()], axis=1)
suggestion = pd.concat([count['If you could make one change to the Warrior Restaurant, what would it be?'].dropna(),
                        percent['If you could make one change to the Warrior Restaurant, what would it be?'].dropna()],
                       axis=1)
sharp = pd.concat([count['Have you been the victim of a sexual assault in the last 90 days?'].dropna(),
                   percent['Have you been the victim of a sexual assault in the last 90 days?'].dropna()], axis=1)
leadership_dining = pd.concat(
    [count['When do you most often see leadership eating at your Warrior Restaurant? (PL/PSG and above)'].dropna(),
     percent['When do you most often see leadership eating at your Warrior Restaurant? (PL/PSG and above)'].dropna()],
    axis=1)
self_harm = pd.concat(
    [count['In the past 90 days, have you experienced depression or had thoughts of harming yourself? '
           '(Choose which most accurately describes you)'].dropna(),
     percent['In the past 90 days, have you experienced depression or had thoughts of harming yourself? '
             '(Choose which most accurately describes you)'].dropna()], axis=1)
meal_quality = pd.concat(
    [count['Do you think there is a difference between the quality of meals on weekdays vs weekends?'].dropna(),
     percent['Do you think there is a difference between the quality of meals on weekdays vs weekends?'].dropna()],
    axis=1)
live_location = pd.concat(
    [count['Before the Army, I lived in'].dropna(), percent['Before the Army, I lived in'].dropna()], axis=1)
education = pd.concat([count['What is your current level of education?'].dropna(),
                       percent['What is your current level of education?'].dropna()], axis=1)
games_hrs = pd.concat([count['How many  hours a week do you spend playing video games? '].dropna(),
                       percent['How many  hours a week do you spend playing video games? '].dropna()], axis=1)
games_habits = pd.concat(
    [count['When do you play video games most?'].dropna(), percent['When do you play video games most?'].dropna()],
    axis=1)
bills = pd.concat(
    [count[
         'On average, how much do you pay total per month? (Everything - rent/mortgage, car, insurance, medical bills, student loans, etc.) '].dropna(),
     percent[
         'On average, how much do you pay total per month? (Everything - rent/mortgage, car, insurance, medical bills, student loans, etc.) '].dropna()],
    axis=1)

gender.columns = ['Raw', 'Percent']
age.columns = ['Raw', 'Percent']
rank.columns = ['Raw', 'Percent']
personality.columns = ['Raw', 'Percent']
friends.columns = ['Raw', 'Percent']
off_base.columns = ['Raw', 'Percent']
rec_activities.columns = ['Raw', 'Percent']
reenlist.columns = ['Raw', 'Percent']
squad.columns = ['Raw', 'Percent']
company.columns = ['Raw', 'Percent']
bn.columns = ['Raw', 'Percent']
satisfaction.columns = ['Raw', 'Percent']
command_support.columns = ['Raw', 'Percent']
concern.columns = ['Raw', 'Percent']
covax.columns = ['Raw', 'Percent']
suggestion.columns = ['Raw', 'Percent']
sharp.columns = ['Raw', 'Percent']
leadership_dining.columns = ['Raw', 'Percent']
self_harm.columns = ['Raw', 'Percent']
meal_quality.columns = ['Raw', 'Percent']
live_location.columns = ['Raw', 'Percent']
education.columns = ['Raw', 'Percent']
games_hrs.columns = ['Raw', 'Percent']
games_habits.columns = ['Raw', 'Percent']
bills.columns = ['Raw', 'Percent']

# make pandas excel writer
writer = pd.ExcelWriter('../Desktop/Work/92G_survey_courage.xlsx')

# write each sheet
gender.to_excel(writer, sheet_name='gender')
age.to_excel(writer, sheet_name='age')
rank.to_excel(writer, sheet_name='rank')
personality.to_excel(writer, sheet_name='describe your personality')
friends.to_excel(writer, sheet_name='do you have friends in your unit')
off_base.to_excel(writer, sheet_name='how many times do you go off post per week')
rec_activities.to_excel(writer, sheet_name='what rec activities do you do for fun')
reenlist.to_excel(writer, sheet_name='reenlist')
squad.to_excel(writer, sheet_name='member of team in sqd')
company.to_excel(writer, sheet_name='member of team in company')
bn.to_excel(writer, sheet_name='member of team in bn')
satisfaction.to_excel(writer, sheet_name='job satisfaction (1-5)')
command_support.to_excel(writer, sheet_name='how can your command_support you')
concern.to_excel(writer, sheet_name='biggest concern')
covax.to_excel(writer, sheet_name='plan on getting covax')
suggestion.to_excel(writer, sheet_name='suggestion to improve WRs')
sharp.to_excel(writer, sheet_name='victim of sharp')
leadership_dining.to_excel(writer, sheet_name='how often do you see your leadership at WR')
self_harm.to_excel(writer, sheet_name='do you have thoughts of hurting yourself')
meal_quality.to_excel(writer, sheet_name='meal quality diff on weekdays vs weekends')
live_location.to_excel(writer, sheet_name="where'd you live before the army")
education.to_excel(writer, sheet_name='current education received')
games_hrs.to_excel(writer, sheet_name='how much video games do you play in hrs')
games_habits.to_excel(writer, sheet_name='when do you play video games most often')
bills.to_excel(writer, sheet_name='typical monthly payments')

# close pandas excel writer
writer.save()
