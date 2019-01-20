# Recreation of pokemon firered

#Rooms

#north,east,south,west


room = {0:{'name':'pallet_bedroom',
           'desc':'Bedroom\n\nYou\'re in your room. There is a staircase to the WEST.',
           'west':1,
           'north':-1,
           'south':-1,
           'east':-1,
           'type':'none'},

        1:{'name':'pallet_home',
           'desc':'Home\n\nYou walk into your living room. \nThere is a staircase to the EAST. \nThere is a door that leads outside to the SOUTH.',
           'east':0,
           'south':3,
           'west':-1,
           'north':-1,
           'type':'none'},
        
        2:{'name':'pallet_rival',
           'desc':'Rival Home\n\n You walk into your rival\'s house. \nThere is a door that leads outside to the SOUTH.',
           'south':3,
           'west':-1,
           'north':-1,
           'east':-1,
           'type':'none'},

        3:{'name':'pallet_center_n',
           'desc':'Pallet Town (North)\nYou walk to the northern part of Pallet Town\n There is a path SOUTH that leads to the southern part of Coquitlam.\n There is a path WEST that leads to your house.\n There is a path NORTH that leads to Surrey. \nThere is a path EAST that leads to your rival\'s house.',
           'south':4,
           'west':1,
           'east':2,
           'north':7,
           'type':'none'},
        
        4:{'name':'pallet_center_s',
           'desc':'Pallet Town (South)\nYou walk to the southern part of Pallet Town.\nThere is a path SOUTH that leads to Coquitlam\'s lake.\n There is a path NORTH that leads to the northern part of Pallet Town.\nThere is a path EAST that leads to Pallet Town\'s Lab.',
           'south':5,
           'east':6,
           'north':3,
           'west':-1,
           'type':'none'},
        
        5:{'name':'pallet_lake',
           'desc':'\tPallet Town\'s Lake\nThere seems to be Route 21 to the SOUTH over the lake, maybe if you have a pokemon with SURF you could cross it.\n There is a path NORTH that lead to the southern part of Pallet Town.',
           'south':-1,#189
           'north':4,
           'west':-1,
           'east':-1,
           'type':'none'},
        
        6:{'name':'pallet_lab',
           'desc':'\tPallet Lab\n \n You walk into Pallet Town\'s Lab home to Prof.Oak. \nThere is a door that leads outside to the SOUTH.',
           'south':4,
           'west':-1,
           'north':-1,
           'east':-1,
           'type':'none'},

        7:{'name':'route1_s',
           'desc':'\t Route 1 (South)\n You walk into the southern part of Route 1.\nThere is a path NORTH that leads to the northern part of Route 1. \nThere is a path SOUTH that leads to Pallet Town.',
           'north':8,
           'south':3,
           'west':-1,
           'east':-1,
           'type':'none'},
        
        8:{'name':'route1_n',
           'desc':'\tRoute 1 (North)\n You walk into the northern part of Route 1.\nThere is a path NORTH that leads to Viridian City.\nThere is a path SOUTH that leads to the southern part of Route 1.',
           'south':7,
           'north':9,
           'west':-1,
           'east':-1,
           'type':'grass'},
            
        9:{'name':'viridian_center_s',
           'desc':'\tViridian City (South)\nYou walk into the southern part of Viridian City.\nThere is a path NORTH that leads to the northern part of Viridian City.\nThere is a path SOUTH that leads to Route 1.\nThere is a path WEST that leads to a PykeMart.\n There is a path to the EAST that leads to the PykeCenter.',
           'south':8,
           'north':12,
           'east':10,
           'west':11,
           'type':'none'},
        
        10:{'name':'viridian_pkc',
            'desc':'\tPykecenter\nThere is a door that leads outside to the SOUTH',
            'south':9,
            'west':-1,
           'north':-1,
           'east':-1,
            'type':'none'},

        11:{'name':'viridian_pkm',
            'desc':'\tPykemart\nThere is a door that leads outside to the SOUTH',
            'south':9,
            'west':-1,
           'north':-1,
           'east':-1,
            'type':'none'},

        12:{'name':'viridian_center_n',
            'desc':'\tViridian City (North)\nYou walk into the northern part of town\nThere is a path NORTH that leads to Route 2\nThere is a path SOUTH that leads to the southern part of town\nThere is a path WEST that leads to the western part of town\nThere is a path EAST that leads to Viridian\'s gym',
            'north':35,
            'south':9,
            'west':14,
            'east':13,
            'type':'none'},

        13:{'name':'viridian_gym_s',
            'desc':'\tViridian Gym\nThere is a door to the SOUTH that leads outside',
            'south':12,
            'west':-1,
            'north':-1,
            'east':-1,
            'type':'none'},

        14:{'name':'viridian_center_w',
            'desc':'\tViridian City (West)\nThere is a path NORTH that leads to a house\nThere is a path SOUTH that leads to a house\nThere is a path EAST that leads to the northern part of town\nThere is a path WEST that leads to Route 22',
            'north':15,
            'south':16,
            'west':17,
            'east':12,
            'type':'none'},
        
        15:{'name':'viridian_house1',
            'desc':'\tViridian House\nYou walk into a house\nThere is a door to the SOUTH that leads outside',
            'type':'none',
            'south':14,
            'north':-1,
            'east':-1,
            'west':-1},

        16:{'name':'viridian_house2',
            'desc':'\tViridian House\n You walk into a house\nThere is a door to the SOUTH that leads outside',
            'type':'none',
            'south':14,
            'north':-1,
            'east':-1,
            'west':-1},

        17:{'name':'route22_e',
            'desc':'\tRoute 22 (East)\nYou walk into the eastern part of Route 22\n There is a path on water to the WEST maybe you could cross if you have a pokemon that can use surf\n There is a path to the EAST that leads to Viridian City',
            'west':-1,#18
            'east':14,
           'north':-1,
           'south':-1,
            'type':'grass'},
        
        18:{'name':'route22_m',
            'desc':'\t Route 22 (Middle) \nThere is a path WEST that leads to the western part of Route 22\n There is a path EAST that leads to the eastern part of Route 22',
            'west':19,
            'east':17,
            'north':-1,
            'south':-1,
            'type':'water'},
        
        19:{'name':'route22_w',
            'desc':'\tRoute 22 (West)\n There is a path West that leads to the Pykemon League Reception Gate\n There is a path EAST that leads to the middle of Route 22',
            'north':20,
            'east':18,
            'west':-1,
            'south':-1,
            'type':'grass'},

        20:{'name':'pklrg',
            'south':19,
            'north':21,
            'west':-1,
            'east':-1,
            'type':'none'},
            
        21:{'name':'victory_road_s1',
            'south':20,
            'north':22,
            'west':-1,
            'east':-1,
            'type':'cave'},
        
        22:{'name':'victory_road_n1',
            'south':21,
            'north':23,
            'west':-1,
            'east':-1,
            'type':'cave'},

       23:{'name':'victory_road_n2',
           'south':22,
           'east':24,
           'west':-1,
           'north':-1,
           'type':'cave'},

       24:{'name':'victory_road_e2',
           'west':23,
           'south':25,
           'north':-1,
           'east':-1,
           'type':'cave'},

       25:{'name':'victory_road_s2',
           'west':26,
           'north':24,
           'south':-1,
           'east':-1,
           'type':'cave'},

       26:{'name':'victory_road_w3',
           'south':27,
           'east':25,
           'west':-1,
           'north':-1,
           'type':'cave'},

       27:{'name':'victory_road_s3',
           'east':28,
           'north':26,
           'type':'cave'},
        
       28:{'name':'victory_road_e3',
           'west':27,
           'north':29,
           'south':-1,
           'east':-1,
           'type':'cave'},

       29:{'name':'victory_road_n3',
           'south':28,
           'east':30,
           'west':-1,
           'north':-1,
           'type':'cave'},

       30:{'name':'victory_road_exit',
           'south':31,
           'north':-1,
           'east':-1,
           'west':29,
           'type':'cave'},

       31:{'name':'indigo_plateau',
           'south':30,
           'north':34,
           'east':32,
           'west':33,
           'type':'none'},
        
       32:{'name':'indigo_plateau_pkc',
           'south':-1,
           'north':-1,
           'east':-1,
           'west':31,
           'type':'none'},

       33:{'name':'indigo_plateau_pkm',
           'south':-1,
           'north':-1,
           'east':31,
           'west':-1,
           'type':'none'},

       34:{'name':'indigo_plateau_league',
           'south':31,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'indigo'},

       35:{'name':'route2_s',
           'desc':'\tRoute 2 (South)\nYou walk into the southern part of Route 2\nThere is a path SOUTH that leads to Viridian City\nThere is a path WEST that leads to the western part of Route 2\n There is a path EAST that has a little tree blocking the way maybe if a pokemon had the move cut you could pass through',
           'south':12,
           'north':-1,
           'east':-1,#37
           'west':36,
           'type':'grass'},

       36:{'name':'route2_w',
           'desc':'\tRoute 2 (West)\nYouwalk into the western part of Route 2\n There is a path NORTH that leads to Viridian Forest\n There is a path East that leads to the southern part of Route 2',
           'desc':'\t',
           'south':-1,
           'north':39,
           'east':35,
           'west':-1,
           'type':'grass'},

       37:{'name':'route2_e',
           'desc':'\tRoute 2 (East)\nThere is a path NORTH that leads to the Digglet Cave\'s Enterance\n There is a path WEST that leads to the southern part of Route 2',
           'south':-1,
           'north':38,
           'east':-1,
           'west':35,
           'type':'none'},

       38:{'name':'route2_dce',
           'desc':'\tDigglet Cave Enterance (Route 2)\nYou walk up to the enterance of the cave\n There is a path NORTH that leads into the cave\nThere is a path SOUTH that leads to the eastern part of Route 2',
           'south':37,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},

       39:{'name':'viridian_forest_sw',
           'desc':'\tViridian Forest (South West)\n You walk into the southwestern part of the forest\n There is a path SOUTH that leads to Route 2\n There is a path EAST that leads to the southeastern part of the forest.',
           'south':36,
           'north':-1,
           'east':40,
           'west':-1,
           'type':'forest'},

       40:{'name':'viridian_forest_se',
           'desc':'\tViridian Forest (South East)\n You walk into the southeastern part of the forest\nThere is a path NORTH that leads to the northeastern part of the forest\nThere is a path WEST that leads to the southwestern part of the forest',
           'south':-1,
           'north':41,
           'east':-1,
           'west':39,
           'type':'forest'},

       41:{'name':'viridian_forest_ne',
           'desc':'\tViridian Forest (North East)\n You walk into the northeastern part of the forest\n There is a path SOUTH that leads to the southeastern part of the forest\n There is a path WEST that leads to the northwestern part of the forest',
           'south':40,
           'north':-1,
           'east':-1,
           'west':42,
           'type':'forest'},

       42:{'name':'viridian_forest_nw',
           'desc':'\tViridian Forest (North West)\nYou walk into the northwestern part of the forest\n There is a path NORTH that leads to the northern part of Route 2\n There is a path EAST that leads to the northeastern part of the forest',
           'south':-1,
           'north':43,
           'east':41,
           'west':-1,
           'type':'forest'},

       43:{'name':'route2_n',
           'desc':'\tRoute 2 (North)\n You walk into the northern part of Route 2\n There is a path NORTH that leads to Pewter City\n There is a path SOUTH that leads to Viridian Forest',
           'south':42,
           'north':44,
           'east':-1,
           'west':-1,
           'type':'grass'},

       44:{'name':'pewter_center_e',
           'desc':'\tPewter City (East)\nYou walk into the eastern part of town\nThere is a path NORTH that leads to a pokemart\nThere is a path SOUTH that leads to Route 2\n There is a path WEST that leads to Route 3\n There is a path EAST that leads to the eastern part of town',
           'south':43,
           'north':45,
           'east':50,
           'west':46,
           'type':'none'},

       45:{'name':'pewter_pkm',
           'desc':'\tPykemart\nThere is a doot to the SOUTH that leads outside',
           'south':44,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},

       46:{'name':'pewter_center_w',
           'desc':'\tPewter City (West)\n You walk into the western part of town\nThere is a path SOUTH that leads to a PykeCenter\nThere is a path WEST that leads to the Pewter Gym\nThere is a path EAST that leads to the eastern part of town',
           'south':47,
           'north':-1,
           'east':44,
           'west':49,
           'type':'none'},

       47:{'name':'pewter_pkc',
           'desc':'\tPykecenter\nThere is a door to the SOUTH that leads outside',
           'south':46,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},


       49:{'name':'pewter_gym',    #<-------------------
           'desc':'\tPewter Gym\nYou walk into the Pewter Gym\nThere is a door to the SOUTh that leads outside',
           'south':46,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},  

       50:{'name':'route3_w', # STUUUUUUUP
           'desc':'\tRoute 3 (West)\nYou walk into the western part of Route 3\nThere is a path WEST that leads to Pewter City\nThere is a path EAST that leads to the middle of Route 3',
           'south':-1,
           'north':-1,
           'east':51,
           'west':44,
           'type':'grass'},

       51:{'name':'route3_m',
           'desc':'\tRoute 3 (Middle)\nYou walk into the middle of Route 3\nThere is a path WEST that leads to the western part of Route 3\nThere is a path EAST that leads to the eastern part of Route 3',
           'south':-1,
           'north':-1,
           'east':52,
           'west':50,
           'type':'grass'},

       52:{'name':'route3_e',
           'desc':'\tRoute 3 (East)\nYou walk into the eastern of Route 3\nThere is a path WEST that leads to the middle of Route 3\n There is a path NORTH that leads to Route 4',
           'south':-1,
           'north':53,
           'east':-1,
           'west':51,
           'type':'grass'},

       53:{'name':'route4_w2',
           'desc':'\tRoute 4 (West)\nYou walk into the western part of Route 4 on the WEST side of Mt. Moon\nThere is a path to the WEST that leads to a PykemonCenter\nThere is a path NORTH that leads to Mt Moon\nThere is a path SOUTH that leads to Route 3',
           'south':52,
           'north':55,
           'east':-1,
           'west':54,
           'type':'none'},

       54:{'name':'route4_pkc',
           'desc':'\tPykemon Center\nThere is a door to the SOUTH that leads outside',
           'south':53,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},

       55:{'name':'mt_moon_sw1',
           'desc':'\tMt. Moon (South West F1)\nYou enter into the south west corner in Mt. Moon\nThere is a ladder to the NORTh that leads downwards\n There is a path to the SOUTH that leads outside\nThere is a path EAST that leads to the south east corner of Mt.Moon',
           'south':54,
           'north':62,
           'east':56,
           'west':-1,
           'type':'cave'},

       56:{'name':'mt_moon_se1',
           'desc':'\tMt. Moon (South East F1)\nYou enter the southeast corner of Mt.Moon\nThere is a path NORTH that leads to the northeast corner of Mt.Moon\nThere is a ladder to the EAST that leads downwards\nThere is a path WEST that leads to the southwest corner of Mt.Moon',
           'south':-1,
           'north':57,
           'east':61,
           'west':55,
           'type':'cave'},

       57:{'name':'mt_moon_ne1',
           'desc':'\tMt. Moon (North East F1)\nYou enter the northeast corner of Mt. Moon\nThere is a path SOUTH that leads to the southeast corner of Mt. Moon\nThere is a ladder to the EAST that leads downwards\nThere is a path WEST that leads to the northwest corner of Mt. Moon',
           'south':56,
           'north':-1,
           'east':60,
           'west':58,
           'type':'cave'},

       58:{'name':'mt_moon_nw1',
           'desc':'\tMt. Moon (North West F1)\nYou enter the northwest corner of Mt. Moon\nThere is a ladder NORTH that leads downwards\nThere is a path EAST that leads to the northeast corner of Mt. Moon',
           'south':-1,
           'north':59,
           'east':57,
           'west':-1,
           'type':'cave'},
        
       59:{'name':'mt moon_nw2',
           'desc':'\tMt. Moon (North West F2)\nYou enter the northwest corner of Mt. Moon\nThere is a ladder SOUTH that leads upwards',
           'south':58,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'cave'},

       60:{'name':'mt_moon_ne2',
           'desc':'\tMt. Moon (North East F2)\nYou enter the northeast corner of Mt. Moon\nThere is a ladder to the WEST that leads upwards\nThere is a path SOUTH that leads outside to Route 4',
           'south':63,
           'north':-1,
           'east':-1,
           'west':57,
           'type':'cave'},

       61:{'name':'mt_moon_se2',
           'desc':'\tMt. Moon (South East F2)\nYou enter the southeast corner of Mt. Moon',
           'south':-1,
           'north':-1,
           'east':56,
           'west':62,
           'type':'cave'},

       62:{'name':'mt_moon_sw2',
           'desc':'\tMt. Moon (South West F2)\nYou enter the southwest corner of Mt. Moon\n There is a path EAST that leads to the southeast corner of Mt. Moon\nThere is a ladder to the SOUTH that leads upwards',
           'south':55,
           'north':-1,
           'east':61,
           'west':-1,
           'type':'cave'}, 

       63:{'name':'route4_w1',
           'desc':'\tRoute 4 (West)\nYou walk into the western part of Route 4 on the EAST side of Mt. Moon\nThere is a path NORTH that leads to Mt. Moon\nThere is a path EAST that leads to the eastern part of Route 4',
           'south':-1,
           'north':62,
           'east':64,
           'west':-1,
           'type':'none'},

       64:{'name':'route4_e',
           'desc':'\tRoute 4 (East)\nYou walk into the eastern part of Route 4\nThere is a path WEST that leads to the western part of Route 4\nThere is a path EAST that leads to Cerulean City',
           'south':-1,
           'north':-1,
           'east':65,
           'west':63,
           'type':'grass'}, 

       65:{'name':'cerulean_center_w',
           'desc':'\tCerulean City (West)\nYou walk into the western part of town\nThere is a path NORTH that leads to Route 24\nThere is a path SOUTH that leads to Route 5 but CUT is needed\nThere is a path WEST that leads to Route 4\n There is a path EAST that leads to the middle of town',
           'south':70,
           'north':69,
           'east':66,
           'west':64,
           'type':'none'},

       66:{'name':'cerulean_center_m',
           'desc':'\tCerulean City (Middle)\nYou walk into the middle of town\nThere is a path SOUTH that leads to a Pykemart\nThere is a path EAST that leads to the eastern part of town\nThere is a path WEST that leads to the western part of town',
           'south':92,
           'north':-1,
           'east':67,
           'west':65,
           'type':'none'},

       92:{'name':'cerulean_pkm',
           'desc':'\tPykemart\nThere is a door to the SOUTH that leads outside',
           'south':66,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},
 
       67:{'name':'cerulean_center_e',
           'desc':'\tCerulean City (East)\nYou walk into the eastern part of town\nThere is a path SOUTH that leads to a Pykemon center\nThere is a path NORTH that leads to a house\nThere is a path EAST that leads to Cerulean Gym\nThere is a path WEST that leads to the middle of the town',
           'south':68,
           'north':71,
           'east':72,
           'west':66,
           'type':'none'},

       68:{'name':'cerulean_pkc',
           'desc':'\tPykemon Center\nThere is a door to the SOUTH that leads outside',
           'south':67,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},

       69:{'name':'route24_s',
           'south':65,
           'north':98,
           'east':-1,
           'west':-1,
           'type':'none'},

       98:{'name':'route24_n',
           'south':69,
           'north':-1,
           'east':99,
           'west':-1,
           'type':'forest'},

       99:{'name':'route25_w',
           'south':-1,
           'north':-1,
           'east':100,
           'west':98,
           'type':'grass'},

       100:{'name':'route25_m',
           'south':-1,
           'north':-1,
           'east':101,
           'west':99,
           'type':'none'},

       101:{'name':'route25_e',
           'south':65,
           'north':102,
           'east':-1,
           'west':100,
           'type':'none'},

       102:{'name':'bill_house',
           'south':101,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'bill_event'},

       71:{'name':'cerulean_house',
           'desc':'\tCerulean House\nYou enter a cerulean house\nThere is a door NORTH that leads out the backdoor\nThere is a door SOUTH that leads to Cerulean City',
           'south':67,
           'north':73,
           'east':-1,
           'west':-1,
           'type':'cerulean_event'},

       72:{'name':'cerulean_gym',     #<------------------------
           'south':67,
           'north':-1,
           'east':-1,
           'west':-1,
           'type':'none'},

       73:{'name':'cerulean_bhouse',
           'desc':'/tCerulean House Backyard\nYou walk into the backyard of the Cerulean House\nThere is a door SOUTH that leads inside the Cerulean house\nThere is a path EAST that leads to Route 9',
           'south':71,
           'north':-1,
           'east':74,
           'west':-1,
           'type':'none'},

     
        
 
 
           }

        
           
      
     
     
