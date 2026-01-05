import yaml
import re
import os
from context import get_context

class RuleEngine:
    def __init__(self, rules_path="rules.yaml"):
        self.rules_path = rules_path
        self.rules = self._load_rules()

    def _load_rules(self):
        if not os.path.exists(self.rules_path):
            print(f"Warning: Rules file {self.rules_path} not found. Using default empty rules.")
            return {"block": [], "confirm": [], "allow": [], "rewrite": []}
        
        with open(self.rules_path, 'r') as f:
            try:
                data = yaml.safe_load(f)
                return data.get("rules", {})
            except yaml.YAMLError as e:
                print(f"Error parsing rules.yaml: {e}")
                return {"block": [], "confirm": [], "allow": [], "rewrite": []}

    def validate_command(self, command_str):
        """
        Validates a command against the rules and current context.
        Returns: (status, message)
        Status: 'block', 'confirm', 'allow', 'unknown'
        """
        # 1. Check Hard Blocks
        for rule in self.rules.get("block", []):
            if re.search(rule["pattern"], command_str):
                return "block", rule.get("explanation", "Command is blocked by security policy.")

        # 2. Check Confirmations
        for rule in self.rules.get("confirm", []):
            if re.search(rule["pattern"], command_str):
                return "confirm", rule.get("explanation", "This command requires confirmation.")

        # 3. Check Auto-Allows
        for rule in self.rules.get("allow", []):
            if re.search(rule["pattern"], command_str):
                return "allow", "Command is in the allow-list."

        # Default: If not matched, we might want to ask for confirmation or allow depending on policy
        return "unknown", "Command not explicitly matched in rules. Proceed with caution?"

if __name__ == "__main__":
    # Test cases
    engine = RuleEngine()
    test_commands = [
        "ls -la",
        "rm -rf /",
        "rm -rf build/",
        "docker system prune",
        "git status",
        "unknown_cmd --flags"
    ]
    
    for cmd in test_commands:
        status, msg = engine.validate_command(cmd)
        print(f"CMD: {cmd}\nSTATUS: {status}\nMSG: {msg}\n{'-'*20}")
