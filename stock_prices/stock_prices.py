#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # this solution works except it does not work for the test case with a negative profit  
    # max_profit = 0
    # min_price = prices[0]
    # for i in range(1, len(prices)):
    #   profit = prices[i] - min_price
    #   max_profit = max(profit, max_profit)
    #   min_price = min(min_price, prices[i])

    #changing profit to be assigned to this allows for the test case with negative numbers 
    profit = prices[1] - prices[0]
    price = prices[0]
    
    #need to start the loop after the first item 
    for i in prices[1:]:
        if (i - price) > profit:
            profit = i - price
        if i < price:
            price = i
            
    return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))