
def findMaxDifference(items_count,items):
    temp=0
    items_list=items.split(" ")
    for each_item in items_list:
        if items_list.index(each_item)+1 != items_count:
            firstelement=each_item
            secondelement=items_list[items_list.index(each_item)+1]
            difference=int(firstelement)-int(secondelement)
            if difference>0 and temp<difference:
                temp=difference
    return temp

a=int(input())
aa=input()
print(findMaxDifference(a,aa))