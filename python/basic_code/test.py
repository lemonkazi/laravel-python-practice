import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
import pytz

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
employee_names = ["Abdullah Al Mamun", "Md. Nazmul Hasan", "Md. Majharul Anwar"]
today = datetime.today().strftime("%-m/%-d/%Y")  # e.g. 8/23/2025
tz = pytz.timezone("Asia/Dhaka")

# --- Streamlit UI ---
st.title("🕒 Employee Attendance")
st.write(f"Today: **{today}**")

selected_employee = st.selectbox("Select Employee", employee_names)

col1, col2 = st.columns(2)

with col1:
    if st.button("Check-in"):
        check_in_time = datetime.now(tz).strftime("%I:%M %p")
        # --- Read all rows ---
        all_rows = sheet.get_all_values()  # includes headers
        headers = [h.strip() for h in all_rows[6]]  # remove spaces

        # Convert headers to lower case for safer matching
        headers_lower = [h.lower() for h in headers]
        
        # Map your expected headers
        name_col = headers_lower.index("name") + 1
        date_col = headers_lower.index("date") + 1
        checkin_col = headers_lower.index("check-in") + 1

        last_date = None
        updated = False
        for idx, row in enumerate(all_rows[7:], start=8):  # sheet rows start after header
            row_name = (row[name_col - 1] or "").strip()
            row_date_str = (row[date_col - 1] or "").strip()

            if row_date_str:
                last_date = row_date_str

            if last_date == today and row_name == selected_employee:
                sheet.update_cell(idx, checkin_col, check_in_time)
                st.success(f"✅ {selected_employee} checked-in at {check_in_time}")
                updated = True
                break
        
        if not updated:
            st.error("⚠️ No matching row found for today's date & employee.")

with col2:
    if st.button("Checkout"):
        check_out_time = datetime.now(tz).strftime("%I:%M %p")
        # --- Read all rows ---
        all_rows = sheet.get_all_values()  # includes headers
        headers = [h.strip() for h in all_rows[6]]  # remove spaces

        # Convert headers to lower case for safer matching
        headers_lower = [h.lower() for h in headers]
        
        # Map your expected headers
        name_col = headers_lower.index("name") + 1
        date_col = headers_lower.index("date") + 1
        checkout_col = headers_lower.index("check-out") + 1

        last_date = None
        updated = False
        for idx, row in enumerate(all_rows[7:], start=8):  # sheet rows start after header
            row_name = (row[name_col - 1] or "").strip()
            row_date_str = (row[date_col - 1] or "").strip()

            if row_date_str:
                last_date = row_date_str

            if last_date == today and row_name == selected_employee:
                sheet.update_cell(idx, checkout_col, check_out_time)
                st.success(f"✅ {selected_employee} checked-out at {check_out_time}")
                updated = True
                break
        
        if not updated:
            st.error("⚠️ No matching row found for today's date & employee.")
