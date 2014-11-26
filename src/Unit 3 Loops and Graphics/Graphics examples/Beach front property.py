from tkinter import *
from random import *
from time import *
from math import *
tk = Tk()
Oct = Canvas(tk, width=800,height=800,background="skyblue")
Oct.pack()
Oct.create_rectangle(800,400,900,300,fill = "black")

numBirds = 10
sunlightlength = 125
sundiameter = 100
sunx = 500
suny = 75
sunmiddlex = sunx + sundiameter/2
sunmiddley = suny + sundiameter/2
numWaves = 15
numBuildings = 8
heightList = [140-40,160-40,180-40,220-40,240-40,260-40,280-40]

building = []
puff1 = []
puff2 = []
puff3 = []
puff4 = []
puff5 = []
puff6 = []
birdLW = []
birdRW =[]
sun = Oct.create_oval(sunx,suny,sunx+sundiameter,suny+sundiameter,fill = "yellow",outline = "yellow")

grass = Oct.create_rectangle(0,390,800,410,fill = "green",outline = "green")
grassheight = 3
for grasses in range(0,1000):
    grassx = randint(0,800)
    grassy = randint(390,410)
    grass = Oct.create_line(grassx,grassy,grassx,grassy-grassheight,fill = "forestgreen")


for sunrayNum in range (0,200):
    circlex = randint(sunlightlength*-10,sunlightlength*10)
    circlex = circlex/10
    posneg = choice([-1,1])
    sunlightx = sunmiddlex+circlex
    sunlighty = sunmiddley + posneg * sqrt(sunlightlength**2 - circlex**2)
    sunrays = Oct.create_line(sunmiddlex,sunmiddley,sunlightx,sunlighty,fill = "yellow")


for buildings in range(0,numBuildings):
    building.append(0)
    buildingx = buildings*150
    
    buildingy = randint(390,410)
    HWratio = 2
    buildingheight = choice(heightList)
    buildingwidth = buildingheight / HWratio
    horizontalWinNum = 5
    borderwidth = 5

    verticalWinNum = horizontalWinNum * HWratio
    windowSizeUD = (buildingwidth-2*borderwidth)/horizontalWinNum
    windowSizeLR = (buildingheight-2*borderwidth)/verticalWinNum


    
    water = Oct.create_rectangle(0,420,800,600, fill = "dodgerblue",outline = "dodgerblue")
topwave = Oct.create_polygon(0,400,100,395,200,400,300,405,400,400,500,395,600,400,700,405,800,400,1600,425,-800,425,fill = "dodgerblue",smooth = "true")
sand = Oct.create_rectangle(0,600,800,800, fill = "sandybrown")
for waveCount in range(0,numWaves):
    Xincrease = waveCount*200/numWaves
    waveX = 400
    Oct.create_line(0,(waveX+Xincrease),100,(waveX+Xincrease)-5,200,(waveX+Xincrease),300,(waveX+Xincrease)+5,400,(waveX+Xincrease),500,(waveX+Xincrease)-5,600,(waveX+Xincrease),700,(waveX+Xincrease)+5,800,(waveX+Xincrease), fill = "darkblue",smooth = "true")


for piecesOfSand in range (0,2500):
    x = randint(0,800)
    y = randint(600,800)
    colorList = ["Chocolate","burlywood","wheat"]
    colorchoice = choice(colorList)
    sandwidth = randint(1,6)
    Oct.create_oval(x,y,x+sandwidth,y+sandwidth, fill = colorchoice)
    


for cloudNum in range(0,9):
    puff1.append(0)
    puff2.append(0)
    puff3.append(0)
    puff4.append(0)
    puff5.append(0)
    puff6.append(0)
    
    cloudx = randint(0,800)
    cloudy = randint(26,300)

    puff1[cloudNum] = Oct.create_oval(cloudx+30*0,cloudy,cloudx+50+30*0,cloudy+50,fill = "white",outline = "white")
    puff2[cloudNum] = Oct.create_oval(cloudx+30*1,cloudy,cloudx+50+30*1,cloudy+50,fill = "white",outline = "white")
    puff3[cloudNum] = Oct.create_oval(cloudx+30*2,cloudy,cloudx+50+30*2,cloudy+50,fill = "white",outline = "white")
    puff4[cloudNum] = Oct.create_oval(cloudx+30*3,cloudy,cloudx+50+30*3,cloudy+50,fill = "white",outline = "white")
    puff5[cloudNum] = Oct.create_oval(cloudx+30*4-90,cloudy-30,cloudx+50+30*4-90,cloudy+50-30,fill = "white",outline = "white")
    puff6[cloudNum] = Oct.create_oval(cloudx+30*5-90,cloudy-30,cloudx+50+30*5-90,cloudy+50-30,fill = "white",outline = "white")
    

for birds in range(0,numBirds):
    birdLW.append(0)
    birdRW.append(0)
    birdwidth = 25
    birdxstart = randint(0,800)
    birdystart = randint(0,300)
    birdLW[birds] = Oct.create_line(birdxstart,birdystart,birdxstart+0.3*birdwidth,birdystart+0.2*birdwidth,birdxstart+0.5*birdwidth,birdystart+0.5*birdwidth,fill = "black",width = 3,smooth = "true")
    birdRW[birds] = Oct.create_line(birdxstart+0.5*birdwidth,birdystart+0.5*birdwidth,birdxstart+0.8*birdwidth,birdystart+0.1*birdwidth,birdxstart+birdwidth,birdystart,fill = "black",width = 3,smooth = "true")

