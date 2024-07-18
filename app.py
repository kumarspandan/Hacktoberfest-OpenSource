import streamlit as st
import requests
import re
import os
# All Functions for fetching email
def get_repos(user, token, sort='created', direction='desc'):
    headers = {
        'Authorization': f'token {token}'
    }
    
    repos_url = f"https://api.github.com/users/{user}/repos"
    repos_params = {
        'type': 'owner',
        'sort': sort,
        'direction': direction
    }
    
    repos_response = requests.get(repos_url, headers=headers, params=repos_params)
    if repos_response.status_code == 401:
        st.error("Error: Unauthorized. The provided token may be expired or invalid.")
        return None
    if repos_response.status_code != 200:
        st.error(f"Error fetching repositories: {repos_response.status_code}")
        return None
    
    return repos_response.json()

def get_commits(user, repo, token, direction='desc'):
    headers = {
        'Authorization': f'token {token}'
    }
    
    commits_url = f"https://api.github.com/repos/{user}/{repo}/commits"
    commits_params = {
        'direction': direction
    }
    
    commits_response = requests.get(commits_url, headers=headers, params=commits_params)
    if commits_response.status_code == 401:
        st.error("Error: Unauthorized. The provided token may be expired or invalid.")
        return None
    if commits_response.status_code != 200:
        st.error(f"Error fetching commits for {repo}: {commits_response.status_code}")
        return None
    
    return commits_response.json()

def get_patch_data(commit_url):
    patch_url = commit_url + ".patch"
    response = requests.get(patch_url)
    
    if response.status_code == 401:
        st.error("Error: Unauthorized. The provided token may be expired or invalid.")
        return None
    if response.status_code != 200:
        st.error(f"Error fetching patch data: {response.status_code}")
        return None
    
    return response.text

def extract_email(patch_data):
    
    # Regex to extract email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.search(email_pattern, patch_data)
    if match:
        email = match.group(0)
        if "@users.noreply.github.com" in email:
            return None
        return email
    return None

def get_commit_email(user, token, sort='created', direction='desc'):
    repos = get_repos(user, token, sort=sort, direction=direction)
    
    if not repos:
        st.info("No repositories found for the user.")
        return None
    
    for repo in repos:
        commits = get_commits(user, repo['name'], token, direction)
        if commits is None:
            continue
        
        for commit in commits:
            if commit['author'] and commit['author']['login'] == user:
                commit_url = commit['html_url']
                patch_data = get_patch_data(commit_url)
                if patch_data is None:
                    continue
                
                email = extract_email(patch_data)
                if email:
                    return email
    
    return None

def get_user_profile(user, token):
    headers = {
        'Authorization': f'token {token}'
    }
    
    user_url = f"https://api.github.com/users/{user}"
    
    user_response = requests.get(user_url, headers=headers)
    if user_response.status_code == 401:
        st.error("Error: Unauthorized. The provided token may be expired or invalid.")
        return None
    if user_response.status_code != 200:
        st.error(f"Error fetching user profile: {user_response.status_code}")
        return None
    
    return user_response.json()

# User Interface Starts here
st.title("OsintHub")
st.write("An Open Source Intelligence Tool to Find the Email Addresses of GitHub Users")

username = st.text_input("GitHub Username", "")

token = os.getenv('ghtoken')
#st.write(token)
if st.button("Fetch Email"):
    if username:
        with st.spinner("Fetching details..."):
            try:
                profile = get_user_profile(username, token)
                email = get_commit_email(username, token, sort='created', direction='desc')
                if not email:
                    email = get_commit_email(username, token, sort='created', direction='asc')

                if profile:
                    st.image(profile['avatar_url'], width=100)
                    st.write(f"**User ID:** {profile['id']}")
                    st.write(f"**Username:** {profile['login']}")
                    if email:
                        st.success(f"**Email:** {email}")
                    else:
                        st.warning("No email found data.")
                else:
                    st.warning("Failed to fetch user profile.")

            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Please enter both username and token.")


