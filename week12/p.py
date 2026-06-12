import numpy as np, math, pandas as pd
def f1(x):
    return ((x[0]+1)**2)/9 + (x[1]+1)**2
def g1(x):
    return np.array([2*(x[0]+1)/9, 2*(x[1]+1)])
def f2(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2
def g2(x):
    x1,x2=x
    return np.array([2*(x1-1)-400*x1*(x2-x1**2), 200*(x2-x1**2)])
def f3(x):
    return 0.5*x[0]**2 + 25*x[1]**2
def g3(x):
    return np.array([x[0],50*x[1]])
def run(f,g,x0,alpha,beta=0,max_iter=1000):
    xs=[np.array(x0,dtype=float)]
    xprev=np.array(x0,dtype=float)
    x=np.array(x0,dtype=float)
    for k in range(max_iter):
        xn=x-alpha*g(x)+beta*(x-xprev)
        xs.append(xn.copy())
        xprev,x=x,xn
        if not np.all(np.isfinite(x)) or np.linalg.norm(x)>1e10:
            break
    vals=np.array([f(x) for x in xs])
    return np.array(xs), vals

# Test f1
for beta in [0,0.5,0.8,0.95]:
    xs,vals=run(f1,g1,[4,-4],0.3,beta,200)
    print('f1 beta',beta,'iters f<1e-6',np.argmax(vals<1e-6) if np.any(vals<1e-6) else None,'final',vals[-1], 'max',np.nanmax(vals))
# f2 tests
for beta in [0,0.5,0.8,0.9,0.95]:
    xs,vals=run(f2,g2,[-1.2,1.0],0.001,beta,5000)
    print('f2 beta',beta,'final',vals[-1], 'min',vals.min(), 'last x', xs[-1], 'finite', np.isfinite(vals).all(), 'iter<1e-4',np.argmax(vals<1e-4) if np.any(vals<1e-4) else None)
# f3 tests
for beta in [0,0.5,0.8,0.9]:
    xs,vals=run(f3,g3,[2,2],0.035,beta,200)
    print('f3 beta',beta,'final',vals[-1], 'max', vals.max(), 'finite', np.isfinite(vals).all(), 'iter<1e-6',np.argmax(vals<1e-6) if np.any(vals<1e-6) else None)
