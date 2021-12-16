def print_triangle(n):
    if n == 1:
        print('*')
    else:
        print_triangle( n - 1 )
        for i in range(n):
            print('*',end ='')
        print('')


#print_triangle(4)


def print_oposite_triangles(n):
    if n == 1:
        print('*')
        print('*')
    else:
        for i in range(n):
            print('*',end ='')
        print('')
        print_oposite_triangles( n-1 )
        for i in range(n):
            print('*',end ='')
        print('')
#print_oposite_triangles(4)

def print_ruler(n):
    if n == 2:
        print('-')
        for i in range(n):
            print('-', end = '')
        print()
        print('-')
    else:
        print_ruler(n-1)
        for i in range(n):
            print('-', end = '')
        print()
        print_ruler( n - 1 )




#print_ruler(4)
