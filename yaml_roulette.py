#!/usr/bin/env python3
"""
YAML Roulette: Russian Roulette for your YAML files.
Will it parse? Will it explode? Let's find out!
"""

import sys
import yaml
from pathlib import Path


def play_roulette(yaml_path):
    """
    Pull the trigger on a YAML file.
    Returns: True if you survive, False if it blows up in your face.
    """
    try:
        with open(yaml_path, 'r') as f:
            content = f.read()
        
        # The moment of truth...
        yaml.safe_load(content)
        
        print("🎉 Click! You survived this round of YAML Roulette!")
        print("   (Your YAML is actually valid. How boring.)")
        return True
        
    except yaml.YAMLError as e:
        print("💥 BANG! Your YAML just exploded!")
        print(f"\nError details (good luck with these):")
        print(f"  {e.problem if hasattr(e, 'problem') else e}")
        
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            print(f"\nThe smoking gun is at line {mark.line + 1}, column {mark.column + 1}")
            
            # Show the crime scene
            lines = content.split('\n')
            if mark.line < len(lines):
                print(f"\nOffending line:\n  {lines[mark.line]}")
                print(f"  {' ' * mark.column}^")
        
        return False
    except FileNotFoundError:
        print("🤡 You tried to shoot a file that doesn't exist. Smooth.")
        return False


def main():
    """Main function - because every script needs one of these"""
    if len(sys.argv) != 2:
        print("Usage: python yaml_roulette.py <your-yaml-file>")
        print("Example: python yaml_roulette.py config.yml")
        sys.exit(1)
    
    yaml_file = Path(sys.argv[1])
    
    print(f"\n🔫 Loading YAML Roulette with {yaml_file}...")
    print("Spinning the chamber...")
    
    survived = play_roulette(yaml_file)
    
    if not survived:
        print("\n💡 Pro tip: Check your indentation. It's ALWAYS the indentation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
