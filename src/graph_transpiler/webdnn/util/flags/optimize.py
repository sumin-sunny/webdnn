import os

OPTIMIZE = os.environ.get("OPTIMIZE", "1") == "1"

# optimize rule
REMOVE_REDUNDANT_OPERATOR = os.environ.get("REMOVE_REDUNDANT_OPERATOR", "1") == "1"
SIMPLIFY_ELEMENTWISE = os.environ.get("SIMPLIFY_ELEMENTWISE", "1") == "1"
REPLACE_SCALAR_AFFINE = os.environ.get("REPLACE_SCALAR_AFFINE", "1") == "1"
REMOVE_NO_EFFECT_OPERATOR = os.environ.get("REMOVE_NO_EFFECT_OPERATOR", "1") == "1"
SIMPLIFY_ELEMENTWISE_PARALLEL = os.environ.get("SIMPLIFY_ELEMENTWISE_PARALLEL", "1") == "1"
SIMPLIFY_ELEMENTWISE_SEQUENTIAL = os.environ.get("SIMPLIFY_ELEMENTWISE_SEQUENTIAL", "1") == "1"
MERGE_ELEMENTWISE = os.environ.get("MERGE_ELEMENTWISE", "1") == "1"
MERGE_SGEMM_AND_ELEMENTWISE_MUL = os.environ.get("MERGE_SGEMM_AND_ELEMENTWISE_MUL", "1") == "1"
OPTIMIZE_CHANNEL_MODE = os.environ.get("OPTIMIZE_CHANNEL_MODE", "1") == "1"
EXTRACT_UNIFORM_LITERAL = os.environ.get("EXTRACT_UNIFORM_LITERAL", "0") == "1"
CONSTANT_FOLDING = os.environ.get("CONSTANT_FOLDING", "1") == "1"

# memory allocation
VALIDATE_GENERATED_SOURCE = os.environ.get("VALIDATE_GENERATED_SOURCE", "1") == "1"
OPTIMIZE_INPLACE_OPERATION = os.environ.get("OPTIMIZE_INPLACE_OPERATION", "1") == "1"
OPTIMIZE_MEMORY_ALLOCATION = os.environ.get("OPTIMIZE_MEMORY_ALLOCATION", "1") == "1"
