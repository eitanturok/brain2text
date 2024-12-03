# brain2text/__init__.py
import sys
import os

# Get the path to semantic-decoding/decoding relative to this __init__.py
base_dir = os.path.dirname(__file__)
decoding_path = os.path.join(base_dir, "semantic-decoding/decoding")
sys.path.append(decoding_path)

# Add to __init__.py temporarily
print(base_dir)  # See what directory this resolves to
print(decoding_path)  # See the full path being added
print(sys.path)  # Check if path was actually added



# # brain2text/__init__.py
# import sys
# import os

# base_dir = os.path.abspath(os.path.dirname(__file__))
# decoding_path = os.path.abspath(os.path.join(base_dir, "semantic-decoding/decoding"))
# sys.path.append(decoding_path)
