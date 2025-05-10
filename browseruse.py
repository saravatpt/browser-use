import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()


llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=os.getenv('GEMINI_API_KEY'))

async def main():
    agent = Agent(
        #task="Go to amazon.in, search for Havells 1200 Watts Foldable Hair Dryer and buy it with cash on delivery option, delivery address is:46, 5th Cross, Chennakesava Layout, Valepura Village, Varthur, BENGALURU, KARNATAKA 560087, India, Phone number: 9600437108.",
        task="goto google.com and search for bangalore weather and get the weather information",
        llm=llm,
        max_actions_per_step=4,
    )
    result = await agent.run()
    # result.save_as_playwright_script('playwright/script')
    
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