!pip install streamlit-authenticator

import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Vishesh", "Radhakrishnan", "Sagar", "Jin Xuemin"]
usernames = ['vishesh', 'sriradhakrishnan', "s.kamarthi", "j.xuemin"]
passwords = ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX']

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed1_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

