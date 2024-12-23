from setuptools import setup, find_packages

setup(
    name="bot_especialist",  # Replace with your package name
    version="0.0.0",  # Version number
    description="bot especialist project to test various rags",
    long_description=open('README.md').read(),  # Ensure you have a README.md file
    long_description_content_type="text/markdown",  # Set to 'text/x-rst' if using reStructuredText
    author="Lucas Vital",  # Replace with your name
    author_email="lucasvittal@gmail.com",  # Replace with your email
    url="https://github.com/yourusername/your_repository",  # Replace with your GitHub or project URL
    packages=find_packages(),  # Automatically finds all packages in the directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if using a different license
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        "aiohappyeyeballs==2.4.4",
        "aiohttp==3.11.10",
        "aiosignal==1.3.1",
        "alembic==1.14.0",
        "altair==4.2.2",
        "annotated-types==0.7.0",
        "anyio==4.7.0",
        "appnope==0.1.4",
        "argon2-cffi==23.1.0",
        "argon2-cffi-bindings==21.2.0",
        "arrow==1.3.0",
        "asttokens==3.0.0",
        "async-lru==2.0.4",
        "async-timeout==4.0.3",
        "attrs==24.2.0",
        "babel==2.16.0",
        "beautifulsoup4==4.12.3",
        "bleach==6.2.0",
        "blinker==1.9.0",
        "cachetools==5.5.0",
        "certifi==2024.8.30",
        "cffi==1.17.1",
        "charset-normalizer==3.4.0",
        "click==8.1.7",
        "comm==0.2.2",
        "dataclasses-json==0.6.7",
        "debugpy==1.8.10",
        "decorator==5.1.1",
        "defusedxml==0.7.1",
        "Deprecated==1.2.15",
        "dill==0.3.9",
        "distro==1.9.0",
        "docarray==0.40.0",
        "entrypoints==0.4",
        "exceptiongroup==1.2.2",
        "executing==2.1.0",
        "fastjsonschema==2.21.1",
        "fqdn==1.5.1",
        "frozenlist==1.5.0",
        "gitdb==4.0.11",
        "GitPython==3.1.43",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "httpx-sse==0.4.0",
        "idna==3.10",
        "importlib_metadata==8.5.0",
        "importlib_resources==6.4.5",
        "ipykernel==6.29.5",
        "ipython==8.18.1",
        "ipywidgets==8.1.5",
        "isoduration==20.11.0",
        "jedi==0.19.2",
        "Jinja2==3.1.4",
        "jiter==0.8.2",
        "joblib==1.4.2",
        "json5==0.10.0",
        "jsonpatch==1.33",
        "jsonpointer==3.0.0",
        "jsonschema==4.23.0",
        "jsonschema-specifications==2024.10.1",
        "jupyter==1.1.1",
        "jupyter-console==6.6.3",
        "jupyter-events==0.10.0",
        "jupyter-lsp==2.2.5",
        "jupyter_client==8.6.3",
        "jupyter_core==5.7.2",
        "jupyter_server==2.14.2",
        "jupyter_server_terminals==0.5.3",
        "jupyterlab==4.3.3",
        "jupyterlab_pygments==0.3.0",
        "jupyterlab_server==2.27.3",
        "jupyterlab_widgets==3.0.13",
        "langchain==0.3.11",
        "langchain-community==0.3.11",
        "langchain-core==0.3.24",
        "langchain-openai==0.2.12",
        "langchain-text-splitters==0.3.2",
        "langsmith==0.2.2",
        "Mako==1.3.8",
        "markdown-it-py==3.0.0",
        "MarkupSafe==3.0.2",
        "marshmallow==3.23.1",
        "matplotlib-inline==0.1.7",
        "mdurl==0.1.2",
        "mistune==3.0.2",
        "multidict==6.1.0",
        "munch==2.5.0",
        "mypy-extensions==1.0.0",
        "narwhals==1.17.0",
        "nbclient==0.10.1",
        "nbconvert==7.16.4",
        "nbformat==5.10.4",
        "nest-asyncio==1.6.0",
        "nltk==3.9.1",
        "notebook==7.3.1",
        "notebook_shim==0.2.4",
        "numpy==1.26.4",
        "openai==1.57.2",
        "opentelemetry-api==1.28.2",
        "opentelemetry-sdk==1.28.2",
        "opentelemetry-semantic-conventions==0.49b2",
        "orjson==3.10.12",
        "overrides==7.7.0",
        "packaging==24.2",
        "pandas==2.2.3",
        "pandocfilters==1.5.1",
        "parso==0.8.4",
        "pexpect==4.9.0",
        "pillow==11.0.0",
        "platformdirs==4.3.6",
        "plotly==5.24.1",
        "prometheus_client==0.21.1",
        "prompt_toolkit==3.0.48",
        "propcache==0.2.1",
        "protobuf==5.29.1",
        "psutil==5.9.8",
        "ptyprocess==0.7.0",
        "pure_eval==0.2.3",
        "pyarrow==18.1.0",
        "pycparser==2.22",
        "pydantic==2.10.3",
        "pydantic-settings==2.6.1",
        "pydantic_core==2.27.1",
        "pydeck==0.9.1",
        "Pygments==2.18.0",
        "pypdf==5.1.0",
        "python-dateutil==2.9.0.post0",
        "python-decouple==3.8",
        "python-dotenv==1.0.1",
        "python-json-logger==2.0.7",
        "pytz==2024.2",
        "PyYAML==6.0.2",
        "pyzmq==26.2.0",
        "referencing==0.35.1",
        "regex==2024.11.6",
        "requests==2.32.3",
        "requests-toolbelt==1.0.0",
        "rfc3339-validator==0.1.4",
        "rfc3986-validator==0.1.1",
        "rich==13.9.4",
        "rpds-py==0.22.3",
        "scikit-learn==1.6.0",
        "scipy==1.13.1",
        "Send2Trash==1.8.3",
        "six==1.17.0",
        "smmap==5.0.1",
        "sniffio==1.3.1",
        "soupsieve==2.6",
        "SQLAlchemy==2.0.36",
        "stack-data==0.6.3",
        "streamlit==1.41.0",
        "streamlit-aggrid==1.0.5",
        "tenacity==9.0.0",
        "terminado==0.18.1",
        "threadpoolctl==3.5.0",
        "tiktoken==0.8.0",
        "tinycss2==1.4.0",
        "toml==0.10.2",
        "tomli==2.2.1",
        "toolz==1.0.0",
        "tornado==6.4.2",
        "tqdm==4.67.1",
        "traitlets==5.14.3",
        "trulens==1.2.10",
        "trulens-apps-langchain==1.2.10",
        "trulens-core==1.2.10",
        "trulens-dashboard==1.2.10",
        "trulens-feedback==1.2.10",
        "trulens-otel-semconv==1.2.10",
        "trulens-providers-langchain==1.2.10",
        "trulens-providers-openai==1.2.10",
        "trulens_eval==1.2.10",
        "types-python-dateutil==2.9.0.20241206",
        "types-requests==2.32.0.20241016",
        "typing-inspect==0.9.0",
        "typing_extensions==4.12.2",
        "tzdata==2024.2",
        "uri-template==1.3.0",
        "urllib3==2.2.3",
        "wcwidth==0.2.13",
        "webcolors==24.11.1",
        "webencodings==0.5.1",
        "websocket-client==1.8.0",
        "widgetsnbextension==4.0.13",
        "wrapt==1.17.0",
        "yarl==1.18.3",
        "zipp==3.21.0",
    ],
    python_requires="==3.9.*",
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com//lucasvittal2/bot-especialist/issues",
        "Documentation": "N/A",
    },
)
