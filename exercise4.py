import copy
import json

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from numpy import pi

with open('election.json') as data_file:
    data = json.load(data_file)

x = [x['number'] for x in data]
top = [y['votes'] for y in data]
colors = [c['color'] if c.get('color') is not None else 'darkblue' for c in data]
short = [s['short'] if s.get('short') is not None else 'other' for s in data]
name = [n['name'] for n in data]

# part 1
p = figure(x_range=name)
p.vbar(x=name, top=top, width=0.7, color=colors)
show(p)

# part 3
shares = [s['share']/100 for s in data]
starts = [p*2*pi for p in shares[:-1]]
ends = [p*2*pi for p in shares[1:]]

p = figure(x_range=(-1,1), y_range=(-1,1))

p.wedge(x=0, y=0, radius=1, start_angle=starts, end_angle=ends, color=colors)

show(p)

############################

# part 2
parties_under_one = [p for p in data if p['share'] < 1]
x = [x['number'] for x in parties_under_one]
top = [y['votes'] for y in parties_under_one]
colors = [c.get('color') for c in parties_under_one]
short = [s.get('short') for s in parties_under_one]
name = [n['name'] for n in parties_under_one]

# part 3
ones = []
all = copy.deepcopy(data)
for party in data:
    if party['share'] < 1:
        ones.append(party)
        all.remove(party)