#Misc Functions
import time
import random
def ps(str): #slow typing for single strs.
    for letter in str:
        print (letter, end='')
        time.sleep(delay)

def timesleep(): # Triple dot print with time interval
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)

def Help(): # Description of all availible commands.
    ps('To move between rooms, use NORTH, EAST, SOUTH, and WEST.\nThey do not have to be capitalized. NoRtH or nOrTH will work as well.\n')

#Pokemon stats
    
def IVcreate():
    b = []
    count = 0
    while count < 6:
        a = random.randint(0,31)
        b.append(a)
        count = count + 1 
    return b

def Natcreate():
    a = random.randint(1,25)
    nateffect = {1:('Hardy',(1,1,1,1,1)),2:('Lonely',(1.1,0.9,1,1,1)),3:('Adamant',(1.1,1,0.9,1,1)),4:('Naughty',(1.1,1,1,0.9,1)),
                 5:('Brave',(1.1,1,1,1,0.9)),6:('Bold',(0.9,1.1,1,1,1)),7:('Docile',(1,1,1,1,1)),8:('Impish',(1,1.1,0.9,1,1)),
                 9:('Lax',(1,1.1,1,0.9,1)),10:('Relaxed',(1,1.1,1,1,0.9)),11:('Modest',(0.9,1,1.1,1,1)),12:('Mild',(1,0.9,1.1,1,1)),
                 13:('Bashful',(1,1,1,1,1)),14:('Rash',(1,1,1.1,0.9,1)),15:('Quiet',(1,1,1.1,1,0.9)),16:('Calm',(0.9,1,1,1.1,1)),
                 17:('Gentle',(1,0.9,1,1.1,1)),18:('Careful',(1,1,0.9,1.1,1)),19:('Quirky',(1,1,1,1,1)),20:('Sassy',(1,1,1,1.1,0.9)),
                 21:('Timid',(0.9,1,1,1,1.1)),22:('Hasty',(1,0.9,1,1,1.1)),23:('Jolly',(1,1,0.9,1,1.1)),24:('Naive',(1,1,1,0.9,1.1)),
                 25:('Serious',(1,1,1,1,1))}
    c = nateffect[a]
    return c

