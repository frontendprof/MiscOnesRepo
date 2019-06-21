# B_R_R
# M_S_A_W

# Enter random names to be sorted for you.
# When you have time you can work on it further, so it accepts inputs and capitalize every object of the given list.

def alphabetize(original_list=[]):
    original_list=input("Enter random names to be sorted: ").split()
    sorted_list = original_list.copy()

    sorted_list.sort()

    final_list = ''

    for name in sorted_list:
        final_list += name + ', '

    final_list = final_list[:-2]

    print(final_list)

alphabetize()
