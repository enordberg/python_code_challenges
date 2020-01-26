""" Simple algorithm test in python."""
# binary gap finder
# find the length of the longest group of consequtive zeros
# in a binary number, with ones on both sides.
# example, 110003001 has a length of 3.  1001 has a length of 2.
# 10101 has a length of 1.  100 has a length of zero (no one on the one side).

def main():
    """ Runs the program."""
    print("Enter a decimal number.  We'll find the binary gap of that number.")
    decimal_input_raw = input()
    decimal_input = int(decimal_input_raw)
    print("You entered " + str(decimal_input) + ".")

    powers_of_two = generate_powers_of_two(decimal_input)

    binary_number_and_gap = determine_binary_and_gap(decimal_input, [], 0, 0, False, powers_of_two)
    print("The binary representation is " +
          convert_int_list_to_string(binary_number_and_gap[1]) + ".")
    print("The binary gap is " + str(binary_number_and_gap[0]) + ".")


def generate_powers_of_two(decimal_input):
    """  Creates a list of all powers of 2 less than or equal to the decimal
    input """
    current_power = 1
    result = []
    while current_power <= decimal_input:
        result.insert(0, current_power)
        current_power = current_power * 2
    return result

def determine_binary_and_gap(current_target, binary_number_in_progress, largest_gap_yet,
                             current_size_of_gap, is_gap_right_now, powers_of_two):
    """ Recursively determines the output binary # and gap #."""
    current_power_of_two = powers_of_two.pop(0)
    if current_target >= current_power_of_two:
        current_target = current_target - current_power_of_two
        binary_number_in_progress.append(1)
        if current_size_of_gap > largest_gap_yet: # gap must end with a 1
            largest_gap_yet = current_size_of_gap
        is_gap_right_now = False
        current_size_of_gap = 0
    else:
        current_size_of_gap = current_size_of_gap + 1
        is_gap_right_now = True
        binary_number_in_progress.append(0)
    if any(powers_of_two):
        return determine_binary_and_gap(current_target,
                                        binary_number_in_progress,
                                        largest_gap_yet, current_size_of_gap,
                                        is_gap_right_now, powers_of_two)
    return (largest_gap_yet, binary_number_in_progress)

def convert_int_list_to_string(binary_in_progress):
    """ Convert list of integers to string. """
    string_list = map(str, binary_in_progress)
    result = ""
    result = result.join(string_list)
    return result

if __name__ == "__main__":
    main()
