# tdidt-id3
Decision tree for data modeling, first try using scikit-learn

Sources:

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0258535#pone-0258535-g001 
- Paper from Mike Barnes, suicidality based on Utah SHARP surveys
- disucsses several models (found lightgbm as best)
- discussion on SHAP analysis

https://www.youtube.com/watch?v=-taOhqkiuIo
- deep dive into shap analysis and its uses

https://www.youtube.com/watch?v=SW3akc0ho7M
- lightgbm python tutorial

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
- Sources on scikit preprocessing for encoding values

Helps:

"'IDKey', 'DateKey', 'UserID_M', 'ResponseID_M', 'StartDate_M', 'StartTime_M', 'SubmitTime_M', 'TimeZone_M', 'TriggerID_M', 'TriggerDate_M', 'TriggerTime_M', 'OS_M', 'Location_M', 'TimeToBed', 'ElapsedSleepWait', 'NumWokeUp', 'ElapsedWokeUp', 'NightmareLog', 'NightmareScore', 'TimeAwake', 'ElapsedSleepTotal', 'SleepQuality', 'SuicideConsidered_M', 'SuicideDesire_M', 'SuicideIntention_M', 'SuicideResist_M', 'SuicideLastHalfHour_M', 'StartDatetime_M', 'ElapsedSurveySecs_M', 'SuicideComposite_M', 'UserID_E', 'ResponseID_E', 'StartDate_E', 'StartTime_E', 'SubmitTime_E', 'TimeZone_E', 'TriggerID_E', 'TriggerDate_E', 'TriggerTime_E', 'OS_E', 'Location_E', 'EnergyLevels', 'Motivation', 'Productivity', 'FeltIll', 'FoodHealthiness', 'PhysicalActivity', 'LeisurePhysicalMinutes', 'NegFeelings', 'ReduceNegFeelings', 'PosFeelings', 'IncreasePosFeelings', 'EnjoyTheMoment', 'NotShowFeelings', 'AcceptedFeeling', 'SelfFault', 'ChangedThoughts', 'RemindFeelingsDontLast', 'StressedLog', 'StressedScore', 'StressManage', 'StressInterfere', 'PeopleInteractionFace', 'PeopleInteractionDigital', 'ConnectFaceScore', 'ConnectDigitalScore', 'DesireSpendTime', 'HowSupportedFelt', 'SpiritualConnection', 'NumNaps', 'ElapsedNapTotal', 'SuicideConsidered_E', 'SuicideDesire_E', 'SuicideIntention_E', 'SuicideResist_E', 'SuicideLastHalfHour_E', 'StartDatetime_E', 'ElapsedSurveySecs_E', 'SuicideComposite_E', 'Date', 'Creativity', 'Education', 'Entertainment', 'Information_Reading', 'Productivity_Finance', 'Social', 'Travel', 'Utilities', 'Shopping_Food', 'Other', 'Games', 'Health and Fitness', 'OS', 'MetricwireID', 'FinishedLog', 'Group', 'VisitsCompleted', 'Age', 'Sex', 'IQ', 'Race', "
