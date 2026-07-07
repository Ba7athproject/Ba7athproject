#!/usr/bin/env python3
"""
Script to fix typo in GitHub repository topics.
Usage: python fix_topics.py <token>
"""

import requests
import sys

def fix_topics_typo(token: str) -> bool:
    """
    Fix the 'javascrip' typo to 'javascript' in repository topics.
    
    Args:
        token: GitHub personal access token
    
    Returns:
        True if successful, False otherwise
    """
    
    # GitHub API endpoint for repository topics
    url = "https://api.github.com/repos/Ba7athproject/Ba7athproject/topics"
    
    # Headers with authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.mercy-preview+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # Updated topics list with corrected 'javascript' (replacing 'javascrip')
    payload = {
        "names": [
            "automation",
            "ba7ath",
            "data-journalism",
            "data-science",
            "developer",
            "education",
            "github-profile",
            "investigation",
            "javascript",  # FIXED: was 'javascrip'
            "ml",
            "open-source",
            "osint",
            "portfolio",
            "profile",
            "python",
            "streamlit",
            "typescript"
        ]
    }
    
    try:
        print("🔄 Fixing typo: 'javascrip' → 'javascript'...\n")
        
        # Make the PUT request
        response = requests.put(url, json=payload, headers=headers)
        
        # Check response status
        if response.status_code == 200:
            print("✅ SUCCESS! Typo fixed!")
            result = response.json()
            print(f"📋 Updated topics: {', '.join(sorted(result.get('names', [])))}")
            return True
        elif response.status_code == 401:
            print("❌ ERROR: Unauthorized - Check your token")
            return False
        elif response.status_code == 404:
            print("❌ ERROR: Repository not found")
            return False
        else:
            print(f"❌ ERROR: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Network error - {e}")
        return False

def main():
    """Main function"""
    
    if len(sys.argv) < 2:
        print("❌ ERROR: GitHub token required!")
        print("\nUsage: python fix_topics.py <YOUR_GITHUB_TOKEN>")
        sys.exit(1)
    
    token = sys.argv[1]
    success = fix_topics_typo(token)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
