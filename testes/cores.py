
"""
    db = {
        1: {
            "title": "",
            "description": "",
            "status" : ""
        },
        2: {
            "title": "",
            "description": "",
            "status" : ""
        }
        3: {
            "title": "",
            "description": "",
            "status" : ""
        }
    }

    db: dict[int, dict[str, str]]


    atual:

    db: list[dict[ str, int | str]]

    db = [
        {
            "id" : 0,
            "title": "",
            "description": "",
            "status" : ""
        },
        {
            "id" : 1,
            "title": "",
            "description": "",
            "status" : ""
        },
        {
            "id" : 2,
            "title": "",
            "description": "",
            "status" : ""
        },
    ]

"""



from time import clock_getres, sleep

def color(r:int = 0, g: int = 0, b:int = 0,*, fundo = False, reset= False):
    if reset: return f"\033[0m"
    plano = 38 if not fundo else 48
    return f"\033[{plano};2;{r};{g};{b}m"



#for ID in range(0, 256):
#    print(f"\033[48;5;{ID}m testes \033[0m")

"""for r in range(0,256):
    print(f"{color(r,0,0)} testes {color(reset=True)}", end="")

print(color(reset=True), "verde")

for g in range(0, 256):
    print(f"{color(0,g,0,)} testes {color(reset=True)}", end="")

print(color(reset=True), "azul")


for b in range(0, 256):
    print(f"{color(0,0,b,)} testes {color(reset=True)}", end="")
print(color(reset=True))"""

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
    

