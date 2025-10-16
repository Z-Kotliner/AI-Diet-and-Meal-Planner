from typing import Dict, Any

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel

dotenv.load_dotenv()


class LLMClient:
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.6, max_retries=2)

    def call_model_json(self, prompt: str, response_model: BaseModel) -> Dict[str, Any]:
        # Define the prompt template
        prompt_template = PromptTemplate(input_variables=["prompt"], template=prompt)

        # Define the JSON parser
        parser = JsonOutputParser(pydantic_object=response_model)

        # Create the chain of operations (prompt->llm->parsing)
        chain = prompt_template | self.llm | parser

        # Invoke the chain and get the final response after parsing
        response = chain.invoke({"prompt": prompt})

        return response
