import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

# --- Google Sheets Auth ---
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
script_dir = os.path.dirname(os.path.abspath(__file__))
credential_path = os.path.join(script_dir, 'credential.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(credential_path, scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("Monthly Attendance Sheet").worksheet("August25")

# --- Settings ---
employee_name = "Abdullah Al Mamun"
today = datetime.today().strftime("%-m/%-d/%Y")  # e.g. 8/23/2025

# --- Streamlit UI ---
st.title("🕒 Employee Attendance")
st.write(f"Today: **{today}**")
st.write(f"Employee: **{employee_name}**")

check_in_input = st.text_input("Enter Check-in Time (e.g. 09:00 AM)")
check_out_input = st.text_input("Enter Check-out Time (e.g. 05:00 PM)")

if st.button("Save Attendance"):
    # --- Read all rows ---
    all_rows = sheet.get_all_values()  # includes headers
    headers = [h.strip() for h in all_rows[6]]  # remove spaces

    # Convert headers to lower case for safer matching
    headers_lower = [h.lower() for h in headers]
    #st.write("Headers:", headers)

    # Map your expected headers
    name_col = headers_lower.index("name") + 1
    date_col = headers_lower.index("date") + 1
    checkin_col = headers_lower.index("check-in") + 1
    checkout_col = headers_lower.index("check-out") + 1
    # all_rows = sheet.get_all_values()  # includes headers
    # headers = all_rows[0]
    # name_col = headers.index("Name") + 1
    # date_col = headers.index("Date") + 1
    # checkin_col = headers.index("Check-in") + 1
    # checkout_col = headers.index("Check-out") + 1

    last_date = None
    updated = False
    today_obj = datetime.today().date()  # current date object

    for idx, row in enumerate(all_rows[7:], start=8):  # sheet rows start after header
        row_name = (row[name_col - 1] or "").strip()
        row_date_str = (row[date_col - 1] or "").strip()


        # Convert row_date to date object if exists
        if row_date_str:
            last_date = row_date_str

        # Debug
        # st.write("Row index:", idx)
        # st.write("row_name:", row_name)
        # st.write("row_date_str:", row_date_str)
        # st.write("last_date:", last_date)

        # Check if this row matches today and employee
        if last_date == today and row_name == employee_name:
            if check_in_input:
                sheet.update_cell(idx, checkin_col, check_in_input)
                st.success(f"✅ Check-in updated: {check_in_input}")

            if check_out_input:
                sheet.update_cell(idx, checkout_col, check_out_input)
                st.success(f"✅ Check-out updated: {check_out_input}")

            updated = True
            break

    if not updated:
        st.error("⚠️ No matching row found for today's date & employee.")
