def select_gridChallenge(grid):
    orderedGrid = [sorted(x) for x in grid]
    for i, string in enumerate(orderedGrid):
        if (i) != len(string):
            newString = ''.join([x[i] for x in orderedGrid])
            if newString!=''.join(sorted(newString)):
                return 'NO'
    return 'YES'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = select_gridChallenge(grid)

        print(result)
        print(grid)