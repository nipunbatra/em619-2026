"""Editable SVG teaching diagrams. All numeric examples are authored, not model results."""
import math,html
I='#14171F';M='#4A5160';B='#245EDB';T='#E4ECFF';G='#0F766E';R='#BE123C';L='#D9DDE5'
def txt(x,y,s,size=26,color=I,anchor='start',weight=500):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(s))}</text>'
def line(x,y,xx,yy,c=L,w=2,dash=''):return f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{c}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
def box(x,y,w,h,label,c=B,fill=T,size=25):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{c}" stroke-width="2"/>'+txt(x+w/2,y+h/2+size*.35,label,size,c,'middle')
def arrow(x,y,xx,yy,c=B):return line(x,y,xx,yy,c,2.5)+f'<path d="M {xx-8} {yy-5} L {xx} {yy} L {xx-8} {yy+5}" fill="none" stroke="{c}" stroke-width="2" transform="rotate({math.degrees(math.atan2(yy-y,xx-x))} {xx} {yy})"/>'
def svg(s):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 410" role="img" style="font-family:Avenir Next,Segoe UI,sans-serif">'+s+'</svg>'
def rows(headers,data,widths=None):
 import textwrap
 widths=widths or [1060/len(headers)]*len(headers)
 size=23
 def wrap(s,w):return textwrap.wrap(str(s),max(8,int((w-24)/(size*.54))),break_long_words=False,break_on_hyphens=False) or ['']
 for trial in range(5):
  hw=[wrap(h,w) for h,w in zip(headers,widths)]
  wrapped=[[wrap(cell,w) for cell,w in zip(row,widths)] for row in data]
  head=max(map(len,hw))*size*1.25+25
  heights=[max(map(len,row))*size*1.28+20 for row in wrapped]
  if head+sum(heights)<=398:break
  size-=1
 s='';x=30
 for parts,w in zip(hw,widths):
  for j,part in enumerate(parts):s+=txt(x+10,26+j*size*1.25,part,size,B,weight=650)
  x+=w
 s+=line(30,head-8,1090,head-8);y=head+size
 for partsrow,height in zip(wrapped,heights):
  x=30
  for parts,w in zip(partsrow,widths):
   for j,part in enumerate(parts):s+=txt(x+10,y+j*size*1.28,part,size)
   x+=w
  y+=height;s+=line(30,y-size-8,1090,y-size-8)
 return svg(s)

def flow(labels,sub=None):
 n=len(labels);w=min(240,960/n-25);gap=(1080-n*w)/(n-1) if n>1 else 0;s=''
 for i,label in enumerate(labels):
  x=20+i*(w+gap);s+=box(x,140,w,90,label,size=24)
  if i<n-1:s+=arrow(x+w+7,185,x+w+gap-7,185)
  if sub:s+=txt(x+w/2,280,sub[i],21,M,'middle')
 return svg(s)
def dots(x,y,values,spacing=30):return ''.join(f'<circle cx="{x+i*spacing}" cy="{y}" r="9" fill="{B if v else R}"/>' for i,v in enumerate(values))
def split(stage=0):
 s=txt(560,35,'Eight training examples: four yes, four no',28,I,'middle')+dots(445,80,[1,1,1,1,0,0,0,0])
 s+=box(405,130,310,60,'Feature ≤ threshold?')
 s+=arrow(460,190,280,255)+arrow(660,190,845,255)+txt(350,224,'yes',21,M)+txt(740,224,'no',21,M)
 s+=dots(205,283,[1,1,1,0])+dots(770,283,[1,0,0,0])
 if stage:s+=txt(260,337,'H = 0.811 bits',25,B,'middle')+txt(830,337,'H = 0.811 bits',25,B,'middle')+txt(560,393,'Gain = 1 − (4/8 × 0.811 + 4/8 × 0.811) = 0.189 bits',26,I,'middle')
 else:s+=txt(260,340,'3 yes · 1 no',25,M,'middle')+txt(830,340,'1 yes · 3 no',25,M,'middle')
 return svg(s)
