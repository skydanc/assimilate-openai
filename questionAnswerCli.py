#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Github Copilot to write this command-line interface.



import os
import openai
import click

def submit_question(text):
    """Submit a question to OpenAI API"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = text
    result = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-002"
    )["choices"][0]["text"].strip(" \n")
    return result

@click.command()
@click.argument("text")
def main(text):
    """Ask the OpenAI API a question to get an answer"""
    print(submit_question(text))

if __name__ == "__main__":
    main()

