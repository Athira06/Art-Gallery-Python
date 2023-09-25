def f():
    print("VISUAL  FOLKS")
    row = 3


    for i in range(row):
        for j in range(row):
            if i == 0 or i == row - 1:
                print("------------------------------------------------", end="")
            elif j == 0 or j == row - 1:
                  print("1.SEARCH            2.ARTIST            3.CUSTOMER            4.DROWING            5.COMPENATION", end="")
                  break

        print()
    row = 6
    for i in range(row):
        for j in range(row):
              print("****", end="")
        for j in range(row):
             print("  ", end="")
        for j in range(row):
             print("****", end="")
        for j in range(row):
             print("  ", end="")
        for j in range(row):
             print("****", end="")

        print()
    print("Abstract     Rs 1,65,000            seascap      Rs 4,50,000            Ganesha     Rs 4,10,0000   ")
    print("By Sanjay                           By Shamendu Sonavane                By Ganapathi Hegda  ")
    print("Acrylic on canvas                   Acrylic on canvas                   Oil on canvas")
    print("36*59 inches                        16*16 inches                        24*24 inches")
    print("\n")
    row = 6
    for i in range(row):
        for j in range(row):
            print("****", end="")
        for j in range(row):
            print("  ", end="")
        for j in range(row):
            print("****", end="")
        for j in range(row):
            print("  ", end="")
        for j in range(row):
            print("****", end="")

        print()
    print("Maharaas     Rs 4,52,000            Reflection     Rs 63,200            Tantric abstract Rs 10,000   ")
    print("By Dipti Kumar                      By Sanjay Chakrabarty               By Punekar  ")
    print("Oil on canvas                       Acrylic on canvas                   Acrylic on canvas ")
    print("24*24 inches                        13*14 inches                        36*36 inches  ")
    from mini_project import start
    start()
f()