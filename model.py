import os
from openai import AzureOpenAI

KEY = "bc9916593fc54489b44ac2bff2d19277"

client = AzureOpenAI(
    api_version="2023-08-01-preview",
    azure_endpoint="!ping -c 5 ai-proxy.lab.epam.com",
    api_key=KEY,
)

def generate_blog(title, keywords):
    # Join the keywords into a single string
    keywords_str = ', '.join(keywords)
    
    # Create a prompt for the AI
    prompt = f"Write a blog post with the title '{title}' that includes the following keywords: {keywords_str}."
    
    # Choose a model to use for generation
    model = 'gpt-4'  # You can choose any other model you prefer
    
    # Generate the blog content
    response = client.chat.completions.create(
        model=model,
        temperature=0.7,  # Adjust temperature for creativity
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    
    # Extract the generated content
    blog_content = response.choices[0].message.content.strip()
    
    return blog_content