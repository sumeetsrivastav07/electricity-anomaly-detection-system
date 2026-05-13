document.addEventListener(
    "DOMContentLoaded",

    function () {

        // Loading Spinner

        const form = document.querySelector(
            "form"
        );

        const loader = document.getElementById(
            "loading-spinner"
        );

        if (form) {

            form.addEventListener(
                "submit",

                function () {

                    loader.style.display =
                        "block";

                }
            );
        }

        // Dark Mode Toggle

        const darkModeButton =
            document.getElementById(
                "dark-mode-toggle"
            );

        if (darkModeButton) {

            darkModeButton.addEventListener(
                "click",

                function () {

                    document.body.classList.toggle(
                        "dark-mode"
                    );

                }
            );
        }

    }
);