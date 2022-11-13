n=0
def test():
    print (n)
    m=1
    print (m)

test()
try:
    print (m)
except:
    print("failed")
    m=2

def test2():
    m=3
    print (m)
    def nested_func():
        print ("this works")
    nested_func()
    

test2()




