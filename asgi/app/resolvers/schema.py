import os
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers
)

from .query import QUERY

_schema_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schema'))
_TYPE_DEFS = load_schema_from_path(_schema_dir)

SCHEMA = make_executable_schema(
    _TYPE_DEFS,
    [*QUERY],
    snake_case_fallback_resolvers
)
