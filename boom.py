import os
from perplexipy import PerplexityClient

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")  
client = PerplexityClient(key=PERPLEXITY_API_KEY)

def generate_llm_prompt(tags):
    return f"""
    you are a tag classifier for www.commudle.com. your task is to read an array of tags, clean the data, and classify the tags into appropriate groups thoroughly.
    
    input format
    the input will be an array of tags represented in json format:
    [tag1, tag2, tag3, tag4, tag5]

    output format
    the output should be in json format and structured as follows:
    {{
        "cleaned_data": [
            {{
                "original_name": "value",
                "corrected_name": "corrected_value"
            }},
            ...
        ],
        "classified_data": [
            {{
                "category_name": "category_name",
                "tags": ["tag1", "tag2", "tag3"]
            }},
            ...
        ]
    }}

    instructions:
    analyze all the tags and clean the data.
    correct any spelling or formatting issues in the tags.
    classify them according to relevant categories, which may include technology groups, locations, names, or other nouns.
    return only the json output.
    ensure that one tag can belong to multiple categories.
    ensure that all output is in small case.
    consider all the tags mandatory to clean and classify.
    do not include any comments in the json output.

    Here is the list of tags you need to process:
    {tags}
    """

def handle_conversation(tags):
    llm_prompt = generate_llm_prompt(tags)
    result = client.query(llm_prompt)
    return result

if __name__ == "__main__":
    while True:
        user_input = input("Enter tags (comma-separated): ")

        if user_input.lower() == "exit":
            break

        tags = [tag.strip() for tag in user_input.split(',')]
        result = handle_conversation(tags)

        print("\nCleaned and Classified Tags:")
        print(result)