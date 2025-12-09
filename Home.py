
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
with st.expander("How to Use Guide"):
    st.markdown("""
    ## What is UPC Fixer?
    
    UPC Fixer normalizes Universal Product Codes (UPCs) to the standard 12-digit UPC-A format by adding missing digits and calculating check digits according to a UPC algorithm.
    
    ## The Rules
    
    The tool handles three different scenarios:
    
    ### 1. 10-Digit UPCs
    - **Action:** Adds a leading '0' and calculates the check digit
    - **Example:** `1234567890` → `012345678905`
    - **Why:** UPC-A codes require 12 digits. A 10-digit code is missing both the leading zero and the check digit
    
    ### 2. 11-Digit UPCs
    - **Action:** Calculates and appends the check digit
    - **Example:** `12345678901` → `123456789012`
    - **Why:** The code has the correct prefix but is missing the final verification digit
    
    ### 3. 12-Digit UPCs
    - **Action:** No modification needed
    - **Example:** `123456789012` → `123456789012`
    - **Why:** The code is already in the correct UPC-A format
    
    ## Input Format
    
    You can paste UPCs in any of these formats:
    - **One per line:**
      ```
      1234567890
      12345678901
      123456789012
      ```
    - **Comma-separated:** `1234567890, 12345678901, 123456789012`
    - **Mixed:** Any combination of commas and line breaks
    
    """)
#################################################
st.header("📝 String Formatter")

with st.expander("How to Use Guide", expanded=False):
    st.markdown("""
    ### Purpose
    Format lists of text for SQL `WHERE` clauses (ILIKE/IN) or convert US State names to abbreviations for database queries.

    ### Steps
    1. **Select Formatting Mode**:
       - **ILIKE**: For wildcard/partial searches
       - **IN**: For exact matches
       - **State Abbreviation**: To convert names like "California" to "CA"
    
    2. **Optional Settings**:
       - Check **"Add % between words"** if you are searching for multi-word phrases and want to match them regardless of spacing.

    3. **Paste Data**:
       - Enter words, phrases, or state names (one per line or comma-separated).

    4. **Process & Copy**:
       - Click Process and copy the SQL-ready code block.

    ### Special Feature
    **Add % between words**:
    - Replaces spaces with wildcards `%`. This is useful when data might have extra words in the middle.
    - **Example:** `diet coke` → `'%diet%coke%'` (Will match "Diet Cherry Coke")
    """)