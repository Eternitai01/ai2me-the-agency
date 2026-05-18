#!/usr/bin/env python3
"""
Generate all 9 AgentOS 24/7 post-purchase email templates
3 plans × 3 time terms = 9 templates
"""

import os
from pathlib import Path

SKILL_DIR = Path(__file__).parent
OUTPUT_DIR = SKILL_DIR / 'templates' / 'generated'

# Pricing data
# Instant Plans (Anthropic) - customer uses our AI credits
INSTANT_PLANS = {
    'Basic': {
        'conversations': '500',
        'channel': 'Telegram',
        'features': """
<li>500 conversations/month</li>
<li>Telegram agent</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates & improvements</li>
<li>24/7 technical support</li>
""",
        'pricing': {
            '1month': {'price': '90', 'discount': '50%'},
            '12months': {'price': '65', 'discount': '64%'},
            '24months': {'price': '49', 'discount': '73%'}
        }
    },
    'Plus': {
        'conversations': '800',
        'channel': 'WhatsApp',
        'features': """
<li>800 conversations/month</li>
<li>Dedicated WhatsApp number</li>
<li>Telegram agent</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>Priority email + chat support</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates & improvements</li>
""",
        'pricing': {
            '1month': {'price': '110', 'discount': '50%'},
            '12months': {'price': '79', 'discount': '64%'},
            '24months': {'price': '59', 'discount': '73%'}
        }
    },
    'Elite': {
        'conversations': '1500',
        'channel': 'Telegram + WhatsApp',
        'features': """
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
""",
        'pricing': {
            '1month': {'price': '276', 'discount': '50%'},
            '12months': {'price': '199', 'discount': '64%'},
            '24months': {'price': '149', 'discount': '73%'}
        }
    }
}

# BYOK Plans (Bring Your Own Key) - customer uses their own API keys
BYOK_PLANS = {
    'Starter': {
        'conversations': '300',
        'channel': 'Telegram',
        'features': """
<li>300 conversations/month</li>
<li>Telegram agent</li>
<li>Use your own API keys (OpenAI, Anthropic, etc.)</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates</li>
<li>Community support</li>
""",
        'pricing': {
            '1month': {'price': '54', 'discount': '50%'},
            '12months': {'price': '39', 'discount': '64%'},
            '24months': {'price': '29', 'discount': '73%'}
        }
    },
    'Pro': {
        'conversations': '600',
        'channel': 'WhatsApp',
        'features': """
<li>600 conversations/month</li>
<li>Dedicated WhatsApp number</li>
<li>Telegram agent</li>
<li>Use your own API keys (OpenAI, Anthropic, etc.)</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>Priority email support</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates</li>
""",
        'pricing': {
            '1month': {'price': '91', 'discount': '50%'},
            '12months': {'price': '65', 'discount': '64%'},
            '24months': {'price': '49', 'discount': '73%'}
        }
    },
    'Business': {
        'conversations': '1200',
        'channel': 'Telegram + WhatsApp',
        'features': """
<li>1200 conversations/month</li>
<li>Dedicated WhatsApp number</li>
<li>Telegram agent</li>
<li>Voice calls included</li>
<li>Use your own API keys (OpenAI, Anthropic, etc.)</li>
<li>80+ professional AI roles</li>
<li>Persistent memory & knowledge base</li>
<li>Priority 24/7 support</li>
<li>AI agent initiation guide</li>
<li>Constant OpenClaw updates</li>
""",
        'pricing': {
            '1month': {'price': '184', 'discount': '50%'},
            '12months': {'price': '132', 'discount': '64%'},
            '24months': {'price': '99', 'discount': '73%'}
        }
    }
}

TERM_LABELS = {
    '1month': '1 Month',
    '12months': '12 Months',
    '24months': '24 Months'
}

# Read base template
base_template = (SKILL_DIR / 'templates' / 'post-purchase.html').read_text()

# Create output directory
OUTPUT_DIR.mkdir(exist_ok=True)

print("Generating 18 post-purchase email templates...\n")
print("📦 INSTANT PLANS (Anthropic - we provide AI)\n")

