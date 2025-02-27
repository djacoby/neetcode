class LeetTester:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
    
    def test(self, expected, actual, test_name=""):
        self.tests_run += 1
        test_id = f"Test #{self.tests_run}"
        prefix = f"{test_id} - {test_name}: " if test_name else f"{test_id}: "
        
        result = self._compare(expected, actual, prefix)
        if result:
            self.tests_passed += 1
        
        return result
    
    def _compare(self, expected, actual, prefix):
        # Handle collections that may have different order but same elements
        if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
            if sorted(expected) == sorted(actual):
                print(f"✅ {prefix}Test passed (after sorting)")
                return True
            else:
                print(f"❌ {prefix}Test failed: Expected {expected} but received {actual}")
                return False
        
        # Regular comparison
        if actual == expected:
            print(f"✅ {prefix}Test passed: {expected}")
            return True
        else:
            print(f"❌ {prefix}Test failed: Expected {expected} but received {actual}")
            return False
    
    def summary(self):
        print(f"\n--- Test Summary ---")
        print(f"Tests run: {self.tests_run}")
        print(f"Tests passed: {self.tests_passed}")
        print(f"Success rate: {(self.tests_passed/self.tests_run)*100:.2f}% " if self.tests_run > 0 else "No tests run")
