# frontend/helpers/styles.py
# CSS styles for the Campus Buddy application
global_styles = """
<style>
/* Global background and font */
body, .stApp {
    background-color: #D5E3F0;
    color: black;
    font-family: 'Segoe UI', sans-serif;
    font-size: 20px;  /* Increased font */
}

/* Login */
.login-title {
    font-size: 3.5rem;
    font-weight: bold;
    color: #0077b6;
    text-align: center;
    margin-bottom: 0.2rem;
}
.login-subtitle {
    font-size: 1.8rem;
    color: #555;
    text-align: center;
    margin-bottom: 1.5rem;
}

/* Cards */
.complaint-card {
    background-color: white;
    border-radius: 15px;
    padding: 1.4rem;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
    margin-bottom: 1.4rem;
    transition: transform 0.2s;
    font-size: 20px;
}
.complaint-card:hover {
    transform: translateY(-3px);
}

/* Status bars */
.status-bar {
    height: 10px;
    border-radius: 4px;
    margin-bottom: 0.5rem;
}
.status-pending { background-color: #FF4C4C; }      /* Red */
.status-in-progress { background-color: #FFD700; }  /* Yellow */
.status-resolved { background-color: #4CAF50; }     /* Green */

/* Sidebar */
.sidebar-box {
    padding:1rem; 
    background-color:white; 
    border-radius:15px; 
    box-shadow:0px 5px 15px rgba(0,0,0,0.1);
    margin-bottom:1rem;
    font-size: 20px;
}
</style>
"""
