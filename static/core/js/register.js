document.addEventListener("DOMContentLoaded", function () {

    /* ================= PHONE INPUT ================= */
    const phoneInput = document.querySelector("#phone_input");

    const iti = window.intlTelInput(phoneInput, {
        initialCountry: "in",
        separateDialCode: true,
        nationalMode: true,
        utilsScript:
            "https://cdn.jsdelivr.net/npm/intl-tel-input@19.5.6/build/js/utils.js"
    });

    const hiddenCountry = document.querySelector("#id_phone_country_code");
    const hiddenLocal = document.querySelector("#id_local_phone_number");

    function syncPhone() {
        const data = iti.getSelectedCountryData();
        hiddenCountry.value = "+" + data.dialCode;

        // Digits only + max 10
        let digits = phoneInput.value.replace(/[^0-9]/g, "");
        digits = digits.substring(0, 10);

        phoneInput.value = digits;
        hiddenLocal.value = digits;
    }

    phoneInput.addEventListener("input", syncPhone);
    phoneInput.addEventListener("countrychange", syncPhone);

    // Hard block non-numeric keys
    phoneInput.addEventListener("keypress", function (e) {
        if (!/[0-9]/.test(e.key)) {
            e.preventDefault();
        }
    });

    /* ================= NATIONALITY FLAGS ================= */
    function formatCountry(option) {
        if (!option.id) return option.text;

        const code = option.id.toLowerCase();
        const flagUrl = `https://flagcdn.com/w20/${code}.png`;

        return $(
            `<span>
                <img src="${flagUrl}" style="width:18px;margin-right:8px;vertical-align:middle;">
                ${option.text}
            </span>`
        );
    }

    $("#id_nationality").select2({
        templateResult: formatCountry,
        templateSelection: formatCountry,
        width: "100%"
    });

});
