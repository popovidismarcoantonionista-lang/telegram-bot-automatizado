# 🤖 Bot Telegram Automatizado

Bot do Telegram totalmente automatizado com integrações completas para serviços de pagamento, compra de seguidores e números virtuais.

## 🎯 Funcionalidades

- ✅ **Menu Interativo** com botões inline
- ✅ **Integração Pluggy.ai** - Pagamentos automáticos via Open Banking
- ✅ **Integração Apex Seguidores** - Compra automática de seguidores/curtidas
- ✅ **Integração SMS-Activate** - Compra de números virtuais
- ✅ **Sistema de Saldo** - Controle automático de créditos
- ✅ **Painel Administrativo** - Acesso exclusivo para admin
- ✅ **Sistema de Logs** - Registro no Google Sheets
- ✅ **Funcionamento 24/7** - Pronto para produção

## 📋 Pré-requisitos

- Python 3.8+
- Conta no Telegram ([@BotFather](https://t.me/BotFather))
- API Keys:
  - Pluggy.ai ([Dashboard](https://dashboard.pluggy.ai/))
  - Apex Seguidores
  - SMS-Activate ([Profile](https://sms-activate.org/en/profile))
- Google Cloud (para Sheets)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/{repo_full_name}.git
cd telegram-bot-automatizado
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

### 4. Execute o bot
```bash
python bot.py
```

## 🐳 Docker (Recomendado para 24/7)

```bash
# Build
docker build -t telegram-bot .

# Run
docker run -d --name telegram-bot --env-file .env telegram-bot
```

## ⚙️ Configuração

Edite o arquivo `.env` com suas credenciais:

```env
# Telegram
TELEGRAM_BOT_TOKEN=seu_token_aqui

# Pluggy.ai
PLUGGY_CLIENT_ID=seu_client_id
PLUGGY_API_KEY=sua_api_key

# Apex Seguidores
APEX_API_KEY=sua_api_key

# SMS-Activate
SMS_ACTIVATE_API_KEY=sua_api_key

# Admin
ADMIN_TELEGRAM_ID=seu_user_id

# Google Sheets (opcional)
GOOGLE_SHEET_ID=id_da_planilha
```

## 📱 Uso

1. **Inicie o bot no Telegram:** Busque por `@seu_bot` e envie `/start`

2. **Menu Principal:**
   - 🧾 Comprar Seguidores
   - 📱 Comprar Número Virtual (R$ 5,00)
   - 💳 Conectar Conta Financeira (recebe R$ 100 inicial)
   - 💰 Ver Saldo

3. **Painel Admin** (apenas para o admin configurado):
   - 📊 Relatórios gerais
   - 👥 Lista de usuários
   - 💵 Gerenciamento de saldos

## 🔧 APIs Utilizadas

### Pluggy.ai
- **Função:** Conexão com contas bancárias e Open Banking
- **Endpoint:** `https://api.pluggy.ai`
- **Docs:** [Pluggy API](https://docs.pluggy.ai)

### Apex Seguidores
- **Função:** Compra de seguidores, curtidas e visualizações
- **Endpoint:** `https://apexseguidores.com/api/v2`
- **Formato:** `?key=API_KEY&action=add&service=SERVICE_ID&link=URL&quantity=QTY`

### SMS-Activate
- **Função:** Compra de números virtuais para verificação
- **Endpoint:** `https://api.sms-activate.org/stubs/handler_api.php`
- **Docs:** [SMS-Activate API](https://sms-activate.org/en/api2)

## 📊 Sistema de Logs

Todos os eventos são registrados automaticamente no Google Sheets:

| Timestamp | User ID | Username | Operação | Valor | Status | Detalhes |
|-----------|---------|----------|----------|-------|--------|----------|
| 2025-11-08... | 123456 | user1 | buy_phone | 5.00 | success | +5511999... |

## 🔐 Segurança

- ✅ Variáveis de ambiente para credenciais
- ✅ Validação de saldo antes de compras
- ✅ Acesso restrito ao painel admin por ID
- ✅ Logs de todas as operações
- ✅ Sem hardcoding de dados sensíveis

## 🛠️ Estrutura do Projeto

```
telegram-bot-automatizado/
├── bot.py                 # Código principal
├── config.py              # Configurações
├── requirements.txt       # Dependências
├── Dockerfile            # Container Docker
├── .env.example          # Exemplo de variáveis
├── .gitignore           # Arquivos ignorados
├── README.md            # Documentação
└── utils/
    ├── __init__.py
    ├── apis.py          # Integrações de APIs
    └── database.py      # Gerenciamento de dados
```

## 📝 Comandos do Bot

- `/start` - Inicia o bot e mostra o menu
- `/saldo` - Verifica o saldo atual
- `/help` - Mostra ajuda (em desenvolvimento)
- `/admin` - Painel admin (apenas admin)

## 🐛 Troubleshooting

### Bot não responde
- Verifique se o token está correto
- Confirme que o bot foi autorizado no Composio

### Erro ao comprar serviços
- Verifique se as API Keys estão corretas
- Confirme que há saldo suficiente

### Logs não aparecem
- Verifique as permissões do Google Sheets
- Confirme que o GOOGLE_SHEET_ID está correto

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Criado com ❤️ usando [Rube by Composio](https://rube.app)

## 🔗 Links Úteis

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Pluggy.ai Docs](https://docs.pluggy.ai)
- [SMS-Activate API](https://sms-activate.org/en/api2)
- [Composio Platform](https://composio.dev)

## ⭐ Suporte

Se este projeto foi útil, deixe uma ⭐!

Para dúvidas ou suporte, abra uma [Issue](https://github.com/{repo_full_name}/issues).

---

**Nota:** Este bot foi desenvolvido para fins educacionais. Use com responsabilidade e de acordo com os Termos de Serviço de cada plataforma.
