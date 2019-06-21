# B_R_R
# M_S_A_W

# Enter random names to be sorted for you.

def alphabetize(original_list=[]):
    original_list=input("Enter random names to be sorted: ")
    sorted_list = original_list.copy()

    sorted_list.sort()

    final_list = ''

    for name in sorted_list:
        final_list += name + ', '

    final_list = final_list[:-2]

    print(final_list)

alphabetize()
