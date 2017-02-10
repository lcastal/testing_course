# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list.
# The return value of the fuzzit procedure should be a list of
# byte-modified strings.


import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):
    # Write a random fuzzer for a simulated text viewer application
    num_test = 10000

    min_fuzz_factor = math.ceil(float(len(content)) / 4)
    max_fuzz_factor = math.ceil(float(len(content)) / 2)
    l = list()

    for i in range(num_test):
        buff = bytearray(str.encode(content, "ascii"))

        #### Charlie Miller Code ####

        # plus one to be sure that at least one byte will be modified
        num_writes = random.randrange(min_fuzz_factor, max_fuzz_factor)

        for j in range(num_writes):
            #replace randomly a byte of content file
            random_byte = random.randrange(256)
            random_index = random.randrange(len(buff))
            buff[random_index] = "%c"%(random_byte)

        l.append(str(buff.decode("ascii", "ignore")))
        #### End Charlie Miller Code ####

    return l

l_result = fuzzit(content)
for elem in l_result:
    print(elem)