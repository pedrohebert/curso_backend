from time import sleep

def color(r:int = 0, g: int = 0, b:int = 0,*, fundo = False, reset= False):
    if reset: return f"\033[0m"
    plano = 38 if not fundo else 48
    return f"\033[{plano};2;{r};{g};{b}m"



cores = range(0,256)
rev_cores = list(reversed(cores))
r=0
g=0
b=0

rr=False
rg=False
rb=False

cr = cores[r]
cg = cores[r]
cb = cores[r]

while True:
    

    if not rr:
        cr = cores[r]
    else: 
        cr = rev_cores[r]
    if not rg:
        cg = cores[g]
    else: 
        cg = rev_cores[g]
    if not rb:
        cb = cores[b]
    else: 
        cb = rev_cores[b]

    print(f"{color(cr,cg,cb,fundo=True)}\n{color(reset=True)}", end="")

    sleep(0.016)
    r+=1
    g+=2
    b+=3
    if r > 255:
        rr= not rr
        r = 0
    if g > 255:
        rg = not rg
        g =0
    if b > 255:
        b = 0
        rb = not rb
    

