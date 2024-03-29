import sys
import math

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist 


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
sites=[]
num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites.append([site_id,x,y])


# game loop
while True:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        
    num_units = int(input())
    queen_pos={'x':0,'y':0}
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if (owner==0 and unit_type==-1):
            queen_pos['x']=x
            queen_pos.['y']=y
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    sitesSorted=sorted(sites,key=lambda site: calculateDistance(site[1],site[2],queen_pos.x,queen_pos,y))
    print(sitesSorted)
    # First line: A valid queen action
    # Second line: A set of training instructions
    print("WAIT")
    print("TRAIN")