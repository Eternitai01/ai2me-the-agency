#!/usr/bin/env python3
"""
Send specific AgentOS 24/7 emails using pre-generated templates
10 emails total: 1 post-chat + 9 post-purchase (3 plans × 3 terms)

Usage:
    # Post-chat
    python3 send-specific.py post-chat --to email@example.com --name "John"
    
    # Post-purchase (specify plan and term)
    python3 send-specific.py post-purchase --to email@example.com --name "John" --plan basic --term monthly --order AGT-001
    python3 send-specific.py post-purchase --to email@example.com --name "John" --plan plus --term 12months --order AGT-002
    python3 send-specific.py post-purchase --to email@example.com --name "John" --plan elite --term 24months --order AGT-003
"""

import argparse
import sys
from pathlib import Path
import importlib.util

SKILL_DIR = Path(__file__).parent
TEMPLATES_DIR = SKILL_DIR / 'templates'
GENERATED_DIR = TEMPLATES_DIR / 'generated'
ASSETS_DIR = SKILL_DIR / 'assets'
LOGO_PATH = ASSETS_DIR / 'logo.png'

# Import send_email from email-sender skill
email_sender_path = SKILL_DIR.parent / 'email-sender'
spec = importlib.util.spec_from_file_location("send_email", email_sender_path / 'send-email.py')
if spec is None or spec.loader is None:
    print("❌ Error: email-sender skill not found", file=sys.stderr)
    sys.exit(1)

send_email_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(send_email_module)
send_email = send_email_module.send_email

def send_post_chat(to, name):
    """Send post-chat follow-up email"""
    template = TEMPLATES_DIR / 'post-chat.html'
    
    if not template.exists():
        print(f"❌ Template not found: {template}", file=sys.stderr)
        return False
    
    print(f"📧 Sending post-chat email to {to}...")
    
    success = send_email(
        to=to,
        subject="Thanks for Chatting with Charlie | AgentOS 24/7",
        html_template=str(template),
        template_vars={'NAME': name},
        inline_images={'logo': str(LOGO_PATH)},
        from_addr='Amaya Sinclair <amaya.sinclair@eternitai.com>'
    )
    
    if success:
        print(f"✅ Post-chat email sent to {to}")
    
    return success

def send_post_purchase(to, name, plan, term, order, byok=False):
    """Send post-purchase email using specific plan+term template"""
    
    # Validate inputs
    if byok:
        valid_plans = ['starter', 'pro', 'business']
    else:
        valid_plans = ['basic', 'plus', 'elite']
    valid_terms = ['1month', '12months', '24months']
    
    plan = plan.lower()
    term = term.lower()
    
    if plan not in valid_plans:
        print(f"❌ Invalid plan: {plan}. Must be: basic, plus, or elite", file=sys.stderr)
        return False
    
    if term not in valid_terms:
        print(f"❌ Invalid term: {term}. Must be: 1month, 12months, or 24months", file=sys.stderr)
        return False
    
    # Find template
    if byok:
        template_name = f"post-purchase-byok-{plan}-{term}.html"
    else:
        template_name = f"post-purchase-{plan}-{term}.html"
    template = GENERATED_DIR / template_name
    
    if not template.exists():
        print(f"❌ Template not found: {template}", file=sys.stderr)
        print(f"   Run: python3 generate-all.py to create templates", file=sys.stderr)
        return False
    
    # Read template and replace remaining variables
    content = template.read_text()
    content = content.replace('{{NAME}}', name)
    content = content.replace('{{ORDER_NUM}}', order)
    
    # Write to temp file
    temp_template = TEMPLATES_DIR / f'.temp-{plan}-{term}.html'
    temp_template.write_text(content)
    
    # Plan display names
    if byok:
        plan_names = {
            'starter': 'Starter (BYOK)',
            'pro': 'Pro (BYOK)',
            'business': 'Business (BYOK)'
        }
    else:
        plan_names = {
            'basic': 'Basic',
            'plus': 'Plus',
            'elite': 'Elite'
        }
    
    term_labels = {
        '1month': '1 Month',
        '12months': '12 Months',
        '24months': '24 Months'
    }
    
    print(f"📧 Sending post-purchase email to {to}...")
    print(f"   {plan_names[plan]} Plan | {term_labels[term]}")
    
    try:
        success = send_email(
            to=to,
            subject="Welcome to AgentOS 24/7 - Your Agent is Being Deployed",
            html_template=str(temp_template),
            template_vars={},  # Already replaced in content
            inline_images={'logo': str(LOGO_PATH)},
            from_addr='Amaya Sinclair <amaya.sinclair@eternitai.com>'
        )
        
        if success:
            print(f"✅ Post-purchase email sent to {to}")
    finally:
        # Clean up temp file
        if temp_template.exists():
            temp_template.unlink()
    
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
    post_purchase.add_argument('--plan', required=True, help='Plan name (lowercase): basic/plus/elite OR starter/pro/business for BYOK')
    post_purchase.add_argument('--term', required=True, choices=['1month', '12months', '24months'], help='Time term')
    post_purchase.add_argument('--order', required=True, help='Order number')
    post_purchase.add_argument('--byok', action='store_true', help='BYOK plan (Bring Your Own Key)')
    
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
        byok = getattr(args, 'byok', False)
        success = send_post_purchase(args.to, args.name, args.plan, args.term, args.order, byok=byok)
    else:
        print(f"❌ Unknown email type: {args.email_type}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
