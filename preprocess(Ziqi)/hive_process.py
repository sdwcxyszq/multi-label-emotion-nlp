result = open('result.csv','w',encoding='utf-8')
result.writelines('id\ttext\tlabel')
id=1
with open('part-00000','r',encoding='utf-8') as file1:
    for line in file1:
        result.writelines(str(id)+'\t'+line)
        id+=1
with open('part-00001','r',encoding='utf-8') as file2:
    for line in file2:
        result.writelines(str(id) + '\t' + line)
        id += 1
with open('part-00002','r',encoding='utf-8') as file3:
    for line in file3:
        result.writelines(str(id) + '\t' + line)
        id += 1
result.close()