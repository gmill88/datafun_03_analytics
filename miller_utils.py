"""
This module provides a reusable byline for evaluating the top 10 
hitters of the Cardinals Baseball team
Last updated January 12, 2024 for the 2023 season
"""

import math
import statistics

def main(): #function to display byline
    print(byline)
    
#defining all variables
Team_name: str="Cardinals"
count_players_on_active_roster: int=26 #of players on an active roster, not just hitters
made_playoffs: bool=False #reflects outcome of 2023
top_10_hitters_average: float=.258
positions_played: list= ["infield, outfield, catcher"]
batting_averages: list=[.284,.276,.268,.266,.264,.261,.248,.244,.236,.233]

#strings made from above variables
active_players_string: str=f"There are currently {count_players_on_active_roster} players on the active roster."
made_playoffs_string: str=f"Did the Cardinals make the playoffs in 2023? {made_playoffs}"
top_10_hitters_average_string: str=f"The top 10 hitters in the Cardinals lineup held an average batting average of {top_10_hitters_average}."
positions_played_string: str=f"Positions played include {positions_played[0]}"
#extracted each to get rid of brackets
batting_averages_string: str=f"The batting averages listed are {batting_averages[0]}, {batting_averages[1]}, {batting_averages[2]}, {batting_averages[3]}, {batting_averages[4]}, {batting_averages[5]}, {batting_averages[6]}, {batting_averages[7]}, {batting_averages[8]}, {batting_averages[9]}"

smallest=min(batting_averages)
largest=max(batting_averages)
total=sum((batting_averages))
count=len(batting_averages)
mean=statistics.mean(batting_averages)
mode=statistics.mode(batting_averages)
median=statistics.median(batting_averages)
standard_deviation=statistics.stdev(batting_averages)

#creating a string for all batting stats to be called on in byline
batting_stats_string: str=f"""
  Descriptive statistics for batting averages
  smallest: {smallest}
  largest: {largest}
  total: {total}
  count: {count}
  mean: {mean}
  mode: {mode}
  median: {median}
  standard deviation: {standard_deviation}
"""

byline: str=f"""
{Team_name}
{active_players_string}
{made_playoffs_string}
{top_10_hitters_average_string}
{positions_played_string}
{batting_averages_string}
{batting_stats_string}
"""

#code can only run from this script
if __name__ == '__main__':
    main()
