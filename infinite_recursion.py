#
#infinite_recursion.py
#
def recursion_depth(number):
    print("Recursion Depth Number %d." % number);
    try:
        recursion_depth(number + 1);
    except:
        print('Maximum Recursion Depth Exceeded');
        
    

recursion_depth(0);
