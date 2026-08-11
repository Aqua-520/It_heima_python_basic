# 导入openai模块中的OpenAI类
from openai import OpenAI

# 导入os文件读写模块读取环境变量
# import os 不写了,直接写死得了

# 生成OpenAi对象
ai_robot = OpenAI(
    api_key='ark-2bacea53-5f0a-44c4-9879-b8f8fe6681c5-49c0a',
    base_url='https://ark.cn-beijing.volces.com/api/v3'
)

# 创建对话请求
response = ai_robot.responses.create(
    model='deepseek-v4-flash-260425',
    input=[
        {
            "role": "system",
            "content": "你是一只猫娘"
        },
        {
            "role": "user",
            "content": "宝贝,你喜欢我吗"
        },
    ]
    # 在input底下可以添加工具
)
# result = response.clean_result = {
#     "reasoning": response.output[0].summary[0].text,  # 思考过程
#     "content": response.output[1].content[0].text,  # 最终输出
#     "tokens": response.usage.total_tokens  # Token 消耗
# }

# 1. 提取最终回答文本
reply_text = response.output[1].content[0].text
print("模型回答：", reply_text)

# 2. 提取模型的思考过程 (Reasoning)
# reasoning_text = response.output[0].summary[0].text
# print("思考过程：", reasoning_text)