class create_pokemon(object):
    Type = 'none'
    def __init__(self,name,base,level): #This calculates the values of stats.
        exp = 0
        self.name = name
        EV = 0
        self.faint = 0
        self.level = level #Pokemon level
        self.ID = base[12]#ID number associated with the pkmn
        self.Type = base[9] #Type based off of base stats of each pkmn in "base" list.
        self.IV = IVcreate() #Random IV numbers to make each pokemon "unique". Based off randomization.
        self.Nat = Natcreate() #Nature that determines slight increases in particular stats.
        self.levelup(base,EV,self.IV,level,exp,self.Nat)
        self.HP = self.orHP #HP number that is used for battle and the constantly fluctuating one.
        self.stateff = 'none'
        self.moves = ['harden','pound','karate chop','double slap']
        print(self.name,self.attack,self.defense,self.spattack,self.spdef,self.speed,self.orHP,self.exp,self.level,self.ID,self.Type,)

    def levelup(self,base,EV,IV,level,exp,Nat):
        self.level = level
        print(base[1],IV[0],EV/4,level,Nat[0])
        self.attack = int(((((2*base[1]+IV[0]+(EV/4))*level)/100)+5)*Nat[1][0]) #The equation for attack
        self.defense = int(((((2*base[2]+IV[1]+(EV/4))*level)/100)+5)*Nat[1][1]) #The equation for defense
        self.spattack = int(((((2*base[3]+IV[2]+(EV/4))*level)/100)+5)*Nat[1][2]) #The equation for special attack
        self.spdef = int(((((2*base[4]+IV[3]+(EV/4))*level)/100)+5)*Nat[1][3]) #The equation for special defense
        self.speed = int(((((2*base[5]+IV[4]+(EV/4))*level)/100)+5)*Nat[1][4]) #The equation for speed
        self.orHP = int((((2*base[6]+IV[5]+(EV/4))*level)/100)+level+10) #The equation for health points (HP)
        self.exp = exp
        if level == base[11]:
            evolup(self.ID,base,EV,level)

    def evolup(self,ID,base,EV,level,exp,Nat):
        self.ID = self.ID + 1
        self.levelup(base,EV,IV,level,exp,Nat)

        
    def bat_init_(self):
        self.crit = 0
        self.acc = 0
        self.eva = 0
        self.atkstg = 0
        self.defstg = 0
        self.spatkstg = 0
        self.spdefstg = 0
        self.spdstg = 0

    def status(self):
        self.batatk = self.attack
        self.batdef = self.defense
        self.batspatk = self.spattack
        self.batspdef = self.spdef
        self.batspd = self.speed

    def batstat(self):
        stage = {-6:(2/8),-5:2/7,-4:2/6,-3:2/5,-2:2/4,-1:2/3,0:1,1:3/2,2:4/2,3:5/2,4:6/2,5:7/2,6:8/2}
        self.batatk = self.attack * stage[self.atkstg]
        self.batdef = self.defense * stage[self.defstg]
        self.batspatk = self.spattack * stage[self.spatkstg]
        self.batspdef = self.spdef * stage[self.spdefstg]
        self.batspd = self.speed * stage[self.spdstg]

    def faint(self):
        self.faint = 1

