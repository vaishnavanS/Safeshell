import sys
import subprocess
import os
from engine import RuleEngine
from context import get_context

def handle_command(command_str, engine):
    if not command_str.strip():
        return

    status, message = engine.validate_command(command_str)

    print(f"\n[AI-SafeShell] Checking command: '{command_str}'")
    
    if status == "block":
        print(f"❌ BLOCKED: {message}")
        return
    
    elif status == "confirm":
        print(f"⚠️ ATTENTION: {message}")
        confirm = input("Do you want to proceed? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled by user.")
            return
    
    elif status == "allow":
        print(f"✅ ALLOWED: {message}")
    
    else:
        print(f"❓ UNKNOWN: {message}")
        confirm = input("Do you want to proceed? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled by user.")
            return

    # Execute the command
    try:
        subprocess.run(command_str, shell=True)
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    engine = RuleEngine()
    
    if len(sys.argv) > 1:
        # Single command mode
        command_str = " ".join(sys.argv[1:])
        handle_command(command_str, engine)
    else:
        # Interactive mode
        print("--- AI-SafeShell Interactive Mode ---")
        print("Type 'exit' or 'quit' to leave.")
        while True:
            try:
                command_str = input("\nSafeShell> ")
                if command_str.lower() in ['exit', 'quit']:
                    break
                handle_command(command_str, engine)
            except KeyboardInterrupt:
                print("\nUse 'exit' to leave.")
            except EOFError:
                break

if __name__ == "__main__":
    main()
