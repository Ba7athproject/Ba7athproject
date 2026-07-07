#!/usr/bin/env python3
"""
Script to add topics to a GitHub repository using the GitHub API.
Usage: python add_topics.py <token> <owner> <repo> <topics>
"""

import requests
import sys
from typing import List

def add_topics_to_repo(token: str, owner: str, repo: str, topics: List[str]) -> bool:
    """
    Add topics to a GitHub repository using the GitHub API.
    
    Args:
        token: GitHub personal access token
        owner: Repository owner (username)
        repo: Repository name
        topics: List of topics to add
    
    Returns:
        True if successful, False otherwise
    """
    
    # GitHub API endpoint for repository topics
    url = f"https://api.github.com/repos/{owner}/{repo}/topics"
    
    # Headers with authentication and API preview header (required for topics)
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.mercy-preview+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # Payload with topics
    payload = {
        "names": topics
    }
    
    try:
        print(f"🔄 Adding {len(topics)} topics to {owner}/{repo}...")
        print(f"📌 Topics: {', '.join(topics)}\n")
        
        # Make the PUT request
        response = requests.put(url, json=payload, headers=headers)
        
        # Check response status
        if response.status_code == 200:
            print("✅ SUCCESS! Topics added successfully!")
            result = response.json()
            print(f"📋 Final topics: {', '.join(result.get('names', []))}")
            return True
        elif response.status_code == 401:
            print("❌ ERROR: Unauthorized - Check your token")
            return False
        elif response.status_code == 404:
            print(f"❌ ERROR: Repository not found - {owner}/{repo}")
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
    
    # Topics to add
    topics = [
        # Génériques
        "profile", "portfolio", "developer", "osint", "datajournalism", 
        "github-profile", "open-source",
        # Langages
        "python", "javascript", "typescript",
        # Domaines
        "web-development", "full-stack", "devops", "machine-learning", 
        "data-science",
        # Autres
        "education", "journalism", "investigative-journalism"
    ]
    
    # Repository info
    owner = "Ba7athproject"
    repo = "Ba7athproject"
    
    # Check if token is provided
    if len(sys.argv) < 2:
        print("❌ ERROR: GitHub token required!")
        print("\nUsage: python add_topics.py <YOUR_GITHUB_TOKEN>")
        print("\nTo get a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select 'repo' scope")
        print("4. Copy the token and use it as argument")
        sys.exit(1)
    
    token = sys.argv[1]
    
    # Call the function
    success = add_topics_to_repo(token, owner, repo, topics)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
