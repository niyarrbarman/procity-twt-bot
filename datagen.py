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
        df_styled = data_df.style.format({'MMR' : '{:20.2f}'}).hide_index().set_properties(subset=data_df.columns, **{'text-align': 'center'}).set_properties(subset=data_df.columns, **{'width': '90px', 'height': '10px'}).set_table_styles(self.styles).background_gradient(cmap='Blues')
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
# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'