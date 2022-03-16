import os
import pandas as pd

#GLOBAL
dirpath = '/usr/src/app/data/'
outputpath = '/usr/src/app/'
#Helper lists
cols = ["Div","Date","FTR","HomeTeam","FTHG","HS","HST","AwayTeam","FTAG","AS","AST","HTR","HTHG","HTAG"]
board_cols = ['Team','Pts','W','L','D','GF','GA','DIFF','Season']
goal_stat_cols = ['Season','Team','GF']
score_reverted_cols = ['Team','n_of_matches','Season']
shot_stats_cols = ['Team','shot_percentage','Season']
#- Equipo más goleador por temporada.
best_scoring_team_by_season = pd.DataFrame()
#- Equipo con la mejor relación de disparos al arco terminando en gol por temporada.
best_shot_stats_team_df = pd.DataFrame()
#- Equipo que dio vuelta mas resultados por temporada
best_lose_to_win_team_df = pd.DataFrame()

def get_season_from_file(filename):
    return filename.rpartition('-')[2].rpartition('_')[0]

def get_teams(df):
    return pd.concat([df['HomeTeam'],df['AwayTeam']]).unique()

def get_pts_by_team(df,item):
    hw = df.apply(lambda x: True if (x['HomeTeam'] == item and x['FTR'] == 'H') else False , axis=1)
    aw = df.apply(lambda x: True if (x['AwayTeam'] == item and x['FTR'] == 'A') else False , axis=1)
    d = df.apply(lambda x: True if (x['HomeTeam'] == item or x['AwayTeam'] == item and x['FTR'] == 'D') else False , axis=1)
    return (len(hw[hw == True].index))*3 + (len(aw[aw == True].index))*3 + len(d[d == True].index)

def get_w_by_team(df,item):
    hw = df.apply(lambda x: True if (x['HomeTeam'] == item and x['FTR'] == 'H') else False , axis=1)
    aw = df.apply(lambda x: True if (x['AwayTeam'] == item and x['FTR'] == 'A') else False , axis=1)
    return len(hw[hw == True].index) + len(aw[aw == True].index)

def get_l_by_team(df,item):
    hw = df.apply(lambda x: True if (x['HomeTeam'] == item and x['FTR'] == 'A') else False , axis=1)
    aw = df.apply(lambda x: True if (x['AwayTeam'] == item and x['FTR'] == 'H') else False , axis=1)
    return len(hw[hw == True].index) + len(aw[aw == True].index)

def get_d_by_team(df,item):
    d = df.apply(lambda x: True if (x['HomeTeam'] == item or x['AwayTeam'] == item and x['FTR'] == 'D') else False , axis=1)
    return len(d[d == True].index)

def get_best_shot_stats_by_team(df,item):
    shots = df.loc[df['HomeTeam'] == item, 'HST'].sum() + df.loc[df['AwayTeam'] == item, 'AST'].sum()
    goals = df.loc[df['HomeTeam'] == item, 'FTHG'].sum() + df.loc[df['AwayTeam'] == item, 'FTAG'].sum()
    return shots/goals

def get_best_lose_to_win_team(df,item):
    htimes = df.apply(lambda x: True if (x['HomeTeam'] == item and x['HTAG'] > x['HTHG'] and x['FTHG'] > x['FTAG']) else False , axis=1)
    atimes = df.apply(lambda x: True if (x['AwayTeam'] == item and x['HTHG'] > x['HTAG'] and x['FTAG'] > x['FTHG']) else False , axis=1)
    return len(htimes[htimes == True].index) + len(atimes[atimes == True].index)

def get_gf_by_team(df,item):
    hg = df.loc[df['HomeTeam'] == item, 'FTHG'].sum()
    ag = df.loc[df['AwayTeam'] == item, 'FTAG'].sum()
    return hg + ag

def get_ga_by_team(df,item):
    ag = df.loc[df['HomeTeam'] == item, 'FTAG'].sum()
    hg = df.loc[df['AwayTeam'] == item, 'FTHG'].sum()
    return ag + hg

def generate_output_file(df,filename):
    df.to_csv(outputpath+filename, sep = "\t", encoding='utf-8', index = False)

def process_data(df,file_season):
    global best_scoring_team_by_season, best_lose_to_win_team_df, best_shot_stats_team_df
    teams = get_teams(df)
    #- Position Table
    board = pd.DataFrame(columns=board_cols)
    score_reverted = pd.DataFrame(columns=score_reverted_cols)
    shot_stats = pd.DataFrame(columns=shot_stats_cols)
    #- calculating stats
    for team in teams:
        #calc stats
        team_pts = get_pts_by_team(df,team)
        team_w = get_w_by_team(df,team)
        team_l = get_l_by_team(df,team)
        team_d = get_d_by_team(df,team)
        team_gf = get_gf_by_team(df,team)
        team_ga = get_ga_by_team(df,team)
        team_diff = team_gf - team_ga
        #Build new DF and add data
        board.loc[-1] = [team,team_pts,team_w,team_l,team_d,team_gf,team_ga,team_diff,file_season]
        board.index = board.index + 1
        board = board.sort_values(by=['Pts'], ascending=False)
        #-----------Stats by team-------------
        #scores
        revert_score = get_best_lose_to_win_team(df,team)
        score_reverted.loc[-1] = [team,revert_score,file_season]
        score_reverted.index = score_reverted.index + 1
        #shots
        shots_percentage = get_best_shot_stats_by_team(df,team)
        shot_stats.loc[-1] = [team,shots_percentage,file_season]
        shot_stats.index = shot_stats.index + 1

    #Collecting data for best scoring team
    best_scoring_team= board[board['GF']==board['GF'].max()]
    best_scoring_team_by_season = pd.concat([best_scoring_team_by_season, best_scoring_team[goal_stat_cols]],ignore_index=True, sort=False)
    #Collecting data for score reverted
    score_reverted = score_reverted[score_reverted['n_of_matches']==score_reverted['n_of_matches'].max()]
    best_lose_to_win_team_df = pd.concat([best_lose_to_win_team_df, score_reverted],ignore_index=True, sort=False)
    #Collecting data for shot stats
    shot_stats = shot_stats[shot_stats['shot_percentage']==shot_stats['shot_percentage'].max()]
    best_shot_stats_team_df = pd.concat([best_shot_stats_team_df, shot_stats],ignore_index=True, sort=False)

    return board


def main():
    jsonfiles = os.listdir(dirpath)
    position_table_df = pd.DataFrame()
    for jsonfile in jsonfiles:
        df = pd.read_json(dirpath+jsonfile)
        file_season = get_season_from_file(jsonfile)
        filtered_data_df = df[cols]

        #- The position table for all the seasons.
        position_table_df = pd.concat([position_table_df,process_data(filtered_data_df,file_season)], ignore_index=True, sort=False)
    
    generate_output_file(position_table_df,'position_table.csv')
    generate_output_file(best_scoring_team_by_season,'best_scoring_team.csv')
    generate_output_file(best_shot_stats_team_df,'best_shots_stats.csv')
    generate_output_file(best_lose_to_win_team_df,'score_reverted.csv')

if __name__ == "__main__":
    main()