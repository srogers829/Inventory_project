
order_guide = dict() #master 
mod_guide = dict() #dictionary of mods to be made to master
fill_guide = dict() #dictionary to be compared to master and retieve differences between values


def guide_conf():
    for item in order_guide.items():
        print(item)
    conf = input('does this look correct? (yes/no): ').lower()
    if conf != 'yes':
        print('Sorry about that let\'s start again.')
    else:
        return order_guide
def master():
    print('Please enter item name and necessary par, enter \'q\' to quit')
    while True:                
        usr_item = input('Item:')
        if usr_item == 'q':
            break
        par = input('Par:')
        if usr_item == 'q':
            break
        order_guide[usr_item] = par
    confirm = guide_conf()
    return confirm 

def mods():
    while True:           
        usr_item1 = input('Item:')
        if usr_item1 == 'q':           
            return mod_guide
        par1 = input('Par:')
        if par1 == 'q':              
            return mod_guide      
        mod_guide[usr_item1] = par1
        order_guide.update(mod_guide)

def fill_order():
    amounts = dict()
    fill_guide = order_guide.copy()
    for k in fill_guide:
        print(k)
        v = input('O/H: ')
    amounts[k] = v
    return amounts
    