for plan_name, plan_data in INSTANT_PLANS.items():
    for term, term_label in TERM_LABELS.items():
        price_info = plan_data['pricing'][term]
        price = price_info['price']
        discount = price_info['discount']
        
        # Create filename
        filename = f"post-purchase-{plan_name.lower()}-{term}.html"
        
        # Replace variables
        content = base_template
        content = content.replace('{{NAME}}', '{{NAME}}')  # Keep as variable
        content = content.replace('{{PLAN_NAME}}', plan_name)
        content = content.replace('{{PRICE}}', price)
        content = content.replace('{{BILLING_PERIOD}}', term_label)
        content = content.replace('{{CONVERSATIONS}}', plan_data['conversations'])
        content = content.replace('{{CHANNEL}}', plan_data['channel'])
        content = content.replace('{{ORDER_NUM}}', '{{ORDER_NUM}}')  # Keep as variable
        content = content.replace('{{PLAN_FEATURES}}', plan_data['features'])
        content = content.replace('{{EXTRA_MESSAGE}}', '')
        
        # Add discount badge if applicable
        if discount != '0%':
            content = content.replace(
                '<span class="badge" style="display: inline-block; background: #10b981; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">✅ PAYMENT CONFIRMED</span>\n                    </div>',
                f'<span class="badge" style="display: inline-block; background: #10b981; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">✅ PAYMENT CONFIRMED</span>\n                        <br style="line-height: 10px;">\n                        <span class="badge" style="display: inline-block; background: #f59e0b; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">💰 Save {discount}</span>\n                    </div>'
            )
        
        # Write file
        output_path = OUTPUT_DIR / filename
        output_path.write_text(content)
        
        print(f"✅ {filename}")
        print(f"   {plan_name} | €{price}/mo | {term_label} | Save {discount}")

print("\n🔑 BYOK PLANS (Bring Your Own Key - customer provides API keys)\n")

for plan_name, plan_data in BYOK_PLANS.items():
    for term, term_label in TERM_LABELS.items():
        price_info = plan_data['pricing'][term]
        price = price_info['price']
        discount = price_info['discount']
        
        # Create filename with byok prefix
        filename = f"post-purchase-byok-{plan_name.lower()}-{term}.html"
        
        # Replace variables
        content = base_template
        content = content.replace('{{NAME}}', '{{NAME}}')  # Keep as variable
        content = content.replace('{{PLAN_NAME}}', f"{plan_name} (BYOK)")
        content = content.replace('{{PRICE}}', price)
        content = content.replace('{{BILLING_PERIOD}}', term_label)
        content = content.replace('{{CONVERSATIONS}}', plan_data['conversations'])
        content = content.replace('{{CHANNEL}}', plan_data['channel'])
        content = content.replace('{{ORDER_NUM}}', '{{ORDER_NUM}}')  # Keep as variable
        content = content.replace('{{PLAN_FEATURES}}', plan_data['features'])
        content = content.replace('{{EXTRA_MESSAGE}}', '')
        
        # Add discount badge if applicable (BYOK)
        if discount != '0%':
            content = content.replace(
                '<span class="badge" style="display: inline-block; background: #10b981; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">✅ PAYMENT CONFIRMED</span>\n                    </div>',
                f'<span class="badge" style="display: inline-block; background: #10b981; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">✅ PAYMENT CONFIRMED</span>\n                        <br style="line-height: 10px;">\n                        <span class="badge" style="display: inline-block; background: #f59e0b; color: #ffffff; padding: 12px 32px; border-radius: 8px; font-size: 14px; font-weight: 600; margin: 5px;">💰 Save {discount}</span>\n                    </div>'
            )
        
        # Write file
        output_path = OUTPUT_DIR / filename
        output_path.write_text(content)
        
        print(f"✅ {filename}")
        print(f"   {plan_name} (BYOK) | €{price}/mo | {term_label} | Save {discount}")

print(f"\n✅ Generated 18 templates in {OUTPUT_DIR}/")
print("\nINSTANT Templates (9):")
print("  post-purchase-basic-1month.html")
print("  post-purchase-basic-12months.html")
print("  post-purchase-basic-24months.html")
print("  post-purchase-plus-1month.html")
print("  post-purchase-plus-12months.html")
print("  post-purchase-plus-24months.html")
print("  post-purchase-elite-1month.html")
print("  post-purchase-elite-12months.html")
print("  post-purchase-elite-24months.html")
print("\nBYOK Templates (9):")
print("  post-purchase-byok-starter-1month.html")
print("  post-purchase-byok-starter-12months.html")
print("  post-purchase-byok-starter-24months.html")
print("  post-purchase-byok-pro-1month.html")
print("  post-purchase-byok-pro-12months.html")
print("  post-purchase-byok-pro-24months.html")
print("  post-purchase-byok-business-1month.html")
print("  post-purchase-byok-business-12months.html")
print("  post-purchase-byok-business-24months.html")
