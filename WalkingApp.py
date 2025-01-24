route=[
    {'town':'Lands End', 'distance':0},
    {'town':'Bristol', 'distance':1000},
    {'town':'Bath', 'distance':20000},
    {'town':'Place', 'distance':300000}
]

total_steps=0

current_town='Lands End'

todays_steps=40001100

total_steps=total_steps+todays_steps

def find_town(total_steps):
    for i, current in enumerate(route):
        if current['distance']> total_steps:
            return route[i-1]['town']
    return route[-1]['town']
            
if find_town(total_steps) !=current_town:
    current_town=find_town(total_steps)
    print(current_town)
