route=[
    {'town':'Lands End', 'distance':0, 'km':0},
    {'town':'Penzance', 'distance':21250, 'km':17},
    {'town':'Redruth', 'distance':58250, 'km':47},
    {'town':'Indian Queens', 'distance':99750, 'km':80}, 
    {'town':'Bodmin Moor', 'distance':142125, 'km':114},
    {'town':'Stowford', 'distance':179125, 'km':143},
    {'town':'North Tawton', 'distance':218625, 'km':175}, 
    {'town':'Tiverton', 'distance':261250, 'km':209},
    {'town':'Taunton', 'distance':300625, 'km':241},
    {'town':'Sedgemoor', 'distance':345375, 'km':276}, 
    {'town':'Bristol', 'distance':389125, 'km':311},
    {'town':'Newport', 'distance':431375, 'km':354},
    {'town':'Norton', 'distance':474625, 'km':380},
    {'town':'Worcester', 'distance':512750, 'km':410},
    {'town':'Kinver', 'distance':550125, 'km':440},
    {'town':'Brewood', 'distance':587500, 'km':470},
    {'town':'Market Drayton', 'distance':632000, 'km':506},
    {'town':'Church Minshull', 'distance':670000, 'km':536}, 
    {'town':'Warrington', 'distance':708750, 'km':567},
    {'town':'Chorley', 'distance':750625, 'km':601},
    {'town':'Garstang', 'distance':790000, 'km':632}
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
