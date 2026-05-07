import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
# 注意：本地模型通常不带搜索功能，为了演示稳定，这里先暂时去掉搜索工具
# 如果你想用搜索，需要确保你的本地模型支持 Function Calling (工具调用)

class BaseAgent:
    def __init__(self):
        self.name = "LocalMLL-Agent"
        self.version = "0.1.0"
        
        # --- 修改重点在这里 ---
        # 我们不再使用默认的 OpenAI 地址，而是指向本地 LM Studio
        self.llm = ChatOpenAI(
            model="local-model", # 模型名字随便填，LM Studio 会忽略它，直接用加载的模型
            openai_api_base="http://localhost:1234/v1", # 指向本地地址
            openai_api_key="lm-studio", # 随便填，本地不需要校验密钥
            temperature=0.7,
            verbose=False 
        )
        # -------------------

        # 暂时去掉工具，因为本地小模型处理工具调用容易出错
        # 等跑通了，我们再研究怎么加搜索功能
        tools = [] 

        # 初始化智能体
        self.agent = initialize_agent(
            tools, 
            self.llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=True 
        )

    def run(self, prompt):
        try:
            print(f"🤖 {self.name} 正在思考 (本地运行)...")
            response = self.agent.run(prompt)
            return response
        except Exception as e:
            return f"出错了：{str(e)}"