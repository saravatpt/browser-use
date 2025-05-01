import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()
#api_key = os.getenv('GOOGLE_API_KEY')
#if not api_key:
#	raise ValueError('GOOGLE_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

async def main():
    agent = Agent(
        task="Go to amazon.in, search for Havells 1200 Watts Foldable Hair Dryer and buy it with cash on delivery option, delivery address is:46, 5th Cross, Chennakesava Layout, Valepura Village, Varthur, BENGALURU, KARNATAKA 560087, India, Phone number: 9600437108.",
        llm=llm,
        max_actions_per_step=4,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

# async def run_search():
# 	agent = Agent(
# 		task=(
# 			'Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result'
# 		),
# 		llm=llm,
# 		max_actions_per_step=4,
# 	)

# 	#await agent.run(max_steps=25)
# 	#await run_search()
# 	result = await agent.run()
# 	print(result)