def confusion():
 s=txt(335,34,'Predicted label',25,M,'middle')+txt(245,80,'positive',24,B,'middle')+txt(455,80,'negative',24,B,'middle')
 for x,y,label,c,fill in [(145,100,'TP = 18',G,'#DCF0EA'),(355,100,'FN = 2',R,'#FBE9EE'),(145,220,'FP = 12',R,'#FBE9EE'),(355,220,'TN = 68',G,'#DCF0EA')]:s+=box(x,y,200,100,label,c,fill,30)
 s+=txt(125,158,'positive',22,M,'end')+txt(125,278,'negative',22,M,'end')+txt(30,370,'Actual labels are the rows.',23,M)
 s+=txt(640,115,'Precision = 18 / 30 = 0.60',29,B)+txt(640,205,'Recall = 18 / 20 = 0.90',29,B)+txt(640,295,'Accuracy = 86 / 100 = 0.86',29)+txt(640,370,'100 illustrative examples',23,M)
 return svg(s)

def axes(x=65,y=345,w=440,h=280,xlabel='x',ylabel='y'):
 return arrow(x,y,x+w,y,M)+arrow(x,y,x,y-h,M)+txt(x+w,y+35,xlabel,23,M,'end')+txt(x-15,y-h-12,ylabel,23,M)
def path(points,c=B,w=3,dash=''):
 return '<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
def fit():
 s=axes(xlabel='model flexibility',ylabel='error')
 s+=path([(70+i*4,95+220*(1-math.exp(-i/26))) for i in range(100)],B)
 s+=path([(70+i*4,175+.018*(i-45)**2) for i in range(100)],R)
 s+=txt(280,330,'training',22,B)+txt(380,210,'validation',22,R)
 # Curves plotted as screen y: lower screen y means higher error; fix U via minimum error at center.
 s=s.replace(path([(70+i*4,175+.018*(i-45)**2) for i in range(100)],R),path([(70+i*4,290-.047*(i-45)**2) for i in range(100)],R))
 s+=txt(620,105,'Too rigid',32)+txt(620,145,'Misses the pattern → high bias',25,M)+txt(620,220,'Too flexible',32)+txt(620,260,'Changes with the sample → high variance',25,M)+txt(620,345,'Choose using held-out performance.',25,B)
 return svg(s)
def cv():
 s=''
 for row in range(5):
  s+=txt(40,60+row*65,f'Fit {row+1}',24,M)
  for col in range(5):s+=box(165+col*165,24+row*65,145,48,'validate' if row==col else 'train',G if row==col else B,'#DCF0EA' if row==col else T,22)
 s+=txt(560,397,'Select settings from mean validation score; test once at the end.',25,I,'middle')
 return svg(s)
def regression(stage=0):
 s=axes(xlabel='x',ylabel='y');px=lambda x:70+x*120;py=lambda y:345-y*48
 for x,y in [(1,2),(2,3),(3,5)]:
  s+=f'<circle cx="{px(x)}" cy="{py(y)}" r="7" fill="{I}"/>'
  if stage:s+=line(px(x),py(y),px(x),py(1.5*x+1/3),R,3)
 if stage:s+=line(px(0),py(1/3),px(3.8),py(1.5*3.8+1/3),B,3)
 s+=txt(615,85,'ŷ = w x + b',39,B)+txt(615,150,'Data: (1, 2), (2, 3), (3, 5)',25)
 if stage:s+=txt(615,220,'w = 1.5     b = 1/3',31)+txt(615,280,'Residuals: 1/6, −1/3, 1/6',26,M)+txt(615,345,'SSE = 1/6     MSE = 1/18',28,B)
 else:s+=txt(615,240,'Find one slope and one intercept.',27,M)
 return svg(s)