#Stats is: atk def aspatk spdef spd hp 
#EV yield is (atk,def,spatk,spdef,spd,hp)
#(ID#:(name,base stats,(EV yield),catch rate,type(s),exp yield,Evo level))
base = {1:('Bulbasaur',49,49,65,65,45,45,(0,0,1,0,0,0),45,('grass','poison'),64,16,1),
        2:('Ivysaur',62,63,80,80,60,60,(0,0,1,1,0,0),45,('grass','poison'),141,36,2),
        3:('Venasaur',82,83,100,100,80,80,(0,0,2,1,0,0),45,('grass','poison'),208,0,3),
        4:('Charmander',52,43,60,50,65,39,(0,0,0,0,1,0),45,('fire'),65,16,4),
        5:('Charmeleon',64,58,80,65,80,58,(0,0,1,0,1,0),45,('fire'),142,36,5),
        6:('Charizard',84,78,109,85,100,78,(0,0,3,0,0,0),45,('fire','flying'),209,0,6),
        7:('Squirtle',48,65,50,64,43,44,(0,1,0,0,0,0),45,('water'),66,16,7),
        8:('Wartortle',63,80,65,80,58,59,(0,1,0,1,0,0),45,('water'),143,36,8),
        9:('Blastoise',83,100,85,105,78,79,(0,0,0,3,0,0),45,('water'),210,0,9),
        10:('Caterpie',30,35,23,23,45,45,(0,0,0,0,0,1),255,('bug'),53,7,10),
        11:('Metapod',20,55,25,25,30,50,(0,2,0,0,0,0),120,('bug'),72,10,11),
        12:('Butterfree',45,50,90,80,70,60,(0,0,2,1,0,0),45,('bug','flying'),160,0,12),
        13:('Weedle',35,30,20,20,50,40,(0,0,0,0,0,1),255,('bug','poison'),52,7,13),
        14:('Kakuna',25,50,25,25,35,45,(0,2,0,0,0,0),120,('bug','poison'),71,10,14),
        15:('Beedrill',90,40,45,80,75,65,(2,0,0,1,0,0),45,('bug','poison'),159,0,15),
        16:('Pidgey',45,40,35,35,56,40,(0,0,0,0,1,0),255,('normal','flying'),55,18,16),
        17:('Pidgeotto',60,55,50,50,71,63,(0,0,0,0,2,0),120,('normal','flying'),113,36,17),
        18:('Pidgeot',80,75,70,70,101,83,(0,0,0,0,3,0),45,('normal','flying'),172,0,18),
        19:('Rattata',56,35,25,35,72,30,(0,0,0,0,1,0),255,('normal'),57,20,19),
        20:('Raticate',81,60,50,70,97,55,(0,0,0,0,2,0),127,('normal'),116,0,20),
        21:('Spearow',60,30,31,31,70,40,(0,0,0,0,1,0),255,('normal','flying'),58,20,21),
        22:('Fearow',90,65,61,61,100,65,(0,0,0,0,2,0),90,('normal','flying'),162,0,22),
        23:('Ekans',60,44,40,54,55,35,(1,0,0,0,0,0),255,('poison'),62,22,23),
        24:('Arbok',82,69,65,79,80,60,(2,0,0,0,0,0),90,('poison'),147,0,24),
        25:('Pikachu',55,40,50,50,90,35,(0,0,0,0,2,0),190,('electric'),82,'thunderstone',25),
        26:('Riachu',90,55,90,80,110,60,(0,0,0,0,3,0),75,('electric'),122,0,26),
        27:('Sandshrew',75,85,20,30,40,50,(0,1,0,0,0,0),255,('ground'),93,22,27),
        28:('Sandslash',100,110,45,55,65,75,(0,2,0,0,0,0),90,('ground'),163,0,28),
        29:('Nidoran♀', 47,52,40,40,41,55,(0,0,0,0,0,1),235,('poison'),59,16,29),
        30:('Nidorina',62,67,55,55,56,70,(0,0,0,0,0,2),120,('poison'),117,'moonstone',30),
        31:('Nidoqueen',92,87,75,85,76,90,(0,0,0,0,0,3),45,('poison','ground'),194,0,31),
        32:('Nidoran♂',57,40,40,40,50,46,(1,0,0,0,0,0),235,('poison'),60,16,32),
        33:('Nidorino',72,57,55,55,65,61,(2,0,0,0,0,0),120,('poison'),33)
             }

