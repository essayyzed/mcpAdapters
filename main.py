import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import StdioServerParameters

load_dotenv()
 
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

stdio_server_params = StdioServerParameters(
    command = "python",
    args = ["/Users/essayyzed/temp/mcp-server/mcpAdapters/servers/math_server.py"],
)

async def main():
    print("Hello from mcpadapters!")


if __name__ == "__main__":
    asyncio.run(main())