def geometry():
 s=arrow(130,340,450,160,B)+arrow(130,340,710,80,R)+arrow(450,160,710,80,G)
 s+=line(20,390,710,2,L,2)+txt(165,295,'ŷ = Xβ',29,B)+txt(405,125,'y',32,R)+txt(590,164,'r = y − ŷ',28,G)
 s+=txt(770,130,'Xᵀr = 0',37,B)+txt(750,220,'Residual is orthogonal',26)+txt(750,260,'to every column of X.',26)+txt(130,400,'Schematic: fitted vector lies in the column space of X.',24,M)
 # Deliberate correct orthogonal residual: fit vector (320,-180), residual (90,160).
 s=arrow(130,340,550,100,B)+arrow(130,340,670,310,R)+arrow(550,100,670,310,G)+line(60,380,665,35,L)+txt(275,200,'ŷ = Xβ',29,B)+txt(380,360,'y',32,R)+txt(620,185,'r',29,G)+txt(770,130,'Xᵀr = 0',37,B)+txt(750,220,'Residual is orthogonal',26)+txt(750,260,'to every column of X.',26)+txt(130,400,'Schematic: fitted vector lies in the column space of X.',24,M)
 return svg(s)
def gd(rate=.1):
 vals=[4.0]
 for i in range(4):vals.append(vals[-1]*(1-2*rate))
 px=lambda w:285+22*w
 py=lambda w:345-3.3*w*w
 s=axes(xlabel='w',ylabel='J(w) = w²')
 s+=path([(px(-9+i*.18),py(-9+i*.18)) for i in range(101)],B)
 points=[(px(w),py(w)) for w in vals]
 s+=path(points,R,2,'5 4')
 for i,(x,y) in enumerate(points):s+=f'<circle cx="{x}" cy="{y}" r="5" fill="{R}"/>'
 s+=txt(px(4)+10,py(4)-12,'start: 4',21,R)+txt(px(0),378,'0',20,M,'middle')
 s+=txt(610,85,'w ← w − η · 2w',39,B)+txt(610,160,f'η = {rate:g}',31)
 s+=txt(610,235,' → '.join(f'{x:.2f}' for x in vals[:3]),29)+txt(610,295,' → '.join(f'{x:.2f}' for x in vals[3:]),29)
 s+=txt(610,370,'Red dots: successive parameter values.',23,M)
 return svg(s)

def sigmoid():
 s=axes(xlabel='score z',ylabel='p(y = 1)');s+=path([(70+i*4,345-280/(1+math.exp(-(i-50)/10))) for i in range(101)])
 s+=line(65,205,475,205,L,2,'6 4')+txt(72,196,'0.5',23,M)+txt(595,95,'z = wᵀx + b',35)+txt(595,175,'p = 1 / (1 + exp(−z))',35,B)+txt(595,260,'z = 0  →  p = 0.5',30)+txt(595,320,'z ≈ 2.20  →  p ≈ 0.90',30)
 return svg(s)
def xor(stage=0):
 s=axes(xlabel='x₁',ylabel='x₂')
 for x,y,v in [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]:
  xx=140+270*x;yy=295-195*y;s+=f'<circle cx="{xx}" cy="{yy}" r="19" fill="{B if v else R}"/>'+txt(xx+33,yy+8,str(v),27)
 if stage:s+=line(70,245,350,50,B,3,'8 5')+line(220,345,500,150,B,3,'8 5')
 s+=txt(620,95,'h₁ = ReLU(x₁ + x₂)',30,B)+txt(620,160,'h₂ = ReLU(x₁ + x₂ − 1)',30,B) if stage else txt(620,135,'Opposite corners share a class.',29)+txt(620,235,'One straight boundary fails.',29,R)
 if stage:s+=txt(620,255,'ŷ = h₁ − 2h₂',38)+txt(620,340,'Outputs at the four corners: 0, 1, 1, 0',23,M)
 return svg(s)
