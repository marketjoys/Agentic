"""
Seed data initialization for the email responder application
"""
from datetime import datetime
from app.utils.helpers import generate_id

async def initialize_seed_data(db_service):
    """Initialize the database with sample data for testing"""
    try:
        # Check if data already exists
        existing_templates = await db_service.get_templates()
        existing_lists = await db_service.get_lists()
        
        if existing_templates and existing_lists:
            print("Seed data already exists, skipping initialization")
            return
        
        print("🌱 Initializing seed data...")
        
        # Sample templates including auto-response templates
        templates = [
            {
                "id": generate_id(),
                "name": "Welcome Email",
                "subject": "Welcome to {{company}} - Let's Connect!",
                "content": """Hi {{first_name}},

I hope this email finds you well! I came across {{company}} and was impressed by your work in the {{industry}} industry.

I'd love to connect and explore potential collaboration opportunities that could benefit both our organizations.

Would you be open to a brief 15-minute call next week to discuss this further?

Best regards,
[Your Name]""",
                "type": "initial",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Follow-up Email",
                "subject": "Following up on our conversation - {{company}}",
                "content": """Hi {{first_name}},

I wanted to follow up on my previous email regarding potential collaboration opportunities between our companies.

I understand you're likely busy, but I believe there could be significant value in a brief conversation about how we can work together.

Would you have 10-15 minutes available this week for a quick call?

Looking forward to hearing from you.

Best regards,
[Your Name]""",
                "type": "follow_up",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Auto Response - Interest",
                "subject": "Re: Thank you for your interest!",
                "content": """Hi {{first_name}},

Thank you for expressing interest in our collaboration proposal!

I'm excited to learn more about {{company}} and explore how we can work together to achieve mutual success in the {{industry}} industry.

I'll reach out within the next 24 hours to schedule a convenient time for our conversation.

Best regards,
[Your Name]""",
                "type": "auto_response",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Auto Response - Questions",
                "subject": "Re: Happy to answer your questions!",
                "content": """Hi {{first_name}},

Great question! I'd be happy to provide more details about our collaboration opportunities.

Based on what I know about {{company}} and your work in {{industry}}, I believe there could be some excellent synergies between our organizations.

Let me send you some additional information, and I'd love to schedule a brief 15-minute call to discuss your specific questions in detail.

When would be a good time for you this week?

Best regards,
[Your Name]""",
                "type": "auto_response",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Auto Response - Pricing",
                "subject": "Re: Pricing Information for {{company}}",
                "content": """Hi {{first_name}},

Thanks for your interest in our pricing! 

I'd love to provide you with detailed pricing information that's tailored specifically for {{company}} and your needs in the {{industry}} sector.

Our pricing varies based on the scope and scale of collaboration, so I'd like to schedule a brief call to understand your specific requirements and provide you with the most accurate information.

Would you have 10-15 minutes available this week for a quick discussion?

Best regards,
[Your Name]""",
                "type": "auto_response", 
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Sample prospects
        prospects = [
            {
                "id": generate_id(),
                "email": "john.doe@techcorp.com",
                "first_name": "John",
                "last_name": "Doe",
                "company": "TechCorp Inc",
                "job_title": "CEO",
                "industry": "Technology",
                "phone": "+1-555-0101",
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "email": "sarah.smith@innovatesoft.com",
                "first_name": "Sarah",
                "last_name": "Smith",
                "company": "InnovateSoft",
                "job_title": "CTO",
                "industry": "Software Development",
                "phone": "+1-555-0102",
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "email": "mike.johnson@datascienceai.com",
                "first_name": "Mike",
                "last_name": "Johnson",
                "company": "DataScience AI",
                "job_title": "VP of Engineering",
                "industry": "Artificial Intelligence",
                "phone": "+1-555-0103",
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Sample email providers
        email_providers = [
            {
                "id": generate_id(),
                "name": "Test Gmail Provider",
                "provider_type": "gmail",
                "email_address": "test@gmail.com",
                "display_name": "Test User",
                "smtp_host": "smtp.gmail.com",
                "smtp_port": 587,
                "smtp_username": "test@gmail.com",
                "smtp_password": "app_password",
                "smtp_use_tls": True,
                "imap_host": "imap.gmail.com",
                "imap_port": 993,
                "imap_username": "test@gmail.com",
                "imap_password": "app_password",
                "daily_send_limit": 500,
                "hourly_send_limit": 50,
                "is_default": True,
                "is_active": True,
                "skip_connection_test": True,
                "current_daily_count": 0,
                "current_hourly_count": 0,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
                "last_sync": datetime.utcnow()
            }
        ]
        
        # Sample intents with auto-response capability
        intents = [
            {
                "id": generate_id(),
                "name": "Interested - Auto Respond",
                "description": "Prospect is interested and wants to learn more",
                "keywords": ["interested", "yes", "tell me more", "sounds good", "let's talk", "want to know more", "please share", "can you send"],
                "response_template": "Thank you for your interest! I'll reach out to schedule a call.",
                "confidence_threshold": 0.7,
                "auto_respond": True,
                "primary_template_id": None,  # Will be set after templates are created
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Question - Auto Respond", 
                "description": "Prospect has questions about our services or offerings",
                "keywords": ["question", "how does", "what is", "can you explain", "tell me about", "more information", "details", "pricing"],
                "response_template": "Great question! I'd be happy to provide more details. Let me send you some information and we can schedule a brief call to discuss further.",
                "confidence_threshold": 0.6,
                "auto_respond": True,
                "primary_template_id": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Pricing Request - Auto Respond",
                "description": "Prospect is asking about pricing or costs",
                "keywords": ["price", "pricing", "cost", "how much", "budget", "quote", "estimate", "fees"],
                "response_template": "Thanks for your interest in our pricing! I'll send you our pricing information and would love to discuss how we can customize a solution for your specific needs.",
                "confidence_threshold": 0.8,
                "auto_respond": True,
                "primary_template_id": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Not Interested",
                "description": "Prospect is not interested at this time",
                "keywords": ["not interested", "no thanks", "remove me", "unsubscribe", "stop", "don't contact"],
                "response_template": "Thank you for your time. I'll remove you from our outreach list.",
                "confidence_threshold": 0.8,
                "auto_respond": False,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": generate_id(),
                "name": "Out of Office",
                "description": "Automatic out of office or vacation reply",
                "keywords": ["out of office", "vacation", "away", "automatic reply", "auto-reply", "currently unavailable"],
                "response_template": "",  # No response needed for auto-replies
                "confidence_threshold": 0.9,
                "auto_respond": False,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Only create templates if they don't exist
        if not existing_templates:
            # Create templates
            for template in templates:
                await db_service.create_template(template)
            print(f"✅ Created {len(templates)} sample templates")
        else:
            print("✅ Templates already exist, skipping template creation")
            
        # Only create prospects if they don't exist
        existing_prospects = await db_service.get_prospects()
        if not existing_prospects:
            # Create prospects
            for prospect in prospects:
                await db_service.create_prospect(prospect)
            print(f"✅ Created {len(prospects)} sample prospects")
        else:
            print("✅ Prospects already exist, skipping prospect creation")
            prospects = existing_prospects
            
        # Only create email providers if they don't exist
        existing_providers = await db_service.get_email_providers()
        if not existing_providers:
            # Create email providers
            for provider in email_providers:
                await db_service.create_email_provider(provider)
            print(f"✅ Created {len(email_providers)} sample email providers")
        else:
            print("✅ Email providers already exist, skipping provider creation")
            
        # Only create intents if they don't exist
        existing_intents = await db_service.get_intents()
        if not existing_intents:
            # Create intents
            for intent in intents:
                await db_service.create_intent(intent)
            print(f"✅ Created {len(intents)} sample intents")
        else:
            print("✅ Intents already exist, skipping intent creation")
        
        # Link auto-response templates to intents
        current_templates = await db_service.get_templates()
        current_intents = await db_service.get_intents()
        
        # Find templates by name and link them to appropriate intents
        template_mapping = {
            "Auto Response - Interest": "Interested - Auto Respond",
            "Auto Response - Questions": "Question - Auto Respond", 
            "Auto Response - Pricing": "Pricing Request - Auto Respond"
        }
        
        for template_name, intent_name in template_mapping.items():
            template = next((t for t in current_templates if t["name"] == template_name), None)
            intent = next((i for i in current_intents if i["name"] == intent_name), None)
            
            if template and intent and not intent.get("primary_template_id"):
                await db_service.update_intent(intent["id"], {
                    "primary_template_id": template["id"]
                })
                print(f"✅ Linked template '{template_name}' to intent '{intent_name}'")
        
        # Always create lists if they don't exist (this is the main fix)
        if not existing_lists:
            # Sample prospect lists
            prospect_lists = [
                {
                    "id": generate_id(),
                    "name": "Technology Companies",
                    "description": "CEOs and CTOs from tech startups and established companies",
                    "color": "#3B82F6",
                    "prospect_count": 0,
                    "tags": ["tech", "startup", "enterprise"],
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow()
                },
                {
                    "id": generate_id(),
                    "name": "AI & Machine Learning",
                    "description": "Companies working with AI, ML, and data science",
                    "color": "#10B981",
                    "prospect_count": 0,
                    "tags": ["ai", "ml", "data-science"],
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow()
                },
                {
                    "id": generate_id(),
                    "name": "Software Development",
                    "description": "Software development companies and service providers",
                    "color": "#F59E0B",
                    "prospect_count": 0,
                    "tags": ["software", "development", "services"],
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow()
                }
            ]
            
            # Create prospect lists
            for prospect_list in prospect_lists:
                await db_service.create_list(prospect_list)
            print(f"✅ Created {len(prospect_lists)} sample prospect lists")
        else:
            print("✅ Prospect lists already exist, skipping list creation")
            prospect_lists = existing_lists
        
        # Add prospects to lists based on their industry
        if prospect_lists and prospects:
            # Add all prospects to the first list (Technology Companies)
            tech_list_id = prospect_lists[0]["id"]
            prospect_ids = [p["id"] for p in prospects]
            
            # First, let's add the list_ids to the prospects
            for prospect in prospects:
                if "list_ids" not in prospect:
                    prospect["list_ids"] = []
                prospect["list_ids"].append(tech_list_id)
                # Update the prospect in the database
                await db_service.update_prospect(prospect["id"], {"list_ids": prospect["list_ids"]})
            
            print(f"✅ Added {len(prospect_ids)} prospects to Technology Companies list")
            
            # Add AI-related prospects to AI & ML list
            if len(prospect_lists) > 1:
                ai_list_id = prospect_lists[1]["id"]
                ai_prospects = [p for p in prospects if "ai" in p.get("industry", "").lower() or "data" in p.get("industry", "").lower()]
                if ai_prospects:
                    for prospect in ai_prospects:
                        if ai_list_id not in prospect.get("list_ids", []):
                            prospect["list_ids"].append(ai_list_id)
                            await db_service.update_prospect(prospect["id"], {"list_ids": prospect["list_ids"]})
                    print(f"✅ Added {len(ai_prospects)} prospects to AI & ML list")
        
        # Now create a sample campaign using the first template and lists
        existing_campaigns = await db_service.get_campaigns()
        if not existing_campaigns and existing_templates and prospect_lists:
            # Get the first template
            templates = await db_service.get_templates()
            campaign = {
                "id": generate_id(),
                "name": "Q1 2025 Outreach Campaign",
                "template_id": templates[0]["id"],  # Use the actual template ID
                "list_ids": [prospect_lists[0]["id"]],  # Use the first list
                "max_emails": 1000,
                "schedule": None,
                "status": "draft",
                "prospect_count": len(prospects),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
            
            await db_service.create_campaign(campaign)
            print(f"✅ Created sample campaign linked to prospect list")
        else:
            print("✅ Campaign already exists, skipping campaign creation")
        
        print("🎉 Seed data initialization completed successfully!")
        
    except Exception as e:
        print(f"❌ Error initializing seed data: {e}")
        import traceback
        traceback.print_exc()