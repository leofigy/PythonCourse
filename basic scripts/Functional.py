import sys

def PowerB(a=1, b=4):
    return a**b


def main():
    """ Functional programming concepts """
    print """Lambda functions, are like light functions, and they have no name, 
            they can return only one argument example
            z = Lambda a, b: a**b
            """
    """ generating a list of numbers """
    z = range(10)
    b = 4
    power_b = lambda a, b:a**b
    """ now using a list comprehesion """
    #z_power_b = [zi**b for zi in z] another way to do it directly
    z_power_b = [power_b(zi, b) for zi in z]
    print "original : {0} \n changed: {1}".format(z, z_power_b)
    
    print """\n More mappings \n result = map(function, sequence)"""
    z_map = map(lambda a: a**3, z)
    z_Map = map(lambda j:j % 2 == 0, z)
    z_Filter = filter(lambda j:j % 2 ==0, z)
    print "mapped {0}, \n {1}".format(z_map, z_Map)

    print """ \n Filtering \n result = filter(function, sequence) if function returns true then returns the element to the list """
    names = ["Ana", "Imelda", "Rox", "Rosalba", "Erika", "Ivette", "Josefa" ]
    names_filter = filter(lambda l:len(l)>4, names)
    print "Normal: {0}, \n Filtered :{1}".format(names, names_filter)
    print "Normal: {0}, \n Filtered :{1}".format(z, z_Filter)

    print """ \n reducing elements result = reduce(function, sequence) returns a single value example"""
    m = range(10)
    m_reduced = reduce(lambda x, y:x+y, m)

    print "Normal: {0}, \n Reduced :{1}".format(m, m_reduced)

if __name__ == '__main__':
    main()


