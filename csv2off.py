#############################################################
#csv2off.py: Convert Fluent result data (.csv) to .off file.#
#Author: Jialei Shen                                        #
#Latest: Jan 28, 2019                                       #
#############################################################

from numpy import *
import pandas as pd
import math

def csv2off(csvname,component, direction = False):
    csvdata = pd.read_csv(csvname)
    d = 'direction' if direction else ''
    myoff = open('myoffdata_'+component+'_'+str(d)+'.off','w')
    myoff.write('NCOFF\n')
    columns = array(csvdata[['cell ID','x-coordinate','y-coordinate','z-coordinate','velocity-magnitude','x-velocity','y-velocity','z-velocity','pollutant']])
    vm = []
    po = []
    myoff.write(str(len(columns))+' 0 0\n')
    for c in columns:
        vm.append(c[4])
        po.append(c[8])
    
    for c in columns:
        if direction:
            if component == 'velocity' or component == 'v':
                myoff.write(str(c[1])+' '+str(c[2])+' '+str(c[3])+' '+str(num2rgba(min(vm),max(vm),c[4])[0])+' '+str(num2rgba(min(vm),max(vm),c[4])[1])+' '+str(num2rgba(min(vm),max(vm),c[4])[2])+' '+str(num2rgba(min(vm),max(vm),c[4])[3])+' '+str(c[5]/magnitude([c[5],c[6],c[7]]))+' '+str(c[6]/magnitude([c[5],c[6],c[7]]))+' '+str(c[7]/magnitude([c[5],c[6],c[7]]))+'\n')
            elif component == 'pollutant' or component == 'p':
                myoff.write(str(c[1])+' '+str(c[2])+' '+str(c[3])+' '+str(num2rgba(min(po),max(po),c[4])[0])+' '+str(num2rgba(min(po),max(po),c[4])[1])+' '+str(num2rgba(min(po),max(po),c[4])[2])+' '+str(num2rgba(min(po),max(po),c[4])[3])+' '+str(c[5]/magnitude([c[5],c[6],c[7]]))+' '+str(c[6]/magnitude([c[5],c[6],c[7]]))+' '+str(c[7]/magnitude([c[5],c[6],c[7]]))+'\n')
            else:
                print('Error: Please select eithor "velocity" or "pollutant" to show')
                break
        else:
            if component == 'velocity' or component == 'v':
                myoff.write(str(c[1])+' '+str(c[2])+' '+str(c[3])+' '+str(num2rgba(min(vm),max(vm),c[4])[0])+' '+str(num2rgba(min(vm),max(vm),c[4])[1])+' '+str(num2rgba(min(vm),max(vm),c[4])[2])+' '+str(num2rgba(min(vm),max(vm),c[4])[3])+' 0 0 0 '+'\n')
            elif component == 'pollutant' or component == 'p':
                myoff.write(str(c[1])+' '+str(c[2])+' '+str(c[3])+' '+str(num2rgba(min(po),max(po),c[4])[0])+' '+str(num2rgba(min(po),max(po),c[4])[1])+' '+str(num2rgba(min(po),max(po),c[4])[2])+' '+str(num2rgba(min(po),max(po),c[4])[3])+' 0 0 0 '+'\n')
            else:
                print('Error: Please select eithor "velocity" or "pollutant" to show')
                break
    myoff.close()

def num2rgba(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)    
    halfmax = (minimum + maximum) / 2
    a = 255
    if minimum <= value <= halfmax:
        r = 0
        g = int( 255./(halfmax - minimum) * (value - minimum))
        b = int( 255. + -255./(halfmax - minimum)  * (value - minimum))
        return (r,g,b,a)    
    elif halfmax < value <= maximum:
        r = int( 255./(maximum - halfmax) * (value - halfmax))
        g = int( 255. + -255./(maximum - halfmax)  * (value - halfmax))
        b = 0
        return (r,g,b,a)
    
def magnitude(v1):
    v1m = math.sqrt(v1[0]*v1[0]+v1[1]*v1[1]+v1[2]*v1[2])
    return v1m


def main():
    print('Runing...')
    csv2off('caseroom0123-data-indoor.csv','velocity',0)
    print('Done!')

if __name__ == "__main__":
    main()

    
