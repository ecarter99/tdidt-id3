import pandas as pd

#4 potential targets:
#Suicide Considered, Suicide Desire, Suicide Intention, Suicide Resist, Suicide Last Half Hour
#All suicide questions should be removed from the table before training
#Person identifiers should also be removed

def get_evening(df):
   evening_survey = df.loc[:, ('Location_E', 'EnergyLevels', 'Motivation',
  'Productivity', 'FeltIll', 'FoodHealthiness', 'PhysicalActivity', 'LeisurePhysicalMinutes', 'NegFeelings',
   'ReduceNegFeelings', 'PosFeelings', 'IncreasePosFeelings', 'EnjoyTheMoment', 'NotShowFeelings', 'AcceptedFeeling',
    'SelfFault', 'ChangedThoughts', 'RemindFeelingsDontLast', 'StressedLog', 'StressedScore', 'StressManage', 'StressInterfere',
     'PeopleInteractionFace', 'PeopleInteractionDigital', 'ConnectFaceScore', 'ConnectDigitalScore', 'DesireSpendTime',
      'HowSupportedFelt', 'SpiritualConnection', 'NumNaps', 'ElapsedNapTotal', 'ElapsedSurveySecs_E', 'Age', 'Sex', 'IQ', 'Race')]

   return evening_survey

def get_target(df, column):
   """
   target_considered_E = df.loc[:, ('SuicideConsidered_E')]
   target_inteneded_E = df.loc[:, 'SuicideIntention_E']
   target_desired_E = df.loc[:, 'SuicideDesire_E']
   target_resist_E = df.loc[:, 'SuicideResist_E']
   target_halfhour_E = df.loc[:, 'SuicideLastHalfHour_E']
   target_composite_E = df.loc[:, ('SuicideComposite_E')]

   target_considered_M = df.loc[:, ('SuicideConsidered_M')]
   target_inteneded_M = df.loc[:, 'SuicideIntention_M']
   target_desired_M = df.loc[:, 'SuicideDesire_M']
   target_resist_M = df.loc[:, 'SuicideResist_M']
   target_halfhour_M = df.loc[:, 'SuicideLastHalfHour_M']
   target_composite_M = df.loc[:, ('SuicideComposite_M')]
   """
   return df.loc[:, column]

def get_morning(df):
   morning_survey = df.loc[:, ('TimeToBed', 'ElapsedSleepWait', 'NumWokeUp', 'ElapsedWokeUp', 'NightmareLog', 'NightmareScore',
   'TimeAwake', 'ElapsedSleepTotal', 'SleepQuality', 'Age', 'Sex', 'IQ', 'Race')]

   return morning_survey

def get_phone(df):
   phone_data = df.loc[:, ('Creativity', 'Education', 'Entertainment', 'Information_Reading', 'Productivity_Finance', 'Social',
   'Travel', 'Utilities', 'Shopping_Food', 'Other', 'Games', 'Health and Fitness')]