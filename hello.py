#!/usr/bin/env python3
"""
GitHub Action script that reads names from a YAML file and prints greetings.
"""

import sys
import yaml
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python hello.py <yaml_file_path>")
        sys.exit(1)
    
    yaml_file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(yaml_file_path):
        print(f"Error: File '{yaml_file_path}' not found.")
        sys.exit(1)
    
    try:
        # Read and parse the YAML file
        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        # Extract names from the YAML data
        names = []
        if isinstance(data, dict):
            # If the YAML has a 'names' key
            if 'names' in data:
                names = data['names']
            # If the YAML has other structure, try to find a list
            else:
                for value in data.values():
                    if isinstance(value, list):
                        names = value
                        break
        elif isinstance(data, list):
            # If the YAML is directly a list of names
            names = data
        
        if not names:
            print("No names found in the YAML file.")
            return
        
        # Print greetings for each name
        print("🎉 Greeting everyone:")
        for name in names:
            if isinstance(name, str):
                print(f"Hello, {name}!")
            else:
                print(f"Hello, {str(name)}!")
        
        print(f"\n✅ Successfully greeted {len(names)} people!")
        
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()