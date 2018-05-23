a=input("hello what is your name")
print("hello",a)

print("The game is about selecting two marvel characters and two are alloted by default to fight against thanos")
print("select any marvel character from the list given:")
print('doctor strange, scarlet witch, hulk, nebula, gamora, drax, thor, black panther, spider man, black widow')

ironman=10
captainamerica=9
thanos=35
c=input("type here 1st name ")
if c== "doctor strange":
    d=10
    print("score 10")
if c== "scarlet witch":
    d=9
    print("score 9")
if c== "hulk":
    d=8
    print("score 8")
if c== "nebula":
    d=6
    print("score 6")
if c== "gamora":
    d=7
    print("score 7")
if c== "drax":
    d=5
    print("score 5")
if c== "thor":
    d=10
    print("score 10")
if c== "black panther":
    d=8
    print("score 8")
if c== "spiderman":
    d=9
    print("score 9")
if c== "black widow":
    d=7
    print("score 7")

e = input("type here 2nd name ")
if e== "doctor strange":
    f=10
    print("score 10")
if e== "scarlet witch":
    f=9
    print("score 9")
if e== "hulk":
    f=8
    print("score 8")
if e== "nebula":
    f=6
    print("score 6")
if e== "gamora":
    f=7
    print("score 7")
if e== "drax":
    f=5
    print("score 5")
if e== "thor":
    f=10
    print("score 10")
if e== "black panther":
    f=8
    print("score 8")
if e== "spiderman":
    f=9
    print("score 9")
if e== "black widow":
    f=7
    print("score 7")

print('total score = captain america + ironman + 1st name + 2nd name')
print("total score=",captainamerica + ironman + d + f)

total_score = captainamerica + ironman + d + f
if total_score <= thanos :
    print("your team lost with thanos")
else:
    print('your team defeated thanos')