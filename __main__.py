from sys import argv
from simpletpb import get_magnets, search, categories as c
import argparse


category_choices = {
        'all': c.ALL,
        'audio': c.AUDIO['ALL'],
        'video': c.VIDEO['ALL'],
        'apps': c.APPLICATIONS['ALL'],
        'games': c.GAMES['ALL'],
        'porn': c.PORN['ALL'],
        'other': c.OTHER['OTHER']
        }


parser = argparse.ArgumentParser()
parser.add_argument("query", help="query to search in TPB. Provide like \"<query>\"", type=str)
parser.add_argument("-c", "--category", help="TPB category of the query", type=str, default='all', choices=sorted(category_choices.keys()))
parser.add_argument("-n", "--number", help="how many magnets", type=int, default=1)
args = parser.parse_args()


search_result = search(args.query, category=category_choices[args.category])
print('\n'.join(get_magnets(search_result)[:args.number]))


