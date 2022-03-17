def cat_strings(a):
    dic = { "R":"R'", "R'":"R",
            "L":"L'", "L'":"L", 
            "D":"D'", "D'":"D", 
            "U":"U'", "U'":"U", 
            "F":"F'", "F'":"F", 
            "B":"B'", "B'":"B" }
    arr  = a.split()
    print(arr)
    newArr = list(map(lambda c: dic(c), arr))
    print(newArr)
    solv = (" ").join(newArr)
    print("%s" % solv)
