"""  
GraphQL configurations
"""
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from main.controller.mutation import mutation
from main.controller.query import query

path = "./"

defs = load_schema_from_path(path)

schema = make_executable_schema(defs, query, mutation, snake_case_fallback_resolvers)
