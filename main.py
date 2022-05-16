from apiflask import APIFlask


class CustomAPIFlask(APIFlask):
    def __init__(self, import_name: str) -> None:
        super().__init__(import_name)
        self.config['SWAGGER_UI_CSS'] = 'https://unpkg.com/swagger-ui-dist@3/swagger-ui.css'
        self.config['SWAGGER_UI_BUNDLE_JS'] = 'https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
        self.config['SWAGGER_UI_STANDALONE_PRESET_JS'] = \
            'https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
        self.config['REDOC_STANDALONE_JS'] = 'https://unpkg.com/redoc@next/bundles/redoc.standalone.js'
