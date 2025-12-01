import streamlit as st

def calculate_check_digit(upc: str) -> int:
    digits = [int(d) for d in upc]
    
    odd_sum = (digits[0] + digits[2] + digits[4] + digits[6] + digits[8] + digits[10]) * 3
    even_sum = digits[1] + digits[3] + digits[5] + digits[7] + digits[9]
    
    total = odd_sum + even_sum
    check_digit = (10 - (total % 10)) % 10
    
    return check_digit

def fix_upc(upc: str) -> tuple:
    digits = "".join(ch for ch in upc if ch.isdigit())
    
    if len(digits) < 10 or len(digits) > 12:
        return None, f"Invalid length: {len(digits)} digits"
    
    if len(digits) == 10:
        with_zero = '0' + digits
        check_digit = calculate_check_digit(with_zero)
        fixed = with_zero + str(check_digit)
        return fixed, "10 digits → added '0' + check digit"
    
    elif len(digits) == 11:
        check_digit = calculate_check_digit(digits)
        fixed = digits + str(check_digit)
        return fixed, "11 digits → added check digit"
    
    else:
        return digits, "12 digits → no changes"

def format_upcs(text: str):
    raw_items = text.replace("\n", ",").split(",")
    upc_list = [item.strip() for item in raw_items if item.strip()]
    
    fixed_upcs = []
    details = []
    errors = []
    
    for i, upc in enumerate(upc_list, 1):
        fixed, info = fix_upc(upc)
        if fixed:
            fixed_upcs.append(f"'{fixed}'")
            details.append(f"{i}. `{upc}` → `{fixed}` ({info})")
        else:
            errors.append(f"{i}. `{upc}` → ❌ {info}")
    
    return fixed_upcs, details, errors

st.title("🔧 UPC Fixer")
st.write("Normalize UPCs to 12 digits with check digit. Paste your UPCs (one per line or separated by commas)")

st.info("""
**How it works:**
- **10 digits:** Adds '0' at the beginning + calculates check digit
- **11 digits:** Calculates and adds check digit
- **12 digits:** Keeps the UPC as is
""")

input_text = st.text_area(
    "Paste UPCs:",
    height=200,
    placeholder="12345678901\n1234567890\n123456789012"
)

if st.button("Process UPCs"):
    if not input_text.strip():
        st.error("You must enter at least one UPC.")
    else:
        fixed_upcs, details, errors = format_upcs(input_text)
        
        if errors:
            st.warning("⚠️ Some UPCs could not be processed:")
            for error in errors:
                st.markdown(error)
        
        if fixed_upcs:
            rows = []
            for i in range(0, len(fixed_upcs), 10):
                chunk = fixed_upcs[i:i+10]
                rows.append(",".join(chunk))
            
            output = ",\n".join(rows)
            
            st.success("Done! Copy the result.")
            
            st.subheader("Result (SQL format):")
            st.code(output, language="sql")
            
            with st.expander("View transformation details"):
                for detail in details:
                    st.markdown(detail)
        else:
            st.error("Could not process any valid UPC.")