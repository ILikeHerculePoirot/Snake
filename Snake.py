import pygame as g,random as r,time,sys
g.init()
c=g.display.set_mode((800,600))
g.display.set_caption('Snake')
while True:
    p=r.randint(1,780)
    q=r.randint(1,580)
    f=g.Rect(p-(p%20),q-(q%20),20,20)
    s=[[0,0]]
    l=''
    while True:
        for e in g.event.get():
            if e.type==g.QUIT:sys.exit()
            elif(e.type==g.KEYDOWN):
                if(e.key==g.K_w and l!='d'):l='u'
                elif(e.key==g.K_s and l!='u'):l='d'
                elif(e.key==g.K_a and l !='r'):l='l'
                elif(e.key==g.K_d and l !='l'):l='r'
        a=[s[0][0],s[0][1]]
        if(l=='u'):s[0][1]-=20
        elif(l=='d'):s[0][1]+=20
        elif(l=='l'):s[0][0]-=20
        elif(l=='r'):s[0][0]+=20
        if(s[0][0]<0 or s[0][0]>800 or s[0][1]<0 or s[0][1]>600):break
        for i in range(0,len(s)):
            if(s.count(s[i])!=1):sys.exit()
        if(s[0][0]==f.x and s[0][1]==f.y):
            p=r.randint(1,780)
            q=r.randint(1,580)
            f.topleft=(p-(p%20),q-(q%20))
            while(s.count([p-(p%20),q-(q%20)])!=0):
                p=r.randint(1,780)
                q=r.randint(1,580)
                f.topleft=(p-(p%20),q-(q%20))
            if(l=='u'):s.append([s[len(s)-1][0],s[len(s)-1][1]+20])
            elif(l=='d'):s.append([s[len(s)-1][0],s[len(s)-1][1]-20])
            elif(l=='l'):s.append([s[len(s)-1][0]+20,s[len(s)-1][1]])
            elif(l=='r'):s.append([s[len(s)-1][0]-20,s[len(s)-1][1]])
        for i in range(1,len(s)):
            h=[s[i][0]-a[0],s[i][1]-a[1]]
            s[i]=a
            a=[s[i][0]+h[0],s[i][1]+h[1]]
        c.fill((0,0,0))
        g.draw.rect(c,(255,255,255),f)
        for p in s:g.draw.rect(c,(255,255,255),g.Rect(p[0],p[1],20,20))
        time.sleep(0.05)
        g.display.update()
