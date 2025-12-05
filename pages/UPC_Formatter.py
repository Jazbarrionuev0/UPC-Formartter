import streamlit as st

def normalize_upc(upc: str) -> str:
    digits = "".join(ch for ch in upc if ch.isdigit())
    
    if len(digits) == 10:
        return digits
    
    elif len(digits) == 11:
        return digits[1:]
    
    elif len(digits) == 12:
        return digits[1:-1]
    
    elif len(digits) == 13:
        digits = digits[1:]
        return digits[1:-1]
    
    else:
        return digits

def format_skus(text):
    raw_items = text.replace("\n", ",").split(",")
    sku_list = [item.strip() for item in raw_items if item.strip()]
    formatted = [f"'{sku}'" for sku in sku_list]
    
    output_lines = []
    for i in range(0, len(formatted), 10):
        chunk = formatted[i:i+10]
        line = ",".join(chunk)
        if i + 10 < len(formatted):
            line += ","
        output_lines.append(line)
    
    return "\n".join(output_lines)

def format_upcs(text):
    raw_items = text.replace("\n", ",").split(",")
    upc_list = [item.strip() for item in raw_items if item.strip()]
    
    formatted = []
    too_long = []
    
    for upc in upc_list:
        digits = "".join(ch for ch in upc if ch.isdigit())
        if len(digits) > 13:
            too_long.append(upc)
        else:
            formatted.append(f"'%{normalize_upc(upc)}%'")
    
    output_lines = []
    for i in range(0, len(formatted), 10):
        chunk = formatted[i:i+10]
        line = ",".join(chunk)
        if i + 10 < len(formatted):
            line += ","
        output_lines.append(line)
    
    return "\n".join(output_lines), too_long

st.title("🔢 UPC/SKU Formatter")

is_sku = st.checkbox("Format as SKU (no normalization, no wildcards)", value=False)

if is_sku:
    st.write("Paste SKUs (one per line or separated by commas). The app will format them for SQL without modification.")
else:
    st.write("Paste UPCs (one per line or separated by commas). The app will normalize them and return them in SQL format.")

input_text = st.text_area("Paste UPCs/SKUs:")

if st.button("Process"):
    if not input_text.strip():
        st.error("You must paste at least one UPC/SKU.")
    else:
        
        if is_sku:
            output = format_skus(input_text)
            st.subheader("Result:")
            st.code(output)
            st.success("Done! Copy the result.")
        else:
            output, too_long = format_upcs(input_text)
            
            if output:
                st.subheader("Result:")
                st.code(output)
                st.success("Done! Copy the result.")
            
            if too_long:
                st.subheader("UPCs with more than 13 digits (not formatted):")
                st.code("\n".join(too_long))