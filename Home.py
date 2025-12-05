
import streamlit as st

st.set_page_config(page_title="Data Team Tools", page_icon="🧠")

st.title("🧠 Data Team Tools")

st.markdown("---")
# How to Use Guide
st.header("UPC/SKU Formatter")

with st.expander("How to Use", expanded=False):
    st.markdown("""
    ### Purpose
    Normalize UPC codes or format SKU codes for SQL queries.
    
    ### Steps
    1. **Choose format type**:
       - Leave unchecked for UPC formatting (default)
       - Check the box for SKU formatting (use this when your codes contain letters)
    
    2. **Paste codes** in the text area:
       - One per line or separated by commas
       - Can include extra digits, spaces, or formatting
    
    3. **Click Process**
    
    4. **Copy the result** from the output box
    
    ### What It Does
    
    **For UPCs (unchecked box)**:
    - Extracts digits only (removes spaces, dashes, letters)
    - Normalizes based on length:
      - **Less than 10 digits**: Formats without modification
      - **10 digits**: Keeps as is
      - **11 digits**: Removes first digit
      - **12 digits**: Removes first and last digit
      - **13 digits**: Removes first digit (converts to UPC), then removes first and last digit
      - **More than 13 digits**: Will not format (listed separately)
    - Formats for SQL: Wraps each UPC in `'%...%'` for ILIKE queries
    
    **For SKUs (checked box)**:
    - Keeps all characters (letters, numbers, special characters)
    - No normalization applied
    - Formats for SQL: Wraps each SKU in `'...'` for exact match queries""")

#################################################
# How to Use Guide
st.header("🛠️ UPC Fixer ")

with st.expander("📖 How to Use", expanded=False):
    st.markdown("""
    ### Purpose
    Normalize UPC codes to 10 digits and format them for SQL queries.
    
    ### Steps
    1. **Paste UPCs** in the text area below
       - One per line or separated by commas
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
    