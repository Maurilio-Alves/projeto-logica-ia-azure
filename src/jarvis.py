import os
import pyttsx3
from openai import AzureOpenAI
from dotenv import load_dotenv

# --- CONFIGURAÇÃO DE CAMINHO (O PULO DO GATO) ---
# Pega o local onde o jarvis.py está (ex: /src)
base_path = os.path.dirname(__file__)
# Aponta para o .env que está uma pasta acima
dotenv_path = os.path.join(base_path, '..', '.env')

# Carrega o .env do caminho específico
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv() # Caso você rode na mesma pasta

# --- CONFIGURAÇÕES DA AZURE ---
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
chave = os.getenv("AZURE_OPENAI_KEY")
modelo = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# --- FUNÇÃO DE VOZ (REINICIALIZADA) ---
def falar(texto):
    print(f"\n🤖 JARVIS: {texto}")
    # Reinicia o motor para garantir que não trave entre frases
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

# --- VERIFICAÇÃO DE CREDENCIAIS ---
if not endpoint or not chave:
    print("❌ ERRO: O arquivo .env não foi encontrado em: " + dotenv_path)
    exit()

# --- CLIENTE AZURE ---
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=chave,
    api_version="2024-02-01"
)

# --- MEMÓRIA E HISTÓRICO ---
historico = [
    {"role": "system", "content": "Você é o Jarvis. Responda de forma heróica, curta e lembre-se do histórico da conversa."}
]

# Saudação inicial
falar("Sistemas de arquivos organizados. Estou pronto para a ação, Maurílio.")

while True:
    print("\n" + "="*45)
    pergunta = input("Sua pergunta (ou 'sair'): ")

    if not pergunta:
        continue

    if pergunta.lower() in ["sair", "parar", "tchau", "exit"]:
        falar("Entendido, senhor. Até a próxima missão!")
        break

    # Adiciona pergunta ao histórico
    historico.append({"role": "user", "content": pergunta})

    try:
        # Chamada para a IA
        response = client.chat.completions.create(
            model=modelo,
            messages=historico
        )

        resposta_texto = response.choices[0].message.content
        
        # Salva a resposta do assistente na memória
        historico.append({"role": "assistant", "content": resposta_texto})
        
        # Fala a resposta
        falar(resposta_texto)

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
        falar("Sinto muito, Maurílio. Tive um problema de comunicação com a base de dados.")