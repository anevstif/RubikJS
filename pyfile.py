def solver(a):
    dic = { "R":"R\'", "R'":"R",
            "L":"L\'", "L'":"L",
            "D":"D\'", "D'":"D",
            "U":"U\'", "U'":"U",
            "F":"F\'", "F'":"F",
            "B":"B\'", "B'":"B" }
    arr  = a.split()
    newArr = list(map(lambda c: dic.get(c, c), arr))
    arr = newArr[::-1]
    solv = (" ").join(arr)
    print(solv)
