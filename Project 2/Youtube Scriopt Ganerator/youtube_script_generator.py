from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

def main():
    llm = ChatOpenAI(
        model_name="gpt-4",      
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)

    topic = input("Enter the topic for your YouTube video: ")

    script = chain.run(topic=topic)
    print("\nGenerated YouTube Script:\n")
    print(script)

if __name__ == "__main__":
    main()