#Move statistics
moves = { 'pound': {'type': 'fire',
                    'category':'physical',
                    'PP': 35,
                    'target':'enemy',
                    'power':40,
                    'movetyp':'dam',
                    'acc': 1},
          'karate chop': {'type': 'grass',
                    'category':'physical',
                    'target': 'enemy',
                    'PP': 25,
                    'power':40,
                    'movetyp':'dam',
                    'acc': 1},
          'double slap': {'type': 'poison',
                    'category':'physical',
                    'target':'enemy',
                    'movetyp':'dam',
                    'PP': 10,
                    'power':40,
                    'acc': 1},
          'harden' : {'type':'normal',
                      'target': 'self',
                      'PP': 35,
                      'movetyp':'status',
                      'stat': 'def',
                      'effect': 1,
                      'acc': 1},
          
          'aerial ace':{'type':'flying',
                        'power':60,
                        'target':'enemy',
                        'PP':20,
                        'category':'physical',
                        'movetyp':'dam',
                        'acc':100000000},
          
          'air cutter':{'type':'flying',
                        'power':60,
                        'target':'enemy',
                        'PP':25,
                        'category':'special',
                        'movetyp':'dam',
                        'acc':.95}
          
    }


# battle function

def STAB(pkm,move):#STAB dmg
    if moves[move]['type'] in pkm.Type:
        stab = 1.5
    else:
        stab = 1
    return stab

def typeff(move,pkm2): #For type effectivenesses
# DEFENSE TYPE     NOR,FR,WA,EL,GR,IC,FI,PO,GR,FL,PS,BU,RO,GH,DR,DA,ST   ATK TYPE
    typematrix = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,.5, 0, 1, 1,.5], #NOR
                   [ 1,.5,.5, 1, 2, 2, 1, 1, 1, 1, 1, 2,.5, 1,.5, 1, 2], #FIR
                   [ 1, 2,.5, 1,.5, 1, 1, 1, 2, 1, 1, 1, 2, 1,.5, 1, 1], #WAT
                   [ 1, 1, 2,.5,.5, 1, 1, 1, 0, 2, 1, 1, 1, 1,.5, 1, 1], #ELE
                   [ 1,.5, 2, 1,.5, 1, 1,.5, 2,.5, 1,.5, 2, 1,.5, 1,.5], #GRA
                   [ 1,.5,.5, 1, 2,.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1,.5], #ICE
                   [ 2, 1, 1, 1, 1, 2, 1,.5, 1,.5,.5,.5, 2, 0, 1, 2, 2], #FIG
                   [ 1, 1, 1, 1, 2, 1, 1,.5,.5, 1, 1, 1,.5,.5, 1, 1, 0], #POI
                   [ 1, 2, 1, 2,.5, 1, 1, 2, 1, 0, 1,.5, 2, 1, 1, 1, 2], #GRO
                   [ 1, 1, 1,.5, 2, 1, 2, 1, 1, 1, 1, 2,.5, 1, 1, 1,.5], #FLY
                   [ 1, 1, 1, 1, 1, 1, 2, 2, 1, 1,.5, 1, 1, 1, 1, 0,.5], #PSY
                   [ 1,.5, 1, 1, 2, 1,.5,.5, 1,.5, 2, 1, 1,.5, 1, 2,.5], #BUG
                   [ 1, 2, 1, 1, 1, 2,.5, 1,.5, 2, 1, 2, 1, 1, 1, 1,.5], #ROC
                   [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1,.5,.5], #GHO
                   [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,.5], #DRA
                   [ 1, 1, 1, 1, 1, 1,.5, 1, 1, 1, 2, 1, 1, 2, 1,.5,.5], #DAR
                   [ 1,.5,.5,.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1,.5]  #STE
                   ]
    typeNo = {'normal':1,'fire':2,'water':3,'electric':4,'grass':5,'ice':6,'fighting':7,'poison':8,'ground':9,'flying':10,
              'psychic':11,'bug':12,'rock':13,'ghost':14,'dragon':15,'dark':16,'steel':17}
    atktype = typeNo[moves[move]['type']]
    if len(pkm2.Type) == 2:
        deftype = typeNo[pkm2.Type[0]]
    else:
        deftype = typeNo[pkm2.Type]
    multiplier = typematrix[atktype][deftype]
    if len(pkm2.Type) == 2: #If the pokemon is a dual type
        deftype = typeNo[pkm2.Type[1]]
        multiplier = multiplier * typematrix[atktype][deftype]
    if multiplier >= 2:
        ps('its super effective!')
    elif multiplier < 1:
        ps('its not very effective...')
    return multiplier

