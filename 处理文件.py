import json
if  __name__ == '__main__':

    #datas.json文件处理
    with open('./datas.json',"r",encoding='utf8') as f:
        data = json.loads(f.read())
    save_file = open('input.txt',"a+",encoding='utf8')
    for i in data['like_uin_info']:
        save_file.write(str(i['nick'])+"\n"+str(i["fuin"])+"\n")
    print("datas done")

    #data4.json文件
    with open('./data4.json',"r",encoding='utf8') as f:
        data = json.loads(f.read())
    save_file = open('input.txt',"a+",encoding='utf8')
    for i in data:
        save_file.write(str(i['nick'])+"\n"+str(i["fuin"])+"\n")
    print("data4 done")


    #data3.json文件
    with open('./data3.json',"r",encoding='utf8') as f:
        data = json.loads(f.read())
    save_file = open('input.txt',"a+",encoding='utf8')
    for i in data:
        fuin,nick,_ = i
        save_file.write(str(nick)+"\n"+str(fuin)+"\n")
    print("data3 done")


    # comment.json
    with open('./comment.json', "r", encoding='utf8') as f:
        data = json.loads(f.read())
    save_file = open('input.txt', "a+", encoding='utf8')
    for i in data:
        fuin = i["uin"]
        nick = i["name"]
        save_file.write(str(nick) + "\n" + str(fuin) + "\n")
    print("comment done")

    #comment2.json
    with open('./comment2.json',"r",encoding='utf8') as f:
        data = json.loads(f.read())
    save_file = open('input.txt',"a+",encoding='utf8')
    for i in data:
        fuin = i["poster"]["id"]
        nick=  i["poster"]["name"]
        save_file.write(str(nick)+"\n"+str(fuin)+"\n")
    print("comment2 done")