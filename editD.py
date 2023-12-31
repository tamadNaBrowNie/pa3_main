from subprocess import check_call
from sys import executable
check_call([executable, "-m", "pip", "install", 'icecream'])

from icecream  import ic
def editDistance(src, tag):
    SUB,EQ,RM,INS ='s','m','d','i'
    m= len(src)
    n = len(tag)
    mat = [[0]*(n+1) for _ in range(m+1)]
    mat[0] = [*range(n+1)]
    ops = [['']*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):mat[i][0]=i
    def inner (i,j):
        pi,pj = i-1,j-1
        if src[pi]==tag[pj]:
            mat[i][j] = mat[pi][pj]
            ops[i][j] = ops[pi][pj]+EQ
            # print(EQ,f'pi {pi} pj {pj}')

        elif  mat[i][pj]<=mat[pi][pj] and mat[i][pj]<=mat[pi][j]:
            mat[i][j] = mat[i][pj]+1
            ops[i][j] = ops[i][pj]+INS
            # print(INS,f'i {i} pj {pj}')
            
        elif  mat[pi][pj]+1<=mat[pi][j] and mat[pi][pj]+1<=mat[pi][j]:
            mat[i][j] = mat[pi][pj]+2
            ops[i][j] = ops[pi][pj]+SUB
            # print(SUB,f'pi {pi} pj {pj}')
            
            
        elif  mat[pi][j]<=mat[pi][pj] and mat[pi][j]<=mat[i][pj]:
            mat[i][j] = mat[pi][j]+1
            ops[i][j] = ops[pi][j]+RM
            # print(RM,f'pi {pi} j {j}')
    def old(i,j):
        pi,pj = i-1,j-1
        mat[i][j] = mat[pi][pj] if src[pi]==tag[pj] else 1+min(mat[pi][j], mat[i][pj], mat[pi][pj]+1)
        val = mat[i][j] -1
        ops[i][j] = ''
        # print(i,j)
        # ic.disable()
        if src[pi]==tag[pj]:
            ops[i][j] = ops[pi][pj]+EQ
            ic(EQ,f'pi {pi} pj {pj}')
        elif  mat[pi][pj]+1 == val:
            ops[i][j]= ops[pi][pj]+SUB
            ic(SUB,f'pi {pi} pj {pj}')
        elif val==mat[pi][j]: 
            ops[i][j] = ops[pi][j]+RM
            ic(RM,f'pi {pi} j {j}')
        elif val == mat[i][pj]: 
            ops[i][j]=ops[i][pj]+INS
            ic(INS,f'i {i} pj {pj}')
        return ops[i][j]
        

            
    for i in range(1,m+1): 
        print(f'\n\ni {i}\n++++')
        for j in range(1, n + 1):
            # inner(i,j)
            print('\nj:',j)
            ic(old(i,j))
     

    trc_src, trc_tag =[],[]
    i,j = 0,0
    trace = ops[m][n]
    
    for c in trace:
        s,t ='',''
        if c==EQ or c==SUB:
            s,t=(src[i],tag[j])
            i+=1
            j+=1
        elif c==RM:
            s,t = (src[i],'_')
            i+=1
        elif c == INS:
            s,t=('>',tag[j])
            j+=1
        trc_src.append(s)
        trc_tag.append(t)
    trace = ' '.join(trace)
    s_trace = ' '.join(trc_src)
    t_trace = ' '.join(trc_tag)
    return (mat[m][n],'\n'.join((s_trace,trace, t_trace,'')))

editDistance("TAGCATCCCATGAC","CTTATATCCGT")