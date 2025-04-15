import chainlit as cl
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)

@cl.on_message
async def main(message: cl.Message):
    system_msg = SystemMessage(content="You are a professional translator. Translate all incoming English text into Thai.")
    user_msg = HumanMessage(content=message.content)

    # Create placeholder message
    msg = cl.Message(content="")
    await msg.send()

    final_text = ""
    async for chunk in llm.astream([system_msg, user_msg]):
        if chunk.content:
            await msg.stream_token(chunk.content)
            final_text += chunk.content

    # ✅ Set content manually, then call update()
    msg.content = final_text
    await msg.update()
