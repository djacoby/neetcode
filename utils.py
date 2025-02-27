# utils.py
def test_fn(expected, actual, test_name=""):
    prefix = f"Test {test_name}: " if test_name else ""
    
    # Handle collections that may have different order but same elements
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if sorted(expected) == sorted(actual):
            print(f"✅ {prefix} Test passed (after sorting)")
            return
        else:
            print(f"❌ {prefix} Test failed: Expected {expected} but received {actual}")
            return
    
    # Regular comparison
    if actual == expected:
        print(f"✅ {prefix} Test passed: {expected}")
    else:
        print(f"❌ {prefix} Test failed: Expected {expected} but received {actual}")
