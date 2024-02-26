from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
load_dotenv()


chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
system = "You are a presales engineer who has a experience in telco domain over 15 years. you can explain any technical details to the customer."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat

while True:
    userinp = input(">>>")
    result = chain.invoke({"text": userinp})
    print(result.content)