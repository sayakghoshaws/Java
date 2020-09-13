## a basic tester for the steganography project for examples given online
## importing functions from assignment code
from steganography import encode, decode

## global variables for counting tests / failed tests
g_test_count = 0
g_fail_count = 0

def test_encode(msg, original, expected_output):
    '''Tests whether encode(msg, original) == expected_output.'''
    ## declare globals
    global g_test_count, g_fail_count

    ## test the encode function
    actual_output = en  code(msg, original)
    g_test_count += 1

    ## check for failure
    if actual_output != expected_output:
        g_fail_count += 1
        print("failed: encode({!r}, {!r})".format(msg, original))
        print("      : --returned: {!r}".format(actual_output))
        print("      : --expected: {!r}".format(expected_output))

def test_decode(input, expected_output):
    '''Tests whether decode(input) == expected_output.'''
    ## declare globals
    global g_test_count, g_fail_count

    ## test the decode function
    actual_output = decode(input)
    g_test_count += 1

    ## check for failures
    if actual_output != expected_output:
        g_fail_count += 1
        print("failed: decode({!r})".format(input))
        print("      : --returned: {!r}".format(actual_output))
        print("      : --expected: {!r}".format(expected_output))

def run_all_tests():
    '''Runs test cases given in the assignment definition.'''
    ## test encodings from the assignment definition
    test_encode("hello", "a"*42, "AAaAaaaAAaaAaAAAaAAaaAAaAAaaAAaAAAAaaaaaaa")
    test_encode("hello", "A"*42, "AAaAaaaAAaaAaAAAaAAaaAAaAAaaAAaAAAAaaaaaaa")
    test_encode("hello", "This is a perfectly normal sentence.  Nothing "
                         "interesting to see here."
                       , "THiS is a PErfEcTLY nORmaL SeNTenCE.  nOTHIng "
                         "interesting to see here.")
    test_encode("secret!", "A perfectly normal and uninteresting sentence "
                           "with no hidden message inside."
                         , "A PErfECTLy nOrMAL and UNINTerEsTIng SeNTENcE "
                           "witH no hiDden message inside.")

    ## test decodings from the assignment definition
    test_decode("A PErfECTLy nOrMAL and UNINTerEsTIng SeNTENcE witH no hiDden "
                "message inside.", "secret!")
    test_decode("THiS is a PErfEcTLY nORmaL SeNTenCE.  nOTHIng interesting to "
                "see here.", "hello")
    test_decode("AAaAaaaAAaaAaAAAaAAaaAAaAAaaAAaAAAAaaaaaaa", "hello")

    ## print summary of testing
    if g_fail_count <= 0:
        print("passed all", g_test_count, "tests!")
    else:
        print("failed", g_fail_count, "of", g_test_count, "tests.")

## run all of the tests
run_all_tests()
