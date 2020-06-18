keep_going = 'y'
while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commision rate: '))

    commission = sales * comm_rate

    print('The commission is $',
          format(commission, ',.2f'), sep = '')

    keep_going = input('Do you want to calcuate anoter ' +
                       'commision (Enter y for yes): ')
