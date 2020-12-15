import utils.get_input

def bubble_sort(list):
    for i in range (len(list)-1):
        for j in range (i, len(list)-1):
            if list[j] > list[j+1]:
                #swap 2 items at this index
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

def main():
    lst = utils.get_input.list("")
    bubble_sort(lst)
    print(lst)

main()