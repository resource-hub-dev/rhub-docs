OpenAPI Documentation
=====================

.. warning::

    API is still in development, the documentation below is the latest version
    from the main development branch.

.. raw:: html

    <div id="swagger-ui"></div>

    <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js" charset="UTF-8"> </script>
    <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js" charset="UTF-8"> </script>
    <script>
    $(document).ready(function() {
        $('head').append('<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css" type="text/css"></link>');
        window.swagger_ui = SwaggerUIBundle({
            dom_id: "#swagger-ui",
            deepLinking: true,
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIStandalonePreset
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout",
            url: "../_static/openapi.json",
        });
    });
    </script>
