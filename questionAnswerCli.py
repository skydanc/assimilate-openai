#!/usr/bin/env python3

import os
import openai
import click

def submit_question(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = text
    result = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = result["choices"][0]["text"].strip()
    return answer

@click.command()
@click.argument("text")
def main(text):
    answer = submit_question(text)
    print(answer)

if __name__ == "__main__":
    main()
