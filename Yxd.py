from mcp.server.fastmcp import FastMCP
import json
import requests
from requests.exceptions import Timeout

# 创建一个MCP服务器
mcp = FastMCP("Yxd")

# 添加一个加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """两个数字相加"""
    return a + b

@mcp.tool()
def Plan(inputregno:str,inputuser:str):
    """我的计划"""
    datas = []
    url = "http://101.132.27.9:8090/openapi/gfspdf/plandata"
    params = {
        "inputregno": inputregno,
        "inputuser": inputuser
    }
    response = requests.post(url, json=params, timeout=30)
    if response.status_code == 200:
        datas = response.json()
    else :
        print('接口失败！')
    return datas

# 添加一个动态问候资源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """问候"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()