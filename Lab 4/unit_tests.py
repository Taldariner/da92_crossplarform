import lizard_13_byte as lz13

test_array = [["PUSH 5", 0],
              ["PUSH 5\nADD 13", 18],
              ["PUSH 5\nSUB 1", 4],
              ["PUSH 5\nADD 0\nBITR", 2],
              ["PUSH 5\nADD 0\nBITL", 10]]
test_pc = lz13.lizard_13()

for test in test_array:
    for command in test[0].split("\n"):
        test_pc.execute_command(command)
    #print(int.from_bytes(test_pc.register_r[0], "little"))
    #print(test[1])
    if(int.from_bytes(test_pc.register_r[0], "little") == test[1]):
        print("Test passed successfully.")
    else:
        print("Test failed.")