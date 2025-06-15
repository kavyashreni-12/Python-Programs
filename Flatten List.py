def flat(num):
    flatlist=[]
    for element in num:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist

num=[1,2,3,[4,5],[6,7,8],9]
print('List',num)
print('Flat list', flat(num))
