from g4f.client import Client
from g4f.Provider import RetryProvider, Phind, DeepInfra, Liaobots, Aichatos, You, AItianhuSpace

def ask_chatGPT(question: str) -> str:
    client = Client(
        provider=RetryProvider([Phind, You, AItianhuSpace], shuffle=False)
    )
    response = client.chat.completions.create(
        model="",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content
    # core.play_voice_assistant_speech(response.choices[0].message.content)
    # core.play_voice_assistant_speech("Удалось решить проблему? да/нет")
    # core.context_set(check_answer_quality, 20)