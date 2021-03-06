from django.conf import settings


PIPELINE_ROOT = getattr(settings, 'PIPELINE_ROOT', settings.MEDIA_ROOT)
PIPELINE_URL = getattr(settings, 'PIPELINE_URL', settings.MEDIA_URL)

PIPELINE = getattr(settings, 'PIPELINE', not settings.DEBUG)
PIPELINE_SOURCE = getattr(settings, 'PIPELINE_SOURCE', settings.STATIC_ROOT)
PIPELINE_ROOT = getattr(settings, 'PIPELINE_ROOT', settings.STATIC_ROOT)
PIPELINE_URL = getattr(settings, 'PIPELINE_URL', settings.STATIC_URL)
PIPELINE_AUTO = getattr(settings, 'PIPELINE_AUTO', True)
PIPELINE_VERSION = getattr(settings, 'PIPELINE_VERSION', False)
PIPELINE_VERSION_PLACEHOLDER = getattr(settings, 'PIPELINE_VERSION_PLACEHOLDER', '?')
PIPELINE_VERSION_DEFAULT = getattr(settings, 'PIPELINE_VERSION_DEFAULT', '0')
PIPELINE_VERSION_REMOVE_OLD = getattr(settings, 'PIPELINE_VERSION_REMOVE_OLD', True)
PIPELINE_VERSIONING = getattr(settings, 'PIPELINE_VERSIONING', 'pipeline.versioning.mtime.MTimeVersioning')

PIPELINE_STORAGE = getattr(settings, 'PIPELINE_STORAGE',
    'pipeline.storage.PipelineStorage')

PIPELINE_CSS_COMPRESSOR = getattr(settings, 'PIPELINE_CSS_COMPRESSOR',
    'pipeline.compressors.yui.YUICompressor'
)
PIPELINE_JS_COMPRESSOR = getattr(settings, 'PIPELINE_JS_COMPRESSOR',
    'pipeline.compressors.yui.YUICompressor'
)
PIPELINE_COMPILERS = getattr(settings, 'PIPELINE_COMPILERS', [])

PIPELINE_CSS = getattr(settings, 'PIPELINE_CSS', {})
PIPELINE_JS = getattr(settings, 'PIPELINE_JS', {})

PIPELINE_TEMPLATE_NAMESPACE = getattr(settings, 'PIPELINE_TEMPLATE_NAMESPACE', "window.JST")
PIPELINE_TEMPLATE_EXT = getattr(settings, 'PIPELINE_TEMPLATE_EXT', ".jst")
PIPELINE_TEMPLATE_FUNC = getattr(settings, 'PIPELINE_TEMPLATE_FUNC', "_.template")

PIPELINE_CSSTIDY_BINARY = '/usr/local/bin/csstidy'
PIPELINE_CSSTIDY_ARGUMENTS = '--template=highest'

PIPELINE_YUI_BINARY = getattr(settings, 'PIPELINE_YUI_BINARY', '/usr/local/bin/yuicompressor')
PIPELINE_YUI_CSS_ARGUMENTS = getattr(settings, 'PIPELINE_YUI_CSS_ARGUMENTS', '')
PIPELINE_YUI_JS_ARGUMENTS = getattr(settings, 'PIPELINE_YUI_JS_ARGUMENTS', '')

PIPELINE_CLOSURE_BINARY = getattr(settings, 'PIPELINE_CLOSURE_BINARY', '/usr/local/bin/closure')
PIPELINE_CLOSURE_ARGUMENTS = getattr(settings, 'PIPELINE_CLOSURE_ARGUMENTS', '')

PIPELINE_UGLIFYJS_BINARY = getattr(settings, 'PIPELINE_UGLIFYJS_BINARY', '/usr/local/bin/uglifyjs')
PIPELINE_UGLIFYJS_ARGUMENTS = getattr(settings, 'PIPELINE_UGLIFYJS_ARGUMENTS', '')

PIPELINE_COFFEE_SCRIPT_BINARY = getattr(settings, 'PIPELINE_COFFEE_SCRIPT_BINARY', '/usr/local/bin/coffee')
PIPELINE_COFFEE_SCRIPT_ARGUMENTS = getattr(settings, 'PIPELINE_COFFEE_SCRIPT_ARGUMENTS', '')

PIPELINE_SASS_BINARY = getattr(settings, 'PIPELINE_SASS_BINARY', '/usr/local/bin/sass')
PIPELINE_SASS_ARGUMENTS = getattr(settings, 'PIPELINE_SASS_ARGUMENTS', '')

PIPELINE_LESS_BINARY = getattr(settings, 'PIPELINE_LESS_BINARY', '/usr/local/bin/lessc')
PIPELINE_LESS_ARGUMENTS = getattr(settings, 'PIPELINE_LESS_ARGUMENTS', '')

if PIPELINE_COMPILERS is None:
    PIPELINE_COMPILERS = []
