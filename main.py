from core.agent import BaseAgent

def main():
    print("🚀 LocalMLL-Agent 正在启动...")
    
    agent = BaseAgent()
    response = agent.run("你好，我是用户")
    print(response)
    
    print("✅ 系统初始化完成，等待指令...")

if __name__ == "__main__":
    main()