from visualiser.visualiser import Visualiser as vs
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})

def lis(A, current, prev):
    """
    this solution is 2^n solution as there are 2 recursive call 

    """
    print(current, prev)
    if len(A) == current:
        return 0
    else:
        c1 = 0
        if prev == -1 or A[prev] < A[current]:
            c1 = 1 + lis(A, current = current+1, prev=current)
        c2 = lis(A, current=current+1, prev=prev)
        return max(c1, c2)


def main():
    # Call function
    print(lis([-4, 10, 3, 7, 15], 0, -1))
    # Save recursion tree to a file
    vs.make_animation("lis.gif", delay=2)


if __name__ == "__main__":
    main()