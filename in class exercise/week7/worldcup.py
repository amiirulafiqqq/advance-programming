import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


worldcupdata = pd.read_csv('kaggle kernels output vishalrsm/fifa-world-cup-2022-winner-prediction -p /path/to/dest')
worldcupdata.tail()


hometeam = worldcupdata[['date','home_team','home_team_fifa_rank']].rename(columns={'home_team':'top_team','home_team_fifa_rank':'top_rank'})
awayteam = worldcupdata[['date','away_team','away_team_fifa_rank']].rename(columns={'away_team':'top_team','away_team_fifa_rank':'top_rank'})
fifateamrank =  hometeam.append(awayteam);

fifa_rank  = fifateamrank.sort_values(['top_team', 'date'], ascending=[True, False])
fifa_rank['row_number'] = fifa_rank.groupby('top_team').cumcount()+1
fifa_rank_top = fifa_rank[fifa_rank['row_number']==1].drop('row_number',axis=1).nsmallest(20, 'top_rank')

# fifa_rank_top.head()
fifa_rank_top
