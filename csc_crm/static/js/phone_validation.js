// =====================================================================
// SHARED PHONE NUMBER RULE  (Requirement 07)
//   * exactly 10 digits
//   * first digit must be 6, 7, 8 or 9
//   * NO "+91" prefix
// Keep in sync with csc_crm/validators.py
// Loaded from the staff / admissions / leads base templates.
// =====================================================================
window.CSCPhone = (function () {

    var PATTERN = /^[6-9]\d{9}$/;

    var MSG_REQUIRED = "Phone number is required.";
    var MSG_DIGITS   = "Phone number must contain digits only (do not enter +91 or any symbols).";
    var MSG_LENGTH   = "Phone number must be exactly 10 digits.";
    var MSG_START    = "Phone number must start with 6, 7, 8 or 9.";

    // Remove everything that is not a digit and keep max 10 digits
    function sanitize(value) {
        return String(value || "").replace(/\D/g, "").slice(0, 10);
    }

    // Returns "" when valid, otherwise the message to show
    function error(value, required) {
        value = String(value || "").trim();

        if (value === "") {
            return required === false ? "" : MSG_REQUIRED;
        }
        if (!/^\d+$/.test(value)) return MSG_DIGITS;
        if (value.length !== 10)  return MSG_LENGTH;
        if (!PATTERN.test(value)) return MSG_START;
        return "";
    }

    function isValid(value) {
        return PATTERN.test(String(value || "").trim());
    }

    return {
        PATTERN: PATTERN,
        sanitize: sanitize,
        error: error,
        isValid: isValid
    };
})();
