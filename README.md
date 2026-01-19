Markdown
# 🤖 Jarvis AI - Assistente Pessoal com Azure OpenAI

Este é um assistente virtual inspirado no Jarvis (Homem de Ferro), desenvolvido como parte do desafio de lógica e IA da **DIO (Digital Innovation One)**. O projeto utiliza a API do Azure OpenAI para processamento de linguagem natural e conversão de texto em fala (TTS).

## 🚀 Funcionalidades
- **Inteligência Artificial:** Respostas contextuais usando o modelo GPT-4o-mini da Azure.
- **Memória de Curto Prazo:** O Jarvis lembra do que foi dito anteriormente durante a conversa.
- **Saída de Voz:** Respostas faladas em tempo real usando a biblioteca `pyttsx3`.
- **Personalidade Única:** Configurado para responder de forma heróica e prestativa.

## 📂 Estrutura de Pastas
```text
projeto-logica-ia-azure/
├── src/
│   └── jarvis.py        # Código fonte principal
├── .env                 # Chaves de API (não versionado)
├── .gitignore           # Proteção para arquivos sensíveis
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
🛠️ Pré-requisitos
Python 3.10 ou superior.

Uma conta na Azure com o serviço Azure OpenAI habilitado.

🔧 Configuração
Clone o repositório.

Crie um arquivo .env na raiz do projeto com as seguintes chaves:

Snippet de código
AZURE_OPENAI_ENDPOINT="seu-endpoint-aqui"
AZURE_OPENAI_KEY="sua-chave-aqui"
AZURE_OPENAI_DEPLOYMENT="nome-da-sua-implantacao"
Instale as dependências:

Bash
pip install -r requirements.txt
▶️ Como usar
Basta executar o script principal:

Bash
python src/jarvis.py
✒️ Autor
Desenvolvido por Maurílio durante o curso de IA na Azure.