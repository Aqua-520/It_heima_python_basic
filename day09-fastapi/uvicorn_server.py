# 导入server包
import uvicorn

if __name__ == '__main__':
    # 启动服务
    uvicorn.run("fast_api_demo01:api_demo", host="127.0.0.1", port=1086, reload=True)
