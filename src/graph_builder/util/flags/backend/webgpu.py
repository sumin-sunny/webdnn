import os

VALIDATE_GENERATED_SOURCE = os.environ.get("FLAG_VALIDATE_GENERATED_SOURCE", "1") == "1"

# memory allocation
OPTIMIZE_MEMORY_ALLOCATION = os.environ.get("FLAG_OPTIMIZE_MEMORY_ALLOCATION", "1") == "1"
OPTIMIZE_INPLACE_OPERATION = os.environ.get("FLAG_OPTIMIZE_INPLACE_OPERATION", "1") == "1"
VISUALIZE_MEMORY_ALLOCATION = os.environ.get("FLAG_VISUALIZE_MEMORY_ALLOCATION", "0") == "1"