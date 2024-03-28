import twain

sm = twain.SourceManager(0)
print(sm)
ss = sm.OpenSource()
print(ss)
name = ss.GetSourceName()
print(name)  # FBH6315+

ss.RequestAcquire(0, 0)
rv = ss.XferImageNatively()
if rv:
    (handle, count) = rv
    twain.DIBToBMFile(handle, 'image.bmp')
