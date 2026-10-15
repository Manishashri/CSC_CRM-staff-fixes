# CSC-CRM change-request - what was changed

Run `python manage.py migrate` after replacing the code (converts existing +91 phone numbers to 10 digits).

| Req | Change | Main files |
|----|--------|-------|
| 01 | Student Overview = Active / Completed / Long-Absent from real records. Active/Completed are decided from batch dates (same rule as `Batch.display_status`), not the manual Status field. Long-Absent = latest N attendance records all Absent (`LONG_ABSENT_CONSECUTIVE_DAYS`, placeholder 7 - NOT confirmed) | `apps/staff/views.py`, `apps/student_attendance/attendance_utils.py`, `templates/staff/dashboard.html` |
| 02 | Batch strength dynamic: adding a student raises enrolled count AND batch total (3/30 -> 4/31); removal/transfer reverses | `apps/admissions/models.py` |
| 03 | Employee ID typed manually; unique + live duplicate check | `apps/staff/forms.py`, `views.py`, `urls.py`, `add_staff.html`, `add_staff.js` |
| 04 | Overview > Recent Leads > View All shows only that staff's leads | `apps/leads/views.py`, `urls.py`, `templates/leads/staff_assigned_leads.html`, `overview.html` |
| 05 | Total Working Days fixed at 28 (`STAFF_TOTAL_WORKING_DAYS`) | `csc_crm/settings.py`, `apps/staff/views.py` |
| 06 | Check-in 9:00 + 30 min grace: <= 9:30:00 Present, after Late | `csc_crm/settings.py`, `apps/staff/views.py` |
| 07 | Phone = 10 digits, starts 6/7/8/9, no +91, everywhere + data migrations | `csc_crm/validators.py`, `static/js/phone_validation.js`, migrations `staff/0024`, `leads/0016`, `admissions/0008` |

Business-rule values are at the bottom of `csc_crm/settings.py`.
