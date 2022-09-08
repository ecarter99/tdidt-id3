import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('FullDataset2022-07-28.csv')

#4 potential targets:
#Suicide Considered, Suicide Desire, Suicide Intention, Suicide Resist, Suicide Last Half Hour
#All suicide questions should be removed from the table before training

evening_survey = df.loc[:, ('IDKey', 'DateKey', 'UserID_E', 'ResponseID_E', 'StartDate_E', 'StartTime_E', 'SubmitTime_E',
 'TimeZone_E', 'TriggerID_E', 'TriggerDate_E', 'TriggerTime_E', 'OS_E', 'Location_E', 'EnergyLevels', 'Motivation',
  'Productivity', 'FeltIll', 'FoodHealthiness', 'PhysicalActivity', 'LeisurePhysicalMinutes', 'NegFeelings',
   'ReduceNegFeelings', 'PosFeelings', 'IncreasePosFeelings', 'EnjoyTheMoment', 'NotShowFeelings', 'AcceptedFeeling',
    'SelfFault', 'ChangedThoughts', 'RemindFeelingsDontLast', 'StressedLog', 'StressedScore', 'StressManage', 'StressInterfere',
     'PeopleInteractionFace', 'PeopleInteractionDigital', 'ConnectFaceScore', 'ConnectDigitalScore', 'DesireSpendTime',
      'HowSupportedFelt', 'SpiritualConnection', 'NumNaps', 'ElapsedNapTotal', 'StartDatetime_E', 'ElapsedSurveySecs_E',
       'MetricwireID', 'FinishedLog', 'Group', 'VisitsCompleted', 'Age', 'Sex', 'IQ', 'Race')]

target_considered_E = df.loc[:, ('SuicideConsidered_E')]
target_inteneded_E = df.loc[:, 'SuicideIntention_E']
target_desired_E = df.loc[:, 'SuicideDesire_E']
target_resist_E = df.loc[:, 'SuicideResist_E']
target_halfhour_E = df.loc[:, 'SuicideLastHalfHour_E']
target_composite_E = df.loc[:, ('SuicideComposite_E')]

morning_survey = df.loc[:, ('IDKey', 'DateKey', 'UserID_M', 'ResponseID_M', 'StartDate_M', 'StartTime_M', 'SubmitTime_M',
 'TimeZone_M', 'TriggerID_M', 'TriggerDate_M', 'TriggerTime_M', 'OS_M', 'Location_M', 'TimeToBed', 'ElapsedSleepWait',
  'NumWokeUp', 'ElapsedWokeUp', 'NightmareLog', 'NightmareScore', 'TimeAwake', 'ElapsedSleepTotal', 'SleepQuality',
   'StartDatetime_M', 'ElapsedSurveySecs_M', 'MetricwireID', 'FinishedLog', 'Group', 'VisitsCompleted', 'Age', 'Sex', 'IQ', 'Race')]

target_considered_M = df.loc[:, ('SuicideConsidered_M')]
target_inteneded_M = df.loc[:, 'SuicideIntention_M']
target_desired_M = df.loc[:, 'SuicideDesire_M']
target_resist_M = df.loc[:, 'SuicideResist_M']
target_halfhour_M = df.loc[:, 'SuicideLastHalfHour_M']
target_composite_M = df.loc[:, ('SuicideComposite_M')]

phone_data = df.loc[:, ('IDKey', 'DateKey', 'Date', 'Creativity', 'Education', 'Entertainment', 'Information_Reading',
 'Productivity_Finance', 'Social', 'Travel', 'Utilities', 'Shopping_Food', 'Other', 'Games', 'Health and Fitness', 'OS')]

le = preprocessing.LabelEncoder()
#each column may need its own label encoder?
#consider looping through df and making an encoder for each one and storing in a dict