#!/usr/bin/env python
# -*- coding: utf-8 -*-

import predict
import time
import datetime
from time import gmtime, strftime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

passImgDir='/home/dane/nasluch/sat/passes/'
tleFileName='/home/filips/progs/autowx/var/tle/weather.txt'
elNOAA=20
elMETEOR=40

NOAA15=[]
NOAA18=[]
NOAA19=[]
METEORM2=[]
ktore=[ NOAA15, NOAA18, NOAA19, METEORM2 ]
g = []

tlefile=open(tleFileName, 'r')
tledata=tlefile.readlines()
tlefile.close()


for i, line in enumerate(tledata):
    if "NOAA 15" in line: 
        for l in tledata[i:i+3]: NOAA15.append(l.strip('\r\n').rstrip()),
for i, line in enumerate(tledata):
    if "NOAA 18" in line: 
        for m in tledata[i:i+3]: NOAA18.append(m.strip('\r\n').rstrip()),
for i, line in enumerate(tledata):
    if "NOAA 19" in line: 
        for n in tledata[i:i+3]: NOAA19.append(n.strip('\r\n').rstrip()),
for i, line in enumerate(tledata):
    if "METEOR-M 2" in line: 
        for o in tledata[i:i+3]: METEORM2.append(o.strip('\r\n').rstrip()),

qth = (52, -21, 5)

font = {'color':  '#212121',
        'size': 8,
        }

font2 = {'color':  '#00796B',
        'size': 12,
        }

czasStart=time.time()-1000
czasKoniec=time.time()+86400
printEl=0
minEl=20

for h in ktore:
    print h[0]
    if h[0] in ('NOAA 15', 'NOAA 18', 'NOAA 19'):
	minEl=elNOAA
    elif h[0] in ('METEOR-M 2'):
	minEl=elMETEOR
    p = predict.transits(h, qth, czasStart)
    for i in range(1,20):
	transit = p.next()
	minuty=time.strftime("%M:%S", time.gmtime(transit.duration()))
	if int(transit.peak()['elevation'])>=minEl:
	    f=predict.quick_predict(h,transit.start,qth)
	    XP=[]
	    YP=[]
	    CZAS=[]
	    TABELA=[]
	    nazwa=f[0]['name']
	    for md in f:
		YP.append(90-md['elevation'])
		XP.append(md['azimuth'])
	        CZAS.append(int(md['epoch']))
	    for ed,ag in enumerate(XP):
		TABELA.append({'czas': strftime('%H:%M:%S', time.localtime(CZAS[ed])), 'azi': np.radians(XP[ed]),'elev': 90-YP[ed],'elunc': YP[ed]})
	    theta=np.radians(XP)
	    zeniths=YP
	    plt.ioff()
	    ax = matplotlib.pyplot.figure(figsize=(4.0, 4.0))
	    ax = plt.subplot(111, projection='polar',  axisbg='#ECEFF1')  # create figure & 1 axis
	    ax.set_xticklabels([])
	    ax.set_yticklabels([])
	    gridX,gridY = 45.0,45.0
	    parallelGrid = np.arange(-90.0,90.0,gridX)
	    meridianGrid = np.arange(-180.0,180.0,gridY)
	    ax.text(0.5,1.025,'N',transform=ax.transAxes,horizontalalignment='center',verticalalignment='bottom',size=12)
	    for para in np.arange(gridY,360,gridY):
	        x= (1.1*0.5*np.sin(np.deg2rad(para)))+0.5
	        y= (1.1*0.5*np.cos(np.deg2rad(para)))+0.5
	        ax.text(x,y,u'%i\N{DEGREE SIGN}'%para,transform=ax.transAxes,horizontalalignment='center',verticalalignment='center',fontdict=font2)
	    ax.set_aspect('auto',adjustable='datalim')
	    ax.set_autoscale_on(True)
	    ax.set_rmax(90)
	    ax.set_theta_zero_location("N")
	    ax.set_theta_direction(-1)
	    ax.plot(np.linspace(0, 2*np.pi, 100), np.ones(100)*90, color='#0d47a1', linestyle='-')
	    ax.plot(theta,zeniths,'-',color='#00695C',lw=2)
	    ax.plot(theta,zeniths,'.',color='#0d47a1',alpha=0.4, lw=2)
	    dc=0.01
	    for mc in TABELA:
		ax.text(mc['azi'],mc['elunc'],' '+mc['czas']+' '+str(int(mc['elev']))+'$^\circ$',fontdict=font)
	    plt.savefig(passImgDir+'/'+nazwa+'-'+str(strftime('%Y%m%d-%H%M',time.localtime(transit.start)))+'-pass-map.png')   # save the figure to file
	    plt.close()    # close the figure
	    print "** "+strftime('%d-%m-%Y %H:%M:%S', time.localtime(transit.start))+" ("+str(int(transit.start))+") to "+strftime('%d-%m-%Y %H:%M:%S', time.localtime(transit.start+int(transit.duration())))+" ("+str(int(transit.start+int(transit.duration())))+")"+", dur: "+str(int(transit.duration()))+" sec ("+str(minuty)+"), max el. "+str(int(transit.peak()['elevation']))+" deg."
	else:
	    if str(printEl) in "1":
		print "!! "+strftime('%d-%m-%Y %H:%M:%S', time.localtime(transit.start))+" ("+str(int(transit.start))+") to "+strftime('%d-%m-%Y %H:%M:%S', time.localtime(transit.start+int(transit.duration())))+" ("+str(int(transit.start+int(transit.duration())))+")"+", dur:"+str(int(transit.duration()))+"s. ,max "+str(int(transit.peak()['elevation']))+" el."
