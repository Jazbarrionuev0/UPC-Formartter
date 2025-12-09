import streamlit as st

US_STATES = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR", "california": "CA",
    "colorado": "CO", "connecticut": "CT", "delaware": "DE", "district of columbia": "DC",
    "florida": "FL", "georgia": "GA", "hawaii": "HI", "idaho": "ID", "illinois": "IL",
    "indiana": "IN", "iowa": "IA", "kansas": "KS", "kentucky": "KY", "louisiana": "LA",
    "maine": "ME", "maryland": "MD", "massachusetts": "MA", "michigan": "MI", "minnesota": "MN",
    "mississippi": "MS", "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV",
    "new hampshire": "NH", "new jersey": "NJ", "new mexico": "NM", "new york": "NY",
    "north carolina": "NC", "north dakota": "ND", "ohio": "OH", "oklahoma": "OK",
    "oregon": "OR", "pennsylvania": "PA", "rhode island": "RI", "south carolina": "SC",
    "south dakota": "SD", "tennessee": "TN", "texas": "TX", "utah": "UT", "vermont": "VT",
    "virginia": "VA", "washington": "WA", "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY"
}

def clean_input_list(text):
    """Splits input by newlines or commas and cleans whitespace."""
    raw_items = text.replace("\n", ",").split(",")
    return [item.strip() for item in raw_items if item.strip()]

def format_output_lines(formatted_list):
    """Joins the list into lines of 10 items for readability."""
    output_lines = []
    for i in range(0, len(formatted_list), 10):
        chunk = formatted_list[i:i+10]
        line = ",".join(chunk)
        if i + 10 < len(formatted_list):
            line += ","
        output_lines.append(line)
    return "\n".join(output_lines)

st.set_page_config(page_title="SQL Search Formatter", page_icon="🔍")

st.title("📝 String Formatter")
st.markdown("Format lists of terms for **ILIKE**, **IN**, or convert **US States**.")

col1, col2 = st.columns([2, 1])

with col1:
    search_type = st.radio(
        "Select Formatting Mode:",
        ("ILIKE Search ('%word%')", "IN Search ('word')", "State Abbreviation ('CA')")
    )

with col2:
    st.write("Options:")
    wildcard_between = st.checkbox(
        "Add % between words?", 
        value=False, 
        help="Example: 'pepsi can' becomes '%pepsi%can%'"
    )

input_text = st.text_area("Paste your list here (one per line or comma-separated):", height=200)

if st.button("Process", type="primary"):
    if not input_text.strip():
        st.error("Please paste at least one item.")
    else:
        items = clean_input_list(input_text)
        formatted_results = []
        errors = [] 
        
        for item in items:
            
            if search_type in ["ILIKE Search ('%word%')", "IN Search ('word')"]:
                current_val = item
                
                if wildcard_between:
                    current_val = current_val.replace(" ", "%")
                
                if "ILIKE" in search_type:
                    formatted_results.append(f"'%{current_val}%'")
                else: 
                    formatted_results.append(f"'{current_val}'")

            elif "State" in search_type:
                clean_state = item.lower()
                if clean_state in US_STATES:
                    abbr = US_STATES[clean_state]
                    formatted_results.append(f"'{abbr}'")
                else:
                    errors.append(item)

        if formatted_results:
            final_output = format_output_lines(formatted_results)
            st.subheader("Formatted SQL Result:")
            st.code(final_output, language="sql")
            st.success(f"Formatted {len(formatted_results)} items.")

        if errors:
            st.warning(f"Could not find abbreviations for {len(errors)} items:")
            st.code("\n".join(errors), language="text")