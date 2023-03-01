result = open('result.json','w',encoding='utf-8')
result.write('[')
with open('part-00000','r',encoding='utf-8') as file1:
    for line in file1:
        result.writelines(line+',')
with open('part-00001','r',encoding='utf-8') as file2:
    for line in file2:
        result.writelines(line+',')
with open('part-00002','r',encoding='utf-8') as file3:
    for line in file3:
        result.writelines(line+',')
result.write(']')
result.close()