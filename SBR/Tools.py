
def calculate_nearest_5(percentage_list: list[float]):
    total_errors = 0
    for i in range(5, 100):
        portions = [i * j for j in percentage_list]
        errors = [j % 5 for j in portions]

        adj_ports = [ for j, k in zip(portions, errors)]


"""
Make a matched bet calculator

Add in options for 
1) Not winning the stake for the sportsbook bet
2) Calculating losing part of the commission on the betting exchange
3) Could do other such as weigh the win on the side of the sportsbook so you dont need to bet as much
"""