def network():
 s='';xs=[120,460,850];ys=[[145,285],[95,215,335],[215]]
 for layer in range(2):
  for a in ys[layer]:
   for b in ys[layer+1]:s+=line(xs[layer]+24,a,xs[layer+1]-24,b,L,2)
 for k,x in enumerate(xs):
  for j,y in enumerate(ys[k]):s+=f'<circle cx="{x}" cy="{y}" r="28" fill="{T}" stroke="{B}" stroke-width="2"/>'+txt(x,y+8,('x' if k==0 else 'h' if k==1 else 'ŷ')+('₁₂₃'[j] if k<2 else ''),22,B,'middle')
 s+=txt(290,385,'2 × 3 + 3 = 9',27,B,'middle')+txt(680,385,'3 × 1 + 1 = 4',27,B,'middle')+txt(1040,225,'13',47,B,'middle')+txt(1040,267,'parameters',20,M,'middle')
 return svg(s)
def graph(stage=0,shared=False):
 if shared:
  return svg(box(40,160,150,70,'x = 3')+arrow(190,177,430,190)+arrow(190,218,430,225)+box(430,165,220,80,'f = x × x = 9')+txt(760,160,'Two paths to x',33)+txt(760,235,'∂f/∂x = x + x = 6',30,B)+txt(170,80,'Each use contributes a gradient; add both.',29,M))
 s=box(20,60,150,60,'x = 2')+box(20,270,150,60,'y = 3')+arrow(170,90,350,190)+arrow(170,300,350,220)+box(355,160,220,80,'a = x + y = 5')+arrow(575,200,770,200)+box(605,40,155,60,'z = 4')+arrow(760,100,835,158)+box(775,160,305,80,'f = a × z = 20')
 if stage:s+=txt(820,310,'∂f/∂a = z = 4',27,G)+txt(610,35,'∂f/∂z = a = 5',24,G)+txt(170,375,'∂f/∂x = 4 × 1 = 4;    ∂f/∂y = 4 × 1 = 4',28,G)
 else:s+=txt(400,345,'Forward: compute and retain intermediate values.',27,M)
 return svg(s)
def context():return rows(['Context (5 characters)','Target'],[['. . . . .','n'],['. . . . n','i'],['. . . n i','p'],['. . n i p','u'],['. n i p u','n'],['n i p u n','. (end)']],[650,410])
def names():
 s='';items=[('5 IDs','B × 5'),('Embedding','B × 5 × 4'),('Flatten','B × 20'),('Hidden','B × 64'),('Logits','B × V')]
 for i,(label,shape) in enumerate(items):
  x=15+i*224;s+=box(x,140,190,78,label,size=26)+txt(x+95,270,shape,24,M,'middle')
  if i<4:s+=arrow(x+195,180,x+219,180)
 s+=txt(560,65,'A next-character model is a classifier at every step',30,I,'middle')+txt(560,360,'V is the vocabulary size; the embedding table is learned.',26,B,'middle')
 return svg(s)
def bars(labels,values):
 s=''
 for i,(label,v) in enumerate(zip(labels,values)):
  y=50+i*85;s+=txt(110,y+30,label,29,anchor='end')+f'<rect x="145" y="{y}" width="{v*750}" height="45" rx="3" fill="{B}"/>'+txt(170+v*750,y+32,f'{v:.3f}',27)
 return svg(s+txt(560,385,'Illustrative probabilities; not predictions from a trained model.',23,M,'middle'))
def timeline():return rows(['Minutes','Revision focus'],[['0–7','Data, tasks and evaluation'],['7–16','Trees, model selection and ensembles'],['16–28','Regression, optimization and ridge'],['28–39','Logistic regression and MLPs'],['39–51','Next-token prediction and autograd'],['51–55','Synthesis and exit questions']],[230,830])

def basis():
 s=axes(xlabel='x',ylabel='ŷ')
 s+=path([(80+i*4,320-.022*(i-10)**2) for i in range(101)],B)
 s+=txt(630,70,'x → [1, x, x²]',36,B)+txt(630,160,'ŷ = β₀ + β₁x + β₂x²',34)+txt(630,250,'Curved in x',30)+txt(630,295,'Linear in β₀, β₁, β₂',30,B)+txt(630,375,'Choose the basis using validation.',23,M)
 return svg(s)
