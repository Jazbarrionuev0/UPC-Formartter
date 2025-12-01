
import streamlit as st

st.set_page_config(page_title="Data Team Tools", page_icon="🧠")

st.title("🧠 Data Team Tools")

st.markdown("---")
# How to Use Guide
st.header("🔢 UPC Formatter ")

with st.expander("📖 How to Use", expanded=False):
    st.markdown("""
    ### Purpose
    Normalize UPC codes to 10 digits and format them for SQL queries.
    
    ### Steps
    1. **Paste UPCs** in the text area below
       - One per line, OR
       - Separated by commas
       - Can include extra digits, spaces, or formatting
    
    2. **Click Process**
    
    3. **Copy the result** from the output box
    
    ### What It Does
    - **Extracts digits only** (removes spaces, dashes, letters)
    - **Normalizes to 10 digits**:
      - If UPC has 10 digits → keeps as is
      - If UPC has more than 10 digits → alternately removes from start/end until 10 remain
      - Example: `012345678901` (12 digits) → `1234567890` (10 digits)
    - **Formats for SQL**: Wraps each UPC in `'%...%'` for ILIKE queries""")

#################################################
# How to Use Guide

st.title("🔧 UPC Fixer")

with st.expander("📖 How to Use", expanded=False):
    st.markdown("""
    ### Purpose
    Normalize UPC codes to 12 digits with valid check digit for SQL IN clauses.
    
    ### Steps
    1. **Paste UPCs** in the text area below
       - One per line, OR
       - Separated by commas
       - Can include extra characters, spaces, or formatting
    
    2. **Click Process UPCs**
    
    3. **Copy the result** from the output box
    
    ### What It Does
    - **Extracts digits only** (removes spaces, dashes, letters)
    - **Normalizes to 12 digits with check digit**:
      - If UPC has 10 digits → adds '0' at start + calculates check digit
      - If UPC has 11 digits → calculates and adds check digit at end
      - If UPC has 12 digits → keeps as is
    - **Formats for SQL**: Wraps each UPC in single quotes for IN queries
    - **Groups output**: 10 UPCs per line for readability
    
    ### Check Digit Algorithm
    Uses the standard UPC-A check digit calculation:
    1. Multiply digits in odd positions (1,3,5,7,9,11) by 3
    2. Add digits in even positions (2,4,6,8,10)
    3. Sum results and calculate modulo 10
    4. Subtract from 10 and calculate modulo 10 again
    """)