def crit(pkm1): #Critical chance
    critperc = {0:16,1:8,2:4,3:3,4:2}
    if random.randint(1,critperc[pkm1.crit]) == 1:
        cdmg = 2
    else:
        cdmg = 1
    return cdmg

def hitchance(pkm1,pkm2,move): #Accuracy/hit chance
    global movestats
    stageacc = {-6:.33,-5:.36,-4:.43,-3:.5,-2:.6,-1:.75,0:1,1:1.33,2:1.66,3:2,4:2.33,5:2.66,6:3}
    stg = pkm1.acc - pkm2.eva
    if stg > 6:
        stg = 6
    elif stg < -6:
        stg = -6
    acc = int(moves[move]['acc'] * stageacc[stg] * 100)
    accnum = random.randint(1,100)
    if accnum in range(1,acc):
        return 1
    else:
        return 0

    
def MOD(pkm1,pkm2,move): #modifier damage
    dmg = (STAB(pkm1,move) * typeff(move,pkm2) * crit(pkm1) * (random.randint(85,100)/100))

    return dmg

def trainertype(c):
    if c == 0:
        a = 1
    else:
        a = 1.2
    return a

def s(pkm1,b):
    pkmIb = []
    if b == 0:
        if pkm1 in pkmIb:
            None
        else:
            pkmIb.append[pkm1]
    if b == 1:
        return pkmIb

def expgain(pkm1,pkm2,s,c):
    global base
    count = 0
    print(trainertype(c))
    print(base[pkm2.ID][10])
    print(len(s))
    deltaexp = int((trainertype(c) * base[pkm2.ID][10] * pkm2.level)/(7 * len(s)))
    if len(s) > 1:
        while count <= len(s):
            if s(count) in belt:
                belt[lst(count)].exp = belt[lst(count)].exp + deltaexp
                ps('%s has gained %s exp!'%(belt[lst(count)].name), deltaexp)
            count = count + 1
    else:
        pkm1.exp = pkm1.exp + deltaexp
        ps('%s has gained %s exp!'%(pkm1.name, deltaexp))
        exp = int((4/3)*int(pkm1.level)**3)
        print (pkm1.exp)
        print(exp)
        if pkm1.exp >= exp:   
            pkm1.levelup(base[ID],pkm1.EV,pkm1.IV,pkm1.level,pkm1.exp,pkm1.Nat)
            pkm1.exp = pkm1.exp - exp

def statchange(pmove1):
    global movestats
    stat = moves[pmove1]['effect']
    typ = moves[pmove1]['stat']
    if stat >= 2:
        Typ = '%s has sharply risen.'%(typ)
    elif stat <= -2:
        Typ = '%s has sharply fallen.'%(typ)
    elif stat > 0:
        Typ =  '%s has risen.'%(typ)
    elif stat < 0:
        Typ = '%s has fallen.'%(typ)
    return Typ

def statmove(pkm1,pkm2,move1):
    if moves[move1]['target'] == 'self':
        effect = {'def':pkm1.defstg,'atk':pkm1.atkstg,'spatk':pkm1.spatkstg,'spdef':pkm1.spdefstg,'spd':pkm1.spdstg,'hp':pkm1.HP}
        alpha = moves[move1]['stat']
        print(effect[alpha])
        effect[alpha] = effect[alpha] + moves[move1]['effect']
        Typ = statchange(move1)
        pkm1.batstat()
        ps("%s has used %s! %s's %s\n"%(pkm1.name,move1,pkm1.name,Typ))
    else:
        effect = {'def':pkm2.defstg,'atk':pkm2.atkstg,'spatk':pkm2.spatkstg,'spdef':pkm2.spdefstg,'spd':pkm2.spdstg,'hp':pkm2.HP}
        alpha = moves[move1]['stat']
        effect[alpha] = effect[alpha] + moves[move1]['effect']
        Typ = statchange(move1)
        pkm2.batstat()
        ps("%s has used %s! %s %s\n"%(pkm1.name,move1,pkm2.name,Typ))

def dmg(pkm1,pkm2,pmove1,pmove2,s,c,count): #Damage calcualtion
    if moves[pmove1]['movetyp'] == 'dam':
        acc = hitchance(pkm1,pkm2,pmove1)
        if acc == 0:
            ps('%s missed!\n'%(pkm1.name))
        elif acc == 1:
            if moves[pmove1]['category'] == 'physical':
                ATK = pkm1.batatk
                DEF = pkm2.batdef
            elif moves[pmove1]['category'] == 'special':
                ATK = pkm.batspatk
                DEF = pkm2.batspdef
            dam = int((((2 * pkm1.level + 10) / 250) * (ATK/DEF) * moves[pmove1]['power'] + 2) * MOD(pkm1,pkm2,pmove1))
            if dam == 0:
                ps('%s does not effect %s...\n'%(pmove1,pkm2.name))
            else:
                pkm2.HP = pkm2.HP - dam
            if pkm2.HP <= 0:
                ps('%s has fainted!'%(pkm2.name))
                pkm2.faint()
                expgain(pkm1,pkm2,s,c)
            else:
                ps('%s used %s!\n'%(pkm1.name,pmove1))
                ps('%s does %s HP to %s!\n %s is now at: %s HP.\n'%(pkm1.name,dam,pkm2.name,pkm2.name,pkm2.HP))
                if count == 0:
                    count = count + 1
                    dmg(pkm2,pkm1,pmove2,pmove1,s,c,count)
                    
    else:
        statmove(pkm1,pkm2,pmove1)

def order(pkm1,pkm2,p1move,p2move,s,c): #Determines who goes first
    if pkm1.speed > pkm2.speed: #p1 first
        dmg(pkm1,pkm2,p1move,p2move,s,c,0)
    elif pkm2.speed > pkm1.speed: #p2 first
        dmg(pkm2,pkm1,p2move,p1move,s,c,0)
    else:
        gen = random.randint(0,1) #If they are the same speed
        if gen == 1: 
            dmg(pkm1,pkm2,p1move,p2move,s,c,0)
            dmg(pkm2,pkm1,p2move,p1move,s,c,0)
        elif gen == 2:
            dmg(pkm2,pkm1,p1move,p2move,s,c,0)
            dmg(pkm1,pkm2,p2move,p1move,s,c,0)
    
def attack(pkm1,pkm2,s,c): #Attack function
    ps('Choose the move to use: ')
    ps('%s   %s   %s   %s'%(pkm1.moves[0].upper(),pkm1.moves[1].upper(),pkm1.moves[2].upper(),pkm1.moves[3].upper()))
    pkm1move = input(': ').lower()
    pkm2move = random.randint(0,3)
    pkm2move = pkm2.moves[pkm2move]
    if pkm1move in pkm1.moves and pkm2move in pkm2.moves:
        order(pkm1,pkm2,pkm1move,pkm2move,s,c)
    else:
        ps('That is not a valid move!')
        attack(pkm1,pkm2,s,c)

