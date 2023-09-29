import json
import pickle
import hashlib
import pprint
if __name__ == '__main__':
    list = {}
    with open('input.txt','r',encoding='utf8') as f:
        datas = f.readlines()
    print(len(datas))
    for i in range(0,len(datas),2):
        name = datas[i][:-1]
        nummber = datas[i+1][:-1]
        print(datas[i][:-1],datas[i+1][:-1])
        hash_object = hashlib.sha256(name.encode('utf-8'))
        list.update(
            {
                nummber:{
                    'hash': hash_object.hexdigest(),
                    'value': hash_object.digest(),
                    'name': name,
                    'number': nummber
                }
            }
        )
    with open('namelist.bin','wb') as f:
        pickle.dump(list,f)

    pprint.pprint(list)
    print(len(list))