sandcastleTower1 = Oct.create_polygon(200,790,200,650,230,600,260,650,260,790,fill = "navajowhite",outline = "white")
sandcastleTower2 = Oct.create_polygon(440,790,440,650,470,600,500,650,500,790,fill = "navajowhite",outline = "white")
sandcastleMiddle = Oct.create_polygon(260,790,260,650,280,650,280,660,300,660,300,650,320,650,320,660, 340,660,340,650,360,650,360,660,380,660,380,650,400,650,400,660,420,660,420,650,440,650,440,790,fill = "navajowhite",outline = "chocolate")
sandcastleIntricacy1 = Oct.create_line(200,650,260,650,fill = "chocolate")
sandcastleIntricacy1 = Oct.create_line(440,650,500,650,fill = "chocolate")

doorTop = Oct.create_arc(330,730,370,770,fill = "sienna",outline = "sienna",extent = 180,)
doorBase = Oct.create_rectangle(330,750,370,790,fill = "sienna",outline = "sienna")
doorLines = Oct.create_line(362,790,362,734,fill = "black")
doorLines = Oct.create_line(354,790,354,731,fill = "black")
doorLines = Oct.create_line(346,790,346,731,fill = "black")
doorLines = Oct.create_line(338,790,338,734,fill = "black")

towertext1 = Oct.create_text(230,640,text = "I - C - S",fill = "chocolate",font = "times 9 bold")
towertext2 = Oct.create_text(470,640,text = "A 5 - P 1",fill = "chocolate",font = "times 9 bold")
caption1 = Oct.create_text(100,50,text = "BEFORE",font = "times 30 underline bold",fill = "black")
 

Oct.update()
for cloudDelete in range(0,9):
    Oct.delete(puff1[cloudDelete])
    Oct.delete(puff2[cloudDelete])
    Oct.delete(puff3[cloudDelete])
    Oct.delete(puff4[cloudDelete])
    Oct.delete(puff5[cloudDelete])
    Oct.delete(puff6[cloudDelete])
for birdparts in range(0,numBirds):
    Oct.delete(birdLW[birdparts])
    Oct.delete(birdRW[birdparts])




Oct.delete(caption1)
sleep(3)

sunlightlength = 60
for buildings in range(0,numBuildings):
    building.append(0)
    buildingx = buildings*150
    
    buildingy = randint(390,410)
    HWratio = 2
    buildingheight = choice(heightList)
    buildingwidth = buildingheight / HWratio
    horizontalWinNum = 5
    borderwidth = 5

    verticalWinNum = horizontalWinNum * HWratio
    windowSizeUD = (buildingwidth-2*borderwidth)/horizontalWinNum
    windowSizeLR = (buildingheight-2*borderwidth)/verticalWinNum


    
    building[buildings] = Oct.create_rectangle(buildingx,buildingy,buildingx+buildingwidth,buildingy-buildingheight,fill = "lightslategrey")
    windows = Oct.create_rectangle(buildingx+borderwidth,buildingy-borderwidth,buildingx+buildingwidth-borderwidth,buildingy-buildingheight+borderwidth,fill = "yellow",outline = "grey")
    for windowbordersUD in range(0,horizontalWinNum+1):

        Oct.create_line(buildingx+borderwidth+windowbordersUD*windowSizeUD,buildingy-1,buildingx+borderwidth+windowbordersUD*windowSizeUD,buildingy-buildingheight+1,fill = "lightslategrey",width = borderwidth)
    for windowbordersLR in range(0,verticalWinNum+1):

        Oct.create_line(buildingx+1,buildingy-borderwidth-windowbordersLR*windowSizeLR,buildingx+buildingwidth-1,buildingy-borderwidth-windowbordersLR*windowSizeLR,fill = "lightslategrey", width = borderwidth)
grass = Oct.create_rectangle(0,390,800,410,fill = "#659D32",outline = "#659D32")
grassheight = 3
for grasses in range(0,1000):
    grassx = randint(0,800)
    grassy = randint(390,410)
    grass = Oct.create_line(grassx,grassy,grassx,grassy-grassheight,fill = "#629632")
water = Oct.create_rectangle(0,420,800,600, fill = "mediumblue",outline = "mediumblue")
topwave = Oct.create_polygon(0,400,100,395,200,400,300,405,400,400,500,395,600,400,700,405,800,400,1600,425,-800,425,fill = "mediumblue",smooth = "true",outline = "mediumblue")
for waveCount in range(0,numWaves):
    Xincrease = waveCount*200/numWaves
    waveX = 400
    Oct.create_line(0,(waveX+Xincrease),100,(waveX+Xincrease)-5,200,(waveX+Xincrease),300,(waveX+Xincrease)+5,400,(waveX+Xincrease),500,(waveX+Xincrease)-5,600,(waveX+Xincrease),700,(waveX+Xincrease)+5,800,(waveX+Xincrease), fill = "navy",smooth = "true")

for clouds in range(1,15):
    cloudx = randint(0,800)
    cloudy = randint(26,300)
    for cloudpuffs in range(0,6):
        if cloudpuffs == 4:
            cloudx = cloudx - 90
            cloudy = cloudy - 30
      
        clouds = Oct.create_oval(cloudx+30*cloudpuffs,cloudy,cloudx+50+30*cloudpuffs,cloudy+50,fill = "goldenrod",outline = "goldenrod")



caption2 = Oct.create_text(100,50,text = "AFTER",font = "times 30 underline bold",fill = "black")



sandcastletext = Oct.create_text(350,690,text = "Octavio Harris",fill = "chocolate",font = "times 20 bold")
sandcastletext2 = Oct.create_text(350,710,text = "was here",fill = "chocolate",font = "times 20 bold")

Oct.update()


