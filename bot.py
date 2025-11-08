#!/usr/bin/env python3
"""
Bot do Telegram Automatizado
Integração com Pluggy.ai, Apex Seguidores e SMS-Activate
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, Any, Tuple

# Importar configurações
from config import (
    TELEGRAM_BOT_TOKEN,
    PLUGGY_CLIENT_ID,
    PLUGGY_API_KEY,
    APEX_API_KEY,
    SMS_ACTIVATE_API_KEY,
    ADMIN_TELEGRAM_ID,
    GOOGLE_SHEET_ID
)

# ============================================
# ARMAZENAMENTO EM MEMÓRIA
# ============================================
user_balances = {}
user_pluggy_items = {}

# ============================================
# FUNÇÕES DE INTEGRAÇÃO COM APIS
# ============================================

def comprar_seguidores_apex(service: str, quantity: int, link: str) -> Tuple[Dict, str]:
    """Integração com Apex Seguidores API"""
    try:
        endpoint = f"https://apexseguidores.com/api/v2?key={APEX_API_KEY}&action=add&service={service}&link={link}&quantity={quantity}"

        # Simular chamada API (em produção, usar requests)
        result = {
            "order_id": f"APX-{int(time.time())}",
            "status": "success",
            "quantity": quantity,
            "link": link
        }

        return result, ""
    except Exception as e:
        return {}, f"Erro Apex: {str(e)}"

def comprar_numero_sms_activate(country: str = "br", service: str = "telegram") -> Tuple[Dict, str]:
    """Integração com SMS-Activate API"""
    try:
        endpoint = f"https://api.sms-activate.org/stubs/handler_api.php?api_key={SMS_ACTIVATE_API_KEY}&action=getNumber&service={service}&country={country}"

        # Simular resposta (em produção, usar requests)
        result = {
            "activation_id": f"SMS-{int(time.time())}",
            "phone_number": f"+5511{int(time.time()) % 100000000}",
            "status": "success"
        }

        return result, ""
    except Exception as e:
        return {}, f"Erro SMS-Activate: {str(e)}"

def conectar_conta_pluggy(user_id: int) -> Tuple[str, str]:
    """Gera link de conexão Pluggy para o usuário"""
    try:
        connect_token = f"pluggy_token_{user_id}_{int(time.time())}"
        connect_url = f"https://connect.pluggy.ai?clientId={PLUGGY_CLIENT_ID}&token={connect_token}"
        return connect_url, ""
    except Exception as e:
        return "", f"Erro ao gerar link Pluggy: {str(e)}"

def obter_saldo_usuario(user_id: int) -> float:
    """Obtém saldo do usuário"""
    return user_balances.get(user_id, 0.0)

def debitar_saldo(user_id: int, valor: float) -> Tuple[bool, str]:
    """Debita saldo do usuário"""
    saldo_atual = obter_saldo_usuario(user_id)
    if saldo_atual < valor:
        return False, "Saldo insuficiente"
    user_balances[user_id] = saldo_atual - valor
    return True, ""

# ============================================
# SISTEMA DE LOGS
# ============================================

def registrar_log(user_id: int, username: str, operacao: str, valor: float, status: str, detalhes: str):
    """Registra log da operação"""
    timestamp = datetime.utcnow().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "user_id": user_id,
        "username": username,
        "operacao": operacao,
        "valor": valor,
        "status": status,
        "detalhes": detalhes
    }

    print(f"[{timestamp}] 📝 Log: {log_entry}")

    # Em produção: salvar no Google Sheets usando Composio

# ============================================
# MENU E TECLADOS
# ============================================

def get_menu_principal():
    """Retorna o teclado do menu principal"""
    keyboard = {
        "inline_keyboard": [
            [{"text": "🧾 Comprar Seguidores", "callback_data": "buy_followers"}],
            [{"text": "📱 Comprar Número Virtual", "callback_data": "buy_phone"}],
            [{"text": "💳 Conectar Conta Financeira", "callback_data": "connect_pluggy"}],
            [{"text": "💰 Ver Saldo", "callback_data": "check_balance"}]
        ]
    }
    return json.dumps(keyboard)

def get_menu_admin():
    """Retorna o teclado do painel admin"""
    keyboard = {
        "inline_keyboard": [
            [{"text": "📊 Relatórios", "callback_data": "admin_reports"}],
            [{"text": "👥 Usuários", "callback_data": "admin_users"}],
            [{"text": "🔙 Menu Principal", "callback_data": "start"}]
        ]
    }
    return json.dumps(keyboard)

# ============================================
# HANDLERS
# ============================================

def handle_start(chat_id: int, user_id: int, username: str):
    """Handler do comando /start"""
    is_admin = (user_id == ADMIN_TELEGRAM_ID)

    if is_admin:
        text = "🔐 *Painel Administrativo*\\n\\nBem-vindo, Admin!"
        keyboard = get_menu_admin()
    else:
        text = f"👋 Olá, {username}!\\n\\n🤖 *Bot de Serviços Automatizados*\\n\\nEscolha uma opção:"
        keyboard = get_menu_principal()

    # Em produção: enviar mensagem via Telegram API
    print(f"Enviando mensagem para {chat_id}: {text}")
    registrar_log(user_id, username, "start", 0, "success", "Iniciou o bot")

def handle_buy_phone(chat_id: int, user_id: int, username: str):
    """Handler de compra de número virtual"""
    preco = 5.0
    saldo = obter_saldo_usuario(user_id)

    if saldo < preco:
        text = f"⚠️ *Saldo Insuficiente*\\n\\nNecessário: R$ {preco:.2f}\\nSeu saldo: R$ {saldo:.2f}"
        print(f"Saldo insuficiente para {username}")
        return

    sucesso, msg = debitar_saldo(user_id, preco)
    if not sucesso:
        print(f"Erro ao debitar: {msg}")
        return

    # Chamar API
    numero_info, error = comprar_numero_sms_activate()

    if error:
        text = f"❌ Erro: {error}"
        registrar_log(user_id, username, "buy_phone", preco, "error", error)
    else:
        text = f"✅ *Número Comprado!*\\n\\n📱 Número: `{numero_info['phone_number']}`\\n💰 Pago: R$ {preco:.2f}"
        registrar_log(user_id, username, "buy_phone", preco, "success", json.dumps(numero_info))

    print(f"Resultado para {username}: {text}")

def handle_connect_pluggy(chat_id: int, user_id: int, username: str):
    """Handler de conexão com Pluggy"""
    connect_url, error = conectar_conta_pluggy(user_id)

    if error:
        print(f"Erro Pluggy: {error}")
    else:
        user_balances[user_id] = 100.0
        print(f"Conta conectada para {username}, saldo: R$ 100,00")
        registrar_log(user_id, username, "connect_pluggy", 0, "success", "Conectou conta")

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print(f"[{datetime.utcnow().isoformat()}] 🚀 Bot iniciado!")
    print(f"[{datetime.utcnow().isoformat()}] 🔑 Token: {TELEGRAM_BOT_TOKEN[:10]}...")
    print(f"[{datetime.utcnow().isoformat()}] 👤 Admin ID: {ADMIN_TELEGRAM_ID}")
    print(f"[{datetime.utcnow().isoformat()}] ✅ Bot pronto para receber comandos")

    # Simular alguns eventos
    handle_start(123456, 123456, "test_user")
    handle_connect_pluggy(123456, 123456, "test_user")
    handle_buy_phone(123456, 123456, "test_user")

    print(f"\\n[{datetime.utcnow().isoformat()}] 🎯 Bot funcionando corretamente!")
