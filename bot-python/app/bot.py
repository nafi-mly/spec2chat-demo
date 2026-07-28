import json
from spec2chat import Chatbot
from openai import OpenAI
from .config import Config
import yaml

class KosanBot:
    def __init__(self):
        # Init OpenAI client with DeepSeek
        self.client = OpenAI(
            api_key=Config.DEEPSEEK_API_KEY,
            base_url=Config.DEEPSEEK_BASE_URL
        )
        
        # Load OpenAPI spec
        with open("app/openapi.yaml", "r") as f:
            spec = yaml.safe_load(f)
        
        # Init spec2chat
        self.bot = Chatbot(
            api_spec=spec,
            llm_client=self.client,
            model=Config.MODEL_NAME,
            system_prompt=Config.SYSTEM_PROMPT,
            backend_url=Config.BACKEND_URL
        )
        
        # Conversation state storage (simple in-memory)
        self.sessions = {}
    
    def process_message(self, user_id: str, message: str) -> str:
        """Main entry point for handling user messages"""
        
        # Get or create session
        if user_id not in self.sessions:
            self.sessions[user_id] = {}
        
        # Process with spec2chat
        result = self.bot.process(
            user_input=message,
            session_state=self.sessions[user_id]
        )
        
        # Update session state
        self.sessions[user_id] = result.state
        
        # Return bot response
        return result.response
    
    def reset_session(self, user_id: str):
        """Reset conversation for a user"""
        if user_id in self.sessions:
            del self.sessions[user_id]