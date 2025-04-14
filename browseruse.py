import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from google.colab import userdata
from browser_use import Agent

load_dotenv()
#os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
api_key = os.getenv('GOOGLE_API_KEY')
#if not api_key:
#	raise ValueError('GOOGLE_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


async def run_search():
	agent = Agent(
		task=(
			'Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result'
		),
		llm=llm,
		max_actions_per_step=4,
	)

	await agent.run(max_steps=25)