def shakecheck(b):
    random = random.randint(0,65535)
    if random >= b:
        check = True
    else:
        check = False
    return check
      
def usepokeball(pkm2,pkbtype):
    a = (((3 * (pkm2.orHP - 2) * pkm2.HP) * base[pkm2.ID][10] * pkbtype)/(3 * pkm2.orHP)) * pkm2.status
    b = 1048560 / sqrt(sqrt(16711680/a))
    count = 1
    while count <= 4:
        check = shakecheck(b)
        if check == True:
           count = count + 1
        else:
           ps('%s broke out!'%(pkm2.name))
           break
    
def pokeballs(pkm2):
    pokeballstats = {'pokeball':(1,0),'great ball':(1.5,0),'great ball':(2,0)}
    global bag
    inventory = tbag[pokeballs]
    ps(inventory)
    ps('Please choose an item.')
    action = input(': ').lower()
    if action in inventory:
        tbag[pokeballs][action] = tbag[pokeballs][action] - 1
        usepokeball(pkm2,pokeballstats[action][0])
        qb = 0
        return qb
    else:
        ps('That is not in your bag!')

def selectpkm():
    global belt
    length = len(belt) - 1
    while count <= length:
        count = 0
        a = []
        a.append(belt[length].name)
        count = count + 1
    ps(a)
    ps('choose a pokemon.')
    action = input(': ').lower()
    if action in a:
        return action
    
def usemeds(item):
    global belt
    medstats = {'potion':20,'super potion':50,'hyper potion':200}
    alpha = selectpkm()
    pkm = belt[alpha].HP
    pkm.HP = pkm.HP + medstats[item]
    change = medstats[item]
    if pkm.HP > pkm.orHP:
        change = pkm.orHP - pkm.HP
        pkm.HP = pkm.orHP
    ps('%s was healed for %s HP!'%(pkm.name,change))
    
def medicine(pkm1):
    ps(bag[medicine])
    ps('please choose an item')
    action = input(': ').lower()
    if action in bag[medicine]:
        if bag[medicine][action] > 0:
            usemeds(action)
            bag[medicine][action] = bag[medicine][action] - 1
            qb = 0
            return qb
    
def bag(pkm1,pkm2):
    qb = 1
    while qb == 1:
        ps('KEY ITEMS, POKEBALLS, MEDICINE')
        menu = input(': ').lower()
        if menu == 'key items':
            ps("You can't use those items here!")
        elif menu == 'pokeballs':
            qb = pokeballs(pkm2)
        elif menu == 'medicine':
            qb = medicine(pkm1)
        
def switch():
    tar = selectpkm()
    return belt[tar]

def run(pkm1,pkm2):
    if pkm1.speed > pkm2.speed:
        ps('got away safely!')
        qq = 1
    else:
        z = random.randint(0,2)
        if  z == 0:
           ps('got away safely!')
           qq = 1
        else:
            ps('Cant escape!')
            qq = 0
    return qq
           
def battle(pkm1,pkm2,c):
    global belt
    pkm1.bat_init_()
    pkm2.bat_init_()
    pkm1.status()
    pkm2.status()
    qq = 0
    s = []
    while qq == 0:
        ps('attack, run, switch, or bag?')
        if pkm1 not in s:
            s.append(pkm1)
        action = input(': ').lower()
        if action == 'attack':
             attack(pkm1,pkm2,s,c)
             if pkm1.faint == 1 or pkm2.faint == 1:
                 break
        if action == 'bag':
            bag(pkm1,pkm2)
        if action == 'switch':
            pkm1 = switch()
        if action == 'run':
             qq = run(pkm1,pkm2)


#Menu
    
def look(a,b):
    if a == 1:
        print(pdex[b])
        print(pdexdes[b])
    elif a == 2:
        if b in pdex:
            print(b)
            alpha = pdex.index(b)
            print(pdexdes[alpha])
        else:
            print('That is not in the Pokédex.')
            
def pokedex():
    global pdex
    global pdexdes
    look(a,b)
    if a == 1:
        print(pdex[b])
        print(pdexdes[b])
    elif a == 2:
        if b in pdex:
            print(b)
            alpha = pdex.index(b)
            print(pdexdes[alpha])
        else:
            print('That is not in the Pokédex.')
    while True:
        print('Please enter your method of search: by number or name,\nor QUIT to exit.')
        action = input(": ").lower()
        if action == 'number':
            search = input(': ').lower()
            try:
                int(search)
                search = int(search) - 1
                print('hi')
                look(1,search)
            except ValueError:
                print('thats not a vaild number!')
        elif action == 'name':
            search = input(': ').lower()
            if int(search) == True:
                print('Thats not a valid string!')
            else:
                look(2,search)
        elif action == 'quit':
            print('Quitted Pokédex.')
            break
        else:
            print('Thats not a valid input!')
            
def pokemon():
    selectpkm()
    
def bagob():
    print('3')
    
def tcard():
    print('4')
    
def save():
    print('5')
    
def options():
    global delay
    print('6')
    None

def menu():
    print('hi')
    action = input(': ').lower()
    if action == 'pokedex':
        pokedex()
    elif action == 'pokemon':
        pokemon()
    elif action == 'bag':
        bagob()
    elif action == 'trainer card' or action == 'tcard':
        tcard()
    elif action == 'save':
        save()
    elif action == 'options':
        options()
    elif action == 'exit':
        return('hi')
def wild_b(currentroom):
    import random
    global base
    global belt
    
    type_b={'grass':{1:{'base':16,
                        'name':'Pidgey'},
                     2:{'base':19,
                        'name':'Rattata'},
                     3:{'base':10,
                        'name':'Caterpie'},
                     4:{'base':13,
                        'name':'Weedle'}},
            'forest':{1:{'base':10,
                         'name':'Caterpie'},
                      2:{'base':13,
                         'name':'Weedle'},
                      3:{'base':14,
                         'name':'Kakuna'},
                      4:{'base':11,
                         'name':'Metapod'},
                      5:{'base':25,
                         'name':'Pikachu'}}}
    
    level_wb={'route1_n':{'ml':2,
                          'hl':4},
              'route2_s':{'ml':2,
                          'hl':5},
              'route2_w':{'ml':2,
                          'hl':5},
              'viridian_forest_sw':{'ml':3,
                                    'hl':5},
              'viridian_forest_se':{'ml':3,
                                    'hl':5},
              'viridian_forest_ne':{'ml':3,
                                    'hl':5},
              'viridian_forest_nw':{'ml':3,
                                    'hl':5},
              'route22_e':{'ml':2,
                           'hl':5}}
    if room[currentroom]['type']=='grass' or room[currentroom]['type']=='forest':
        
        if room[currentroom]['type']=='grass':
            wpg=random.randint(1,4)
            wpl=random.randint(level_wb[room[currentroom]['name']]['ml'],level_wb[room[currentroom]['name']]['hl'])
            wp_type='grass'

        if room[currentroom]['type']=='forest':
            wpg=random.randint(1,5)
            wpl=random.randint(level_wb[room[currentroom]['name']]['ml'],level_wb[room[currentroom]['name']]['hl'])
            wp_type='forest'
        print(type_b[wp_type][wpg]['base'])
        print(wpl)

        wp_c=create_pokemon(type_b[wp_type][wpg]['name'],base[type_b[wp_type][wpg]['base']],wpl)
        print('\n\nA wild ',type_b[wp_type][wpg]['name'],' Appears! Time to BATTLE!\n\n')
        battle(belt[0],wp_c,0)

