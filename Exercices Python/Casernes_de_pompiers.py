"https://www.france-ioi.org/algo/task.php?idChapter=648&idTask=1979"

nbPairesZones = int(input())

for i in range(nbPairesZones):
    absMin1 = int(input())
    absMax1 = int(input())
    ordMin1 = int(input())
    ordMax1 = int(input())
    absMin2 = int(input())
    absMax2 = int(input())
    ordMin2 = int(input())
    ordMax2 = int(input())
    
    if (absMax1 <= absMin2 or absMin1 >= absMax2 or ordMax1 <= ordMin2 or ordMin1 >= ordMax2):
        print("NON")
    else:
        print("OUI")
