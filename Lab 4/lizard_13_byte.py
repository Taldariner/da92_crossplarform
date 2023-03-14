# @title version 5
class lizard_13():

    def __init__(self):
        self.zero = 0
        self.register_size = 16
        self.register_c = [self.zero.to_bytes(4, "little")] * 16
        self.register_a = [self.zero.to_bytes(4, "little")] * 16
        self.register_b = [self.zero.to_bytes(4, "little")] * 16
        self.register_r = [self.zero.to_bytes(4, "little")] * 16
        self.current_position = 0
        # self.register_lines = 0
        self.output = ""

    def clear_registers(self):
        self.register_c = [self.zero.to_bytes(4, "little")] * 16
        self.register_a = [self.zero.to_bytes(4, "little")] * 16
        self.register_b = [self.zero.to_bytes(4, "little")] * 16
        self.register_r = [self.zero.to_bytes(4, "little")] * 16
        self.current_position = 0

    def execute_command(self, command):
        command = command.split(" ")

        if (command[0] == "ENT"):
            self.command_ent()

        if (command[0] == "MOV"):
            self.command_mov(int(command[1]).to_bytes(4, "little"))

        if (command[0] == "PUSH"):
            if (command[1] == "CURR"):
                self.command_push("CURR".ljust(4, '\0').encode())
            else:
                self.command_push(int(command[1]).to_bytes(4, "little"))
            # self.register_r.insert(0, self.register_a[self.current_command] + self.register_b[self.current_command])

        if (command[0] == "ADD"):
            self.command_add(int(command[1]).to_bytes(4, "little"))
            # self.register_r.insert(0, self.register_a[self.current_command] + self.register_b[self.current_command])

        if (command[0] == "SUB"):
            self.command_sub(int(command[1]).to_bytes(4, "little"))

        if (command[0] == "BITR"):
            self.command_bitr()

        if (command[0] == "BITL"):
            self.command_bitl()

        if (command[0] == "ISBG"):
            if (command[1] == "CURR"):
                self.command_isbg("CURR".ljust(4, '\0').encode())
            else:
                self.command_isbg(int(command[1]).to_bytes(4, "little"))

        self.register_slice()

    def command_push(self, argument):
        self.register_c[0] = "PUSH".ljust(4, '\0').encode()
        if (argument == "CURR".ljust(4, '\0').encode()):
            self.register_a[0] = self.register_r[self.current_position]
        else:
            self.register_a[0] = argument

    def command_add(self, argument):
        self.register_c[0] = "ADD".ljust(4, '\0').encode()
        self.register_b[0] = argument
        result = (int.from_bytes(self.register_a[0], byteorder='little') + int.from_bytes(self.register_b[0],
                                                                                          byteorder='little')).to_bytes(
            4, "little")
        self.register_r[0] = result

    def command_sub(self, argument):
        self.register_c[0] = "SUB".ljust(4, '\0').encode()
        self.register_b[0] = argument
        result = (int.from_bytes(self.register_a[0], byteorder='little') - int.from_bytes(self.register_b[0],
                                                                                          byteorder='little')).to_bytes(
            4, "little")
        self.register_r[0] = result

    def command_bitr(self):
        self.register_c[0] = "BITR".ljust(4, '\0').encode()
        self.register_r[0] = (int.from_bytes(self.register_r[0], byteorder='little') >> 1).to_bytes(4, "little")

    def command_bitl(self):
        self.register_c[0] = "BITL".ljust(4, '\0').encode()
        self.register_r[0] = (int.from_bytes(self.register_r[0], byteorder='little') << 1).to_bytes(4, "little")

    def command_mov(self, argument):
        self.register_c[0] = "MOV".ljust(4, '\0').encode()
        self.current_position = int.from_bytes(argument, "little")

    def command_isbg(self, argument):
        self.register_c[0] = "ISBG".ljust(4, '\0').encode()
        if (argument == "CURR".ljust(4, '\0').encode()):
            self.register_b[0] = self.register_r[self.current_position]
        else:
            self.register_b[0] = argument
        self.register_r[0] = int(int.from_bytes(self.register_a[0], "little") > int.from_bytes(self.register_b[0], "little")).to_bytes(4, "little")

    '''
    def command_ent(self):
        # self.register_lines += 1
        self.register_c.insert(0, "ENT".ljust(4, '\0').encode())
        self.register_a.insert(0, self.zero.to_bytes(4, "little"))
        self.register_b.insert(0, self.zero.to_bytes(4, "little"))
        self.register_r.insert(0, self.zero.to_bytes(4, "little"))

        self.register_c.pop(-1)
        self.register_a.pop(-1)
        self.register_b.pop(-1)
        self.register_r.pop(-1)
    '''

    def command_ent(self):
        self.register_c = ["ENT".ljust(4, '\0').encode()] + self.register_c[:-1]
        self.register_a = ["ENT".ljust(4, '\0').encode()] + self.register_a[:-1]
        self.register_b = ["ENT".ljust(4, '\0').encode()] + self.register_b[:-1]
        self.register_r = ["ENT".ljust(4, '\0').encode()] + self.register_r[:-1]


    def register_slice(self):
        self.output = ""
        for i in range(16):
            self.output += str(self.register_c[i]) + "\t\t" + str(self.register_a[i]) + "\t\t" + str(
                self.register_b[i]) + "\t\t" + str(self.register_r[i]) + "\t\t" + str(self.current_position) + "\n"

    '''
    PUSH 5
    ADD 13
    ENT
    MOV 1
    PUSH CURR
    ADD 1
    '''