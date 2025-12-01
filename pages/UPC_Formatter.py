import streamlit as st

def normalize_upc(upc: str) -> str:
    digits = "".join(ch for ch in upc if ch.isdigit())

    if len(digits) == 10:
        return digits

    remove_from_start = True

    while len(digits) > 10:
        if remove_from_start:
            digits = digits[1:]
        else:
            digits = digits[:-1]
        remove_from_start = not remove_from_start

    return digits

def format_skus(text):
    raw_items = text.replace("\n", ",").split(",")
    sku_list = [item.strip() for item in raw_items if item.strip()]
    return [f"'{sku}'" for sku in sku_list]

def format_upcs(text):
    raw_items = text.replace("\n", ",").split(",")
    upc_list = [item.strip() for item in raw_items if item.strip()]
    return [f"'%{normalize_upc(upc)}%'" for upc in upc_list]

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
            formatted = format_skus(input_text)
        else:
            formatted = format_upcs(input_text)
        
        output = ",".join(formatted)

        st.subheader("Result:")
        st.code(output)

        st.success("Done! Copy the result.")