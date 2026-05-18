#!/usr/bin/env python3
"""
AgentOS 24/7 Email Sender
Send customer emails using predefined templates.

Usage:
    python3 send.py post-chat --to email@example.com --name "John"
    python3 send.py post-purchase --to email@example.com --name "John" --plan "Basic" --price "90" --billing "Annual" --conversations "500" --channel "Telegram" --order "AGT-001"
    python3 send.py welcome --to email@example.com --name "John" --plan "Professional Plan" --customer-num "AGT-001"
"""

import argparse
import os
import sys
from pathlib import Path

# Add parent email-sender skill to path
email_sender_path = Path(__file__).parent.parent / 'email-sender'
sys.path.insert(0, str(email_sender_path))

# Import send_email module
import importlib.util
spec = importlib.util.spec_from_file_location("send_email", email_sender_path / 'send-email.py')
if spec is None or spec.loader is None:
    print("❌ Error: email-sender skill not found", file=sys.stderr)
    print(f"   Expected: {email_sender_path / 'send-email.py'}", file=sys.stderr)
    sys.exit(1)

send_email_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(send_email_module)
send_email = send_email_module.send_email

SKILL_DIR = Path(__file__).parent
TEMPLATES_DIR = SKILL_DIR / 'templates'
ASSETS_DIR = SKILL_DIR / 'assets'
LOGO_PATH = ASSETS_DIR / 'logo.png'

# Plan features
PLAN_FEATURES = {
    'Basic': """
<li>500 conversations/month</li>
<li>Telegram agent</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates & improvements</li>
<li>24/7 technical support</li>
""",
    'Plus': """
<li>800 conversations/month</li>
<li>Dedicated WhatsApp number</li>
<li>Telegram agent</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>Priority email + chat support</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates & improvements</li>
""",
    'Elite': """
<li>1500 conversations/month</li>
<li>Dedicated WhatsApp number</li>
<li>Telegram agent</li>
<li>Voice calls included</li>
<li>Dante Guardian personal monitoring</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>Priority 24/7 support</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates & improvements</li>
"""
}

def send_post_chat(to, name):
    """Send post-chat follow-up email"""
    template = TEMPLATES_DIR / 'post-chat.html'
    
    if not template.exists():
        print(f"❌ Template not found: {template}", file=sys.stderr)
        return False
    
    print(f"📧 Sending post-chat email to {to}...")
    
    success = send_email(
        to=to,
        subject=f"Thanks for Chatting with Charlie | AgentOS 24/7",
        html_template=str(template),
        template_vars={'NAME': name},
        inline_images={'logo': str(LOGO_PATH)},
        from_addr='Amaya Sinclair <amaya.sinclair@eternitai.com>'
    )
    
    if success:
        print(f"✅ Post-chat email sent to {to}")
    
    return success

def send_post_purchase(to, name, plan, price, billing, conversations, channel, order):
    """Send post-purchase receipt email"""
    template = TEMPLATES_DIR / 'post-purchase.html'
    
    if not template.exists():
        print(f"❌ Template not found: {template}", file=sys.stderr)
        return False
    
    # Get plan features
    plan_features = PLAN_FEATURES.get(plan, PLAN_FEATURES['Basic'])
    
    print(f"📧 Sending post-purchase email to {to}...")
    print(f"   Plan: {plan} | €{price}/{billing} | {conversations} conversations | {channel}")
    
    success = send_email(
        to=to,
        subject=f"Welcome to AgentOS 24/7 - Your Agent is Being Deployed",
        html_template=str(template),
        template_vars={
            'NAME': name,
            'PLAN_NAME': plan,
            'PRICE': price,
            'BILLING_PERIOD': billing,
            'CONVERSATIONS': conversations,
            'CHANNEL': channel,
            'ORDER_NUM': order,
            'PLAN_FEATURES': plan_features,
            'EXTRA_MESSAGE': ''
        },
        inline_images={'logo': str(LOGO_PATH)},
        from_addr='Amaya Sinclair <amaya.sinclair@eternitai.com>'
    )
    
    if success:
        print(f"✅ Post-purchase email sent to {to}")
    
    return success

def send_welcome(to, name, plan, customer_num):
    """Send welcome/go-live email"""
    template = TEMPLATES_DIR / 'welcome.html'
    
    if not template.exists():
        print(f"❌ Template not found: {template}", file=sys.stderr)
        return False
    
    print(f"📧 Sending welcome email to {to}...")
    print(f"   {plan} | Customer #{customer_num}")
    
    success = send_email(
        to=to,
        subject=f"✅ AgentOS 24/7 - Your Agents Are Ready",
        html_template=str(template),
        template_vars={
            'CUSTOMER_NAME': name,
            'PLAN_NAME': plan,
            'CUSTOMER_NUM': customer_num
        },
        inline_images={'logo': str(LOGO_PATH)},
        from_addr='Amaya Sinclair <amaya.sinclair@eternitai.com>'
    )
    
    if success:
        print(f"✅ Welcome email sent to {to}")
    
    return success

def main():
    parser = argparse.ArgumentParser(description='Send AgentOS 24/7 customer emails')
    subparsers = parser.add_subparsers(dest='email_type', help='Email type')
    
    # Post-chat
    post_chat = subparsers.add_parser('post-chat', help='Send post-chat follow-up')
    post_chat.add_argument('--to', required=True, help='Recipient email')
    post_chat.add_argument('--name', required=True, help='Customer first name')
    
    # Post-purchase
    post_purchase = subparsers.add_parser('post-purchase', help='Send post-purchase receipt')
    post_purchase.add_argument('--to', required=True, help='Recipient email')
    post_purchase.add_argument('--name', required=True, help='Customer first name')
    post_purchase.add_argument('--plan', required=True, choices=['Basic', 'Plus', 'Elite'], help='Plan name')
    post_purchase.add_argument('--price', required=True, help='Price (e.g., 90, 109, 276)')
    post_purchase.add_argument('--billing', required=True, help='Billing period (e.g., Annual, Monthly)')
    post_purchase.add_argument('--conversations', required=True, help='Conversation limit (e.g., 500, 800, 1500)')
    post_purchase.add_argument('--channel', required=True, help='Channel (e.g., Telegram, WhatsApp)')
    post_purchase.add_argument('--order', required=True, help='Order number')
    
    # Welcome
    welcome = subparsers.add_parser('welcome', help='Send welcome/go-live email')
    welcome.add_argument('--to', required=True, help='Recipient email')
    welcome.add_argument('--name', required=True, help='Customer first name')
    welcome.add_argument('--plan', required=True, help='Plan display name')
    welcome.add_argument('--customer-num', required=True, help='Customer number')
    
    args = parser.parse_args()
    
    if not args.email_type:
        parser.print_help()
        sys.exit(1)
    
    # Check logo exists
    if not LOGO_PATH.exists():
        print(f"❌ Logo not found: {LOGO_PATH}", file=sys.stderr)
        print(f"   Download it first:", file=sys.stderr)
        print(f"   curl -o {LOGO_PATH} https://agentos247.com/assets/agentos247-logo-DgB4oMWh.png", file=sys.stderr)
        sys.exit(1)
    
    # Send email
    if args.email_type == 'post-chat':
        success = send_post_chat(args.to, args.name)
    elif args.email_type == 'post-purchase':
        success = send_post_purchase(
            args.to, args.name, args.plan, args.price,
            args.billing, args.conversations, args.channel, args.order
        )
    elif args.email_type == 'welcome':
        success = send_welcome(args.to, args.name, args.plan, args.customer_num)
    else:
        print(f"❌ Unknown email type: {args.email_type}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
