from util.PlayerMatchHistory import GetPlayerMatchHistory
from util.ReadMatchData import ReadMatchData
from util.MakeGraph.MakeGraph import MakeGraph


def main():
    
    player = 'Twitch_belleeun'
    platform = 'PC'

    # Get match history
    MatchData = GetPlayerMatchHistory()
    match_history = MatchData.get_match_history(player,
                                                platform.upper())

    # Filter relevant data from the match history
    ReadMatch = ReadMatchData(match_history, 'BRScore')
    filtered_data = ReadMatch.filter_match_data()

    print(filtered_data)

    # Make graphs with the data provided
    Graph = MakeGraph(filtered_data)
    Graph.line_plot()

if __name__ == '__main__':
    main()
