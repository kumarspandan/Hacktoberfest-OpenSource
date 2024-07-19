# Osintgit

**Osintgit** is an open-source-intelligence tool designed to find **email** of **GitHub** users for *contact* purposes 🕊

It is built using Python and hosted on Streamlit 🛶

## Features

💌 Extract and display email addresses associated with GitHub accounts (if available) 
  
🙈 Search for GitHub user profiles 
  
✨ Simple and intuitive web interface using Streamlit

> [!NOTE]  
> Now you can use it without downloading anything—completely from your browser, with no tedious setup required.

##

> [!WARNING]
> For those who want to download it, follow the steps below.
### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps
#### Open your terminal
1. **Clone the repository:**

   ```bash
   git clone https://github.com/ByteJoseph/osintgit.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd osintgit
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set the GitHub Personal Access Token:**
   
   Before starting the Streamlit app, you need to set the GitHub Personal Access Token as an environment variable. Replace `"your_github_personal_access_token"` with your actual token.

   For Linux/MacOS:

   ```bash
   export ghtoken="your_github_personal_access_token"
   ```
   For Windows (Command Prompt):

   ```bash
   set ghtoken=your_github_personal_access_token
   ```
6. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   This will start a local server and open the app in your default web browser.
# Diagram of how this works
[![](https://mermaid.ink/img/pako:eNqFVV1zojAU_SuZPFPHL3TlYTsqfrZaq7uzXcGHCFGZSuKEsK2r_vcNCWgqOpsHhuSec-65SS4coEd9DC242tIPb4MYBz9slwAxms6Mi_kCPDx8By3nZ4QZGJBdzBcq3pKBttMhXER6Ae_HS5CgCApximlLjO30MAedEAVb0Io5pwS0t4H3jv3HFKeeUbxcM7TbSJWmxwNKVCAZtpQ6_sbREXSc2YZ-gNkuIASzRQ40pkfQVKuY-C65ku9i7m2SHBNGV8EWX_gdye9Kv7LgFKGl6KoUaQB0aUz8I-hJyhTvaBRwygIc3aeMKc9ob6qQX4iRgKwt0BVbhH3AqfJ4y8OtgvS8TeK3aRgGPLoY6CkDOixz0He6lIEO8jSV_SJHHdMvSY5grpwPyIpa4CqqtDWRy1tfyg3kbqU2NdxAJUsDmcXhxaKK5BnCQEoSFd3KO5S4J0ehwHIvt_ZRU3rS7tez9DdByRHYiKM8LLlhw1uJntOzPnOzKkZO55Mz5KWNsMhRRA0X1h31kYKqVkr1sBAfpw0Rex6OIiuXYnROkaMO71-rRDPXImMp9aIS3umRl68XfpSUlezrRLGaf0SFzFDsgW1cfzU0CWVX65jXq445l3T_zk2k1PQ_WzSVqOZl4VVf0LbnTV-fZxNowBAzoemLj-khCbqQb3CIXWiJVx-xdxe65CRwKOZ0ticetDiLsQEZjdcbaK3QNhKzeOcjju0AiTMIM8gOkTml4Rkk5tA6wE9omaVioVytNMx6rdooNcyKacA9tCp1s1AuV0vVRq34rVyp1U8G_CsVioVqQ41Ko1YrmmbZgNhPOnek_gTyh3D6B4HVzwU?type=png)](https://mermaid.live/edit#pako:eNqFVV1zojAU_SuZPFPHL3TlYTsqfrZaq7uzXcGHCFGZSuKEsK2r_vcNCWgqOpsHhuSec-65SS4coEd9DC242tIPb4MYBz9slwAxms6Mi_kCPDx8By3nZ4QZGJBdzBcq3pKBttMhXER6Ae_HS5CgCApximlLjO30MAedEAVb0Io5pwS0t4H3jv3HFKeeUbxcM7TbSJWmxwNKVCAZtpQ6_sbREXSc2YZ-gNkuIASzRQ40pkfQVKuY-C65ku9i7m2SHBNGV8EWX_gdye9Kv7LgFKGl6KoUaQB0aUz8I-hJyhTvaBRwygIc3aeMKc9ob6qQX4iRgKwt0BVbhH3AqfJ4y8OtgvS8TeK3aRgGPLoY6CkDOixz0He6lIEO8jSV_SJHHdMvSY5grpwPyIpa4CqqtDWRy1tfyg3kbqU2NdxAJUsDmcXhxaKK5BnCQEoSFd3KO5S4J0ehwHIvt_ZRU3rS7tez9DdByRHYiKM8LLlhw1uJntOzPnOzKkZO55Mz5KWNsMhRRA0X1h31kYKqVkr1sBAfpw0Rex6OIiuXYnROkaMO71-rRDPXImMp9aIS3umRl68XfpSUlezrRLGaf0SFzFDsgW1cfzU0CWVX65jXq445l3T_zk2k1PQ_WzSVqOZl4VVf0LbnTV-fZxNowBAzoemLj-khCbqQb3CIXWiJVx-xdxe65CRwKOZ0ticetDiLsQEZjdcbaK3QNhKzeOcjju0AiTMIM8gOkTml4Rkk5tA6wE9omaVioVytNMx6rdooNcyKacA9tCp1s1AuV0vVRq34rVyp1U8G_CsVioVqQ41Ko1YrmmbZgNhPOnek_gTyh3D6B4HVzwU)
 


