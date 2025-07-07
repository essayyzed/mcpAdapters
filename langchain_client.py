from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
import asyncio

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


async def main():
    # Create the client without using it as a context manager
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/essayyzed/temp/mcp-server/mcpAdapters/servers/math_server.py"
                ],
                "transport": "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse"
            },
        }
    )
    
    # Get tools directly from the client
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    result = await agent.ainvoke({"messages": "what is the weather in SF?"})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
