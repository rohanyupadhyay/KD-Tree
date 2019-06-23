from graphics import *;
class bpt():
    def __init__(self):
        self.sep=None;
        self.xvalues=None;
        self.yvalues=None;
        self.lnext=None;
        self.rnext=None;
        self.par=None;
        self.top=None;
        self.bot=None;
        self.left=None;
        self.right=None;
     
     



print("Enter the number of values: ");
n=int(input());
x=[];
y=[];
print("\n");
for i in range(n):
    print("Enter the ["+str(i+1)+"] x coordinate: ");
    x.append(int(input()));
    print("Enter the ["+str(i+1)+"] y coordinate: ");
    y.append(int(input()));

win = GraphWin("Window",1200,700);
for i in range(n):
    print(str(x[i])+" "+str(y[i])+"\n");
    pt=Point(((x[i]-1)*1200)/100,700-((y[i]-1)*700)/100);
    cir = Circle(pt, 5)
    cir.draw(win);




def createbpt(theTree,xmin,ymin,xmax,ymax,c):
   
    
    tc=0;
    for i in range(n):
        if(x[i]>=xmin and x[i]<=xmax and y[i]>=ymin and y[i]<=ymax):
            tc+=1;

    if(tc>2):
        if(theTree.par==None):
            tx=x;
            tx.sort;
            xsize=len(tx);
       
            theTree.sep=tx[int(xsize/2)];
            line = Line(Point(((theTree.sep-2)*1200)/100,700-((ymin-1)*700)/100), Point(((theTree.sep-2)*1200)/100, 700-((ymax)*700)/100));
            line.draw(win);
            theTree.left=xmin;
            theTree.bot=ymin;
            theTree.right=xmax;
            theTree.top=ymax;

            theTree.lnext=bpt();
            ptr=theTree.lnext;
            ptr.par=theTree;
            c+=1;
            print("\n"+str(theTree.sep)+" l "+str(xmin)+" "+str(ymin)+" "+str(theTree.sep-1)+ " "+str(ymax)+" "+str(c)+"\n");
            createbpt(ptr,xmin,ymin,theTree.sep-1,ymax,c);


            theTree.rnext=bpt();
            ptr=theTree.rnext;
            ptr.par=theTree;
            print("\n"+str(theTree.sep)+" r "+str(theTree.sep)+" "+str(ymin)+" "+str(xmax)+" "+str(ymax)+ " "+str(c)+"\n");
            createbpt(ptr,theTree.sep,ymin,xmax,ymax,c);

           
        
                    
                

        else:
            if(c%2==1): 
               
                c+=1;                                    
                count=0;
                ty=None;
                ty=[];
                for i in range(n):
                    if(x[i]>=xmin and x[i]<=xmax and y[i]>=ymin and y[i]<=ymax):
                        count+=1;
                        ty.append(y[i]);
                ty.sort();
                ysize=len(ty);
                

                theTree.sep=ty[int(ysize/2)];
                line = Line(Point(((xmin-2)*1200)/100,700-((theTree.sep-2)*700)/100), Point(((xmax-1)*1200)/100, 700-((theTree.sep-2)*700)/100));
                line.draw(win);
                theTree.left=xmin;
                theTree.bot=ymin;
                theTree.right=xmax;
                theTree.top=ymax;

                theTree.lnext=bpt();
                ptr=theTree.lnext;
                ptr.par=theTree;
                print("\n"+str(theTree.sep)+" yl "+str(xmin)+" "+str(ymin)+" "+str(xmax)+" "+str(theTree.sep-1)+" "+str(c)+"\n");
                createbpt(ptr,xmin,ymin,xmax,theTree.sep-1,c);

                theTree.rnext=bpt();
                ptr=theTree.rnext;
                ptr.par=theTree;
                print("\n"+str(theTree.sep)+" yr "+str(xmin)+" "+str(theTree.sep)+" "+str(xmax)+" "+str(ymax)+ " "+str(c)+"\n");
                createbpt(ptr,xmin,theTree.sep,xmax,ymax,c);


            else:
                if(c%2==0):
                
                    c+=1;
                    count=0;
                    tx=None;
                    tx=[];
                    for i in range(n):
                        if(x[i]>=xmin and x[i]<=xmax and y[i]>=ymin and y[i]<=ymax):
                            count+=1;
                            tx.append(x[i]);
                    tx.sort();
                    xsize=len(tx);
               

                    theTree.sep=tx[int(xsize/2)];
                    line = Line(Point(((theTree.sep-2)*1200)/100,700-((ymin-2)*700)/100), Point(((theTree.sep-2)*1200)/100, 700-(((ymax-1)*700)/100)));
                    line.draw(win);
                    theTree.left=xmin;
                    theTree.bot=ymin;
                    theTree.right=xmax;
                    theTree.top=ymax;
                
                    theTree.lnext=bpt();
                    ptr=theTree.lnext;
                    ptr.par=theTree;
                    print("\n"+str(theTree.sep)+" xl "+str(xmin)+" "+str(ymin)+" "+str(xmax)+" "+str(theTree.sep-1)+ " "+str(c)+"\n");
                    createbpt(ptr,xmin,ymin,theTree.sep-1,ymax,c);
                    
                    theTree.rnext=bpt();
                    ptr=theTree.rnext;
                    ptr.par=theTree;
                    print("\n"+str(theTree.sep)+" xr "+str(theTree.sep)+" "+str(ymin)+" "+str(xmax)+" "+str(ymax)+ " "+str(c)+"\n");
                    createbpt(ptr,theTree.sep,ymin,xmax,ymax,c);

    else:
        theTree.xvalues=[];
        theTree.yvalues=[];
        theTree.left=xmin;
        theTree.bot=ymin;
        theTree.right=xmax;
        theTree.top=ymax;

        for i in range(n):
            if(x[i]>=xmin and x[i]<=xmax and y[i]>=ymin and y[i]<=ymax):
                theTree.xvalues.append(x[i]);
                theTree.yvalues.append(y[i]);
   



t=bpt();

c=0;
createbpt(t,1,1,100,100,c);
    

input();
win.close();
