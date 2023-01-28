import pandas as pd
import dataframe_image as dfi
import numpy as np
from datetime import date

class dataGen:

    def __init__(self, data) -> None:
        self.data = data
        self.cols = {'name' : 'Name',
                    'mmr' : 'MMR',
                    'wins' : 'Wins',
                    'losses' : 'Losses',
                    'totalgames' : 'Total Games',
                    'streak' : 'Streak'
                    }
        self.styles = styles = [dict(selector='th', props=[('text-align', 'center'), ('background-color', '#001254'), ('color', '#fff')]),
                                {'selector' : '', 'props' : [('border', '1px solid black')]}]
        
    def generateTable(self):
        df = pd.DataFrame.from_dict(self.data)
        y = df['alltime']
        y = y.to_dict()
        data = pd.DataFrame.from_dict(y)
        table = data.transpose()
        table_data = pd.DataFrame.from_dict(table['data'])
        table_data = pd.json_normalize(table_data['data'])
        table = table.join(table_data)
        table = table.sort_values(by = 'mmr', ascending=False)
        data_df = table.head(10)
        data_df.rename(columns=self.cols, inplace=True)
        data_df = data_df.reset_index()
        data_df = data_df.reset_index()
        data_df.rename(columns={'level_0' : 'Rank'}, inplace=True)
        data_df['Rank'] += 1
        data_df = data_df.drop(['index', 'rank', 'id', 'data'], axis = 1)
        df_styled = data_df.style.format({'MMR' : '{:20.2f}'}).hide_index().set_properties(subset=data_df.columns, **{'text-align': 'center'}).set_properties(subset=data_df.columns, **{'width': '60px', 'height': '10px'}).set_table_styles(self.styles).background_gradient(cmap='Blues')
        dfi.export(df_styled, 'table.png', table_conversion='chrome')
        return df_styled

    @staticmethod
    def messages():
        today = date.today()
        today = today.strftime('%B %d, %Y')
        leaderboard_tweets = [
            "The ProCity leaderboard is heating up! Check out today's top 10 players and their stats.", 
            "Who will take the top spot on the ProCity leaderboard today? Stay tuned for the latest updates.", 
            f"The competition is fierce in ProCity! Here's the latest leaderboard standings for {today}.", 
            f"Who's leading the pack in ProCity? Check out the latest leaderboard updates for {today}.", 
            "The ProCity leaderboard is always changing. Who will come out on top today?",]
        
        return leaderboard_tweets [np.random.randint(0,len(leaderboard_tweets))]


if __name__ == "__main__":
    
    pass