def trainer_b(currentroom):
    global belt
    global base
    trainer={'route2_s':{1:{'name':'Weedle',
                        'base':13,
                        'level':6}},
             'viridian_forest_sw':{1:{'name':'Weedle',
                                      'base':13,
                                      'level':7}},
             'viridian_forest_se':{1:{'name':'Kakuna',
                                     'base':14,
                                     'level':7}},
             'viridian_forest_ne':{1:{'name':'Caterpie',
                                      'base':10,
                                      'level':8}}
             }
    
    if room[currentroom]['name']=='route2_s' or room[currentroom]['name']=='route2_w' or room[currentroom]['name']=='viridian_forest_sw' or room[currentroom]['name']=='viridian_forest_se' or room[currentroom]['name']=='viridian_forest_ne':
            ps('\n\nA Trainer has challenged you to BATTLE!\n\n')
            vfr1=create_pokemon(trainer[room[currentroom]['name']][1]['name'],base[trainer[room[currentroom]['name']][1]['base']],trainer[room[currentroom]['name']][1]['level'])
            battle(belt[0],vfr1,1) 
        
#Events
        
def event_1():
    ps('Hello, there!\nGlad to meet you!\nWelcome to the world of Python! My name is Sean Oreily.\nPeople affectionately refer to me as\nthe Programming teacher.\nThis world is inhabited far and wide\nby creatures called POKéMON. For some people, POKéMON are pets.\nOthers use them for battle.\nAs for myself, I study pokemon as a profession.\nBut first, tell me a little about yourself.\nAre you a boy?\nOr are you a girl?')
    gender = input(str(': ')).lower()
    print(gender)
    key = 1
    while key == 1:
        if gender == 'girl' or gender == 'boy':
            break
        else:
            ps('That is not a proper gender. Please enter a proper gender. ')
            gender = input(': ')
    ps('What is your name?')
    name = input(str(': '))
    ps('Right... So your name is %s? (Y/N)'%(name))
    conf = input(': ').upper()
    while conf == 'N':
        ps('What is your name?')
        name = input(str(': '))
        ps('Right... So your name is %s? (Y/N)'%(name))
        conf = input(': ').upper()
    ps("My son has known you for quite a while now.\nYou've been rivals since you were babies.\nEr... what was his name again?")
    rname = input(': ')
    ps('Right... So his name is %s? (Y/N)'%(rname))
    conf = input(': ').upper()
    while conf == 'N':
        ps('What is his name?')
        rname = input(str(': '))
        ps('Right... So his name is %s? (Y/N)'%(rname))
        conf = input(': ').upper()
    ps("%s! Your very own POKéMON legend is about to unfold!\nA world of dreams and adventures with POKéMON awaits!\nLet's go!\n"%(name))
    return gender,name,rname
def event_2(room,action,rname,name):
    global belt
    if room == 'pallet_center_n':
        if action == 'north':
            ps('\nStop!')
            time.sleep(.5)
            ps('\nIts dangerous out there! Wild POKéMON live in tall grass!\nCome! Follow me to my  Classroom!\n')
            room = 'pallet_lab'
            ps("You notice %s is inside already.\n%s! %s! I have three POKéMON here on the desk.\n%s, since I promised a POKéMON to you,\nI'll let you pick first!\n"%(rname,name,rname,name))
            ps('There are three pokemon to choose from:\nPops! What about me?\n%s? hm... let me see. You can choose after %s!\n'%(rname,name))
            ps('CHARMANDER - the blaze pokemon. A strong fire pokemon.\n')
            ps('SQUIRTLE - the turtle pokemon. A strong water pokemon.\n')
            ps('BULBASAUR - the vine pokemon. A strong grass pokemon.\n')
            ps('Choose one: C for Charmander, S for Squirtle, and B for Bulbasaur.\n')
            choice = input(': ').upper() #Choose starter pkmn.
            if choice == 'C':
                pkm1 = 'Charmander'
                ID = 4
            if choice == 'S':
                pkm1 = 'Squirtle'
                ID = 7
            if choice == 'B':
                pkm1 = 'Bulbasaur'
                ID = 1
            action = input('Choose a nickname for your pokemon? (Y/N): ').lower()
            if action == 'y':
                pkm1 = input(': ')
                pkm1 = create_pokemon(pkm1,base[ID],5)
                ps('%s was added to your belt!\n'%(pkm1.name))
                belt.append(pkm1)
            else:
                pkm1 = create_pokemon(pkm1,base[ID],5)
                ps('%s was added to your belt\n!'%(pkm1.name))
                belt.append(pkm1)
            ps('Fine! ill take this one then!\n')
            IDchange = {4:7,7:1,1:4}
            a = base[IDchange[ID]][0]
            ps('%s took %s\n!'%(rname,a))
            pkm2 = create_pokemon(a,base[IDchange[ID]],5)
            ps('Hey %s! lets test out our new pokemon!\n'%(name))
            timesleep()
            ps('Oh for petes sake... always pushy as always. \nUse attack to use moves.\n Use bag to use items.\n Use run to run away.\n Use switch to change your current pokemon.\n')
            battle(pkm1,pkm2,2)
            newroom = 6
            currentroom = newroom
belt = [] #Pokemon belt
tbag = {pokeballs:{'pokeball':0,'great ball':0},
       medicine:{'potion':0,'super potion':0,'hyper potion':0,'max potion':0}
       }

#Key commands
delay = 0.025
z = 1
ec = 1

currentroom = 0
a = event_1()
gender = a[0]
name = a[1]
rname = a[2]
timesleep()
ps("\nOh! %s! Don't forget your stuff before you go out!\n"%(name))
time.sleep(.5)
ps('Obtained BACKPACK!\n')
time.sleep(.5)
ps('Obtained TRAINER CARD!\n')
time.sleep(.5)
ps('Go! Your adventure awaits!\n')
Help()
print(room[currentroom]['desc'])
while z == 1:
    action = input(': ').lower()
    if action == 'x' or action == 'menu':
        menu()
    if ec == 1:
        event_2(room[currentroom]['name'],action,rname,name)
    #move actions
    if action == 'type' or action == 'east' or action == 'north' or action =='south' or action =='west' or action =='name':
        newroom = room[currentroom][action]
        if newroom == -1:
            print('You Cant Go That Way')
        if newroom != -1:
            if action != 'type':
                if action != 'desc':
                    currentroom=newroom
                    wild_b(currentroom)
                    trainer_b(currentroom)
                    print('\n')
                    print(room[currentroom]['desc'])
    else:
        print('You Can\'t Do That')
    
    
    

    
    

