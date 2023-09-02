""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a python code for Multi Arguments
"""

def test(*ls):
    ln = len(ls)
    for i in range(0, ln):
        print(ls[i], end=" ")
    print("")


test("Malek", "Ahmed")
test("Malek", "Ahemd", "Adel")
test("Malek", "Ahemd", "Adel", "Youssef")
print()


def test2(**args):
    print(f"length of args {len(args)}")
    ls = []
    for i in args.keys():
        ls.append(i)
        print(args[i])
    # print(ls[0])
    for i in ls:
        print(args[i])

    print()

test2(first="red", second="yellow")
test2(first="red", second="yellow", third="green")
