document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("select").addEventListener("change", () => {
        document.querySelector("form").submit();
    });
});