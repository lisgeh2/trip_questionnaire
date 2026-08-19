import anthropic

client = anthropic.Anthropic()#KEY aus der Umgebung

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    system="Du bist ein hilfreicher Assistent. Antworte auf Deutsch und fasse dich kurz.",
    messages=[
        {"role": "user", "content": "Erkläre Rekursion in einem Satz."},
    ],
)

def give_interaction_safety_rating(med):
   
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="Answer with a single number only",
        messages=[
            {"role": "user", "content": f"Rate the pharmacological safety of combining psilocybin and {med}, from 1 to 10. Answer only with this number."},
        ],
    )
    
    return int(message.content[0].text)

def give_interaction_safety_text(med):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="Give a short and concise answer. No Titles, just plain text, 1-3 sentences",
        messages=[
            {"role": "user", "content": f"Rate the pharmacological safety of combining psilocybin and {med}, answer with a **short** text of 2-3 sentences. No titles, just plain text. Use language for normal people."},
        ],
    )
    
    return message.content[0].text    




if __name__ == "__main__":
    print(give_interaction_safety_text("lithium"))
    print(give_interaction_safety_rating("lithium"))