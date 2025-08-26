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

# --- Refactored Function for Updating Attendance ---
def update_attendance(employee: str, date_str: str, column_name: str, time_str: str) -> bool:
    """
    Updates the specified column (e.g., 'check-in' or 'check-out') for the given employee and date in the Google Sheet.

    Args:
        employee (str): The employee's name.
        date_str (str): The date in format like '8/23/2025'.
        column_name (str): The column header to update (e.g., 'check-in').
        time_str (str): The time string to write.

    Returns:
        bool: True if updated successfully, False otherwise.
    """
    # Read all rows once
    all_rows = sheet.get_all_values()  # includes headers
    headers = [h.strip() for h in all_rows[6]]  # headers in row 7 (index 6)

    # Convert headers to lower case for case-insensitive matching
    headers_lower = [h.lower() for h in headers]

    # Find column indices (1-based for sheet.update_cell)
    try:
        name_col = headers_lower.index("name") + 1
        date_col = headers_lower.index("date") + 1
        target_col = headers_lower.index(column_name.lower()) + 1
        checkin_col = headers_lower.index("check-in") + 1
        checkout_col = headers_lower.index("check-out") + 1
        hours_logged_col = headers_lower.index("hours logged") + 1
        over_time_col = headers_lower.index("over time") + 1
        attendance_status_col = headers_lower.index("attendance status") + 1
    except ValueError as e:
        st.error(f"⚠️ Column not found in headers. {e}")
        return False

    last_date = None
    for idx, row in enumerate(all_rows[7:], start=8):  # data starts from row 8
        row_name = (row[name_col - 1] or "").strip()
        row_date_str = (row[date_col - 1] or "").strip()

        if row_date_str:
            last_date = row_date_str

        if last_date == date_str and row_name == employee:
            sheet.update_cell(idx, target_col, time_str)

            # If updating 'check-out', calculate and update other columns
            if column_name.lower() == "check-out":
                checkin_time_str = row[checkin_col - 1]
                if checkin_time_str:
                    try:
                        # Parse time strings and calculate time difference
                        checkin_time = datetime.strptime(checkin_time_str, "%I:%M %p")
                        checkout_time = datetime.strptime(time_str, "%I:%M %p")
                        hours_logged = (checkout_time - checkin_time).total_seconds() / 3600
                        over_time = hours_logged - 8.0

                        # Update 'Hours Logged', 'Over Time', and 'Attendance Status' columns
                        sheet.update_cell(idx, hours_logged_col, str(round(hours_logged, 2)))
                        sheet.update_cell(idx, over_time_col, str(round(over_time, 2)))
                        sheet.update_cell(idx, attendance_status_col, "Present")
                    except ValueError:
                        st.error(f"⚠️ Could not parse check-in or check-out time for {employee} on {date_str}.")
                        return False
                else:
                    st.warning(f"⚠️ Check-in time not found for {employee} on {date_str}.")

            return True

    return False

# --- Streamlit UI ---
st.title("🕒 Employee Attendance")

clock_html = """
    <div id="clock" style="color:white; text-align: center; font-size: 48px; font-weight: bold;"></div>
    <div id="date" style="color:white; text-align: center; font-size: 30px; font-weight: bold;"></div>

    <script>
    function updateClock() {
        const now = new Date();
        const formatter = new Intl.DateTimeFormat('en-US', {
            timeZone: 'Asia/Dhaka',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: true
        });
        document.getElementById('clock').innerHTML = formatter.format(now);
        const dateFormatter = new Intl.DateTimeFormat('en-US', {
            timeZone: 'Asia/Dhaka',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
        document.getElementById('date').innerHTML = dateFormatter.format(now);
    }
    updateClock();
    setInterval(updateClock, 1000);
    </script>
    """

st.components.v1.html(clock_html, height=100)

selected_employee = st.selectbox("Select Employee", employee_names)

# ... existing code ...
# Create three columns: left for check-in, middle for clock, right for check-out
col1, col3 = st.columns([1,1])  # Middle column wider for the clock



with col1:
    if st.button("Check-in"):
        check_in_time = datetime.now(tz).strftime("%I:%M %p")
        if update_attendance(selected_employee, today, "check-in", check_in_time):
            st.success(f"✅ {selected_employee} checked-in at {check_in_time}")
        else:
            st.error("⚠️ No matching row found for today's date & employee.")

with col3:
    if st.button("Checkout"):
        check_out_time = datetime.now(tz).strftime("%I:%M %p")
        if update_attendance(selected_employee, today, "check-out", check_out_time):
            st.success(f"✅ {selected_employee} checked-out at {check_out_time}")
        else:
            st.error("⚠️ No matching row found for today's date & employee.")
