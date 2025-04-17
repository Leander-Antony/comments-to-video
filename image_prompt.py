import pandas as pd
import ollama
import re

df = pd.read_csv("sidemen_top_comments.csv")
comments = df['comment'].tolist()

def generate_prompt_for_comment(comment, position):
    system_prompt = (
    "You're a creative text to image prompt maker in a single line"
    "Given a funny YouTube comment from a Sidemen video, turn it into a short, dramatic, and hilarious image prompt. "
    "ignore any names"
    "Make the scene feel epic and cinematic, exaggerating the moment. "
    "Keep it short, funny, and visual — perfect for animation. "
    "\n\nFormat exactly like:\nPrompt: <your prompt here>\n\n"
    "Do not include any extra text."
)



    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": comment}
        ]
    )

    raw_output = response['message']['content']
    print(f"Raw output: {raw_output}")
    
    return raw_output.strip()

def generate_all_prompts(comments, output_csv="prompts_with_order.csv"):
    data = []
    
    for idx, comment in enumerate(comments):
        print(f"🎬 Generating prompt for comment {idx+1}/{len(comments)}...")
        result = generate_prompt_for_comment(comment, idx + 1)
        if result:
            data.append(result)
    
    df_out = pd.DataFrame(data)
    df_out.to_csv(output_csv, index=False)
    print(f"Saved {len(df_out)} prompts to {output_csv}")
    return df_out

generate_all_prompts(comments, output_csv="prompts_for_image.csv")
