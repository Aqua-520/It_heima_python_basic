# 定义一个字典类型
user_info = {
    'name': '黄一个',
    'age': 18,
    'gender': '男',
    'hobby': ['看电影', '敲代码']
}

# 对字典进行序列化操作
from json import load, dump

with open('./resources/user_config.json', mode='w', encoding='utf-8') as file_obj:
    # 写入文件
    dump(user_info, file_obj, ensure_ascii=True, indent=4)

# 反序列化读取
with open('./resources/user_config.json', mode='r', encoding='utf-8') as file_obj:
    # 读取文件
    content = load(file_obj)
    print(content)
