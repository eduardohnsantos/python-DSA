# Projeto 3 - Construindo Chatbot Personalizado com GPT4 e Linguagem Python

# Import
import openai

# Chave
openai.api.key = 'sk-proj-RvtZNRcdE320Af3W8isjT3BlbkFJbvuXmHZMS22QoKro0tPI'

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    # Obtém a resposta do modelo de linguagem
    response = openai.Completion.create(
        # Modelo usado
        # Outros modelos estão disponíveis em https://platform.openai.com/account/rate-limits
        engine = "text-davinci-003",
        
        # Texto inicial da conversa com o chatbot.
        prompt = texto,
        
        # Comprimento da resposta gerada pelo modelo.
        max_tokens = 150,
        
        # Quantas conclusões gerar para cada prompt.
        n = 5,
        
        # O texto retornado não conterá a sequência de parada.
        stop = None,
        
        # Uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
        # Valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a 0 significam que a saída é muito identificável.
        temperature = 0.8,
    )

    return response.choices[0].text.strip()
    
# Função principal do programa em Python
def main():

    print("\nBem-vindo ao GPT-4 Chatbot do Projeto 3 do Curso Gratuito da Data Science Academy!")
    print("www.datascienceacademy.com.br")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    # Loop
    while True:

        # Coleta a pergunta digitada pelo usuário.
        user_message = input("\nVocê: ")

        # Se a mensagem for "sair" finaliza o programa.
        if user_message.lower() == "sair":
            break

        # Coloca a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt.
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        # Obtém a resposta do modelo executando a função gera_texto().
        chatbot_response = gera_texto(gpt4_prompt)

        # Imprime a resposta do chatbot.
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python
if __name__ == "__main__":
    main()
    
