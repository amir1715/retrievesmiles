import sys,os,codecs
from urllib.request import urlopen
def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + ids + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'

file_name=str(input('please input the path to the file containing CAS numbers or names:'))
file_out=str(input('please input the name of the output file:'))
f_out = codecs.open(os.path.join(os.getcwd(),file_out),mode='a',encoding='utf-8')
ids_file=open(os.path.join(os.getcwd(),file_name),'r')
for line in ids_file.readlines():
    line=line.replace('\n', '')
    line=line.split(",")[-1]
    smi=CIRconvert(line)
    if not smi in 'Did not work':
        new_f=codecs.open(os.path.join(os.getcwd(),line+'.smi'),mode='a',encoding='utf-8')
        new_f.write(smi)
        new_f.close()
    res=line+'\t'+smi
    print(str(res))
    f_out.write(str(res)+'\n')
f_out.close()
print('The SMILES are saved in '+ file_out)