#######################################################################
#Student Name           :Sayak Ghosh
#ID                     :873464327
#Description of Program :Selection Sort
#######################################################################
list =[4,2,6]
def sort(list):
    idx =0
    output=[]
    for item in range(len(list)):
        if list[idx] < list[idx+1]:
            smallest = list[idx]
            save_idx = idx
            ouput += [list.pop[save_idx]]
