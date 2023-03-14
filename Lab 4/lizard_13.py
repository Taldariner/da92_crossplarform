# @title version 3
class lizard_13():

    def __init__(self):
        self.register_size = 16
        self.register_c = []
        self.register_a = []
        self.register_b = []
        self.register_r = []
        self.current_position = 0
        self.register_lines = 0
        self.output = ""

    def execute_command(self, command):
        command = command.split(" ")

        if (command[0] == "PUSH"):
            self.command_push(command[1])
            # self.register_r.insert(0, self.register_a[self.current_command] + self.register_b[self.current_command])

        if (command[0] == "ADD"):
            self.command_add(int(command[1]))
            # self.register_r.insert(0, self.register_a[self.current_command] + self.register_b[self.current_command])

        if (command[0] == "SUB"):
            self.command_sub(int(command[1]))

        if (command[0] == "BITR"):
            self.command_bitr()

        if (command[0] == "BITL"):
            self.command_bitl()

        if (command[0] == "ENT"):
            self.command_ent()

        if (command[0] == "MOV"):
            self.command_mov(command[1])

        if (command[0] == "ISBG"):
            self.command_isbg(command[1])

        self.register_slice()

    def command_push(self, argument):
        self.register_c[0] = "PUSH"
        if (argument == "CURR"):
            self.register_a[0] = self.register_r[self.current_position]
        else:
            self.register_a[0] = int(argument)

    def command_add(self, argument):
        self.register_c[0] = "ADD"
        self.register_b[0] = argument
        self.register_r[0] = self.register_a[0] + self.register_b[0]

    def command_sub(self, argument):
        self.register_c[0] = "SUB"
        self.register_b[0] = argument
        self.register_r[0] = self.register_a[0] - self.register_b[0]

    def command_bitr(self):
        self.register_c[0] = "BITR"
        self.register_r[0] = self.register_r[0] >> 1

    def command_bitl(self):
        self.register_c[0] = "BITL"
        self.register_r[0] = self.register_r[0] << 1

    def command_mov(self, argument):
        self.register_c[0] = "MOV"
        self.current_position = int(argument)

    def command_isbg(self, argument):
        self.register_c[0] = "ISBG"
        if (argument == "CURR"):
            self.register_b[0] = self.register_r[self.current_position]
        else:
            self.register_b[0] = argument
        self.register_r[0] = int(self.register_a[0] > self.register_b[0])

    def command_ent(self):
        if (len(self.register_c) < self.register_size and
                len(self.register_a) < self.register_size and
                len(self.register_b) < self.register_size and
                len(self.register_r) < self.register_size):
            self.register_lines += 1
            self.register_c.insert(0, "ENT")
            self.register_a.insert(0, 0)
            self.register_b.insert(0, 0)
            self.register_r.insert(0, 0)
        else:
            raise Exception("System register overload. Comand execution aborted.")

    def register_slice(self):
        for i in range(self.register_lines):
            # print(self.register_c[i], "\t", self.register_a[i], "\t", self.register_b[i], "\t", self.register_r[i], "\t", self.current_position)
            self.output += str(self.register_c[i]) + "\t" + str(self.register_a[i]) + "\t" + str(
                self.register_b[i]) + "\t" + str(self.register_r[i]) + "\t" + str(self.current_position) + "\n"
        self.output += "=" * 50 + "\n"


if __name__ == "__main__":
    lizard_13 = lizard_13()

    print("reg c", "\t", "reg a", "\t", "reg b", "\t", "reg r", "\t", "current position", )
    print("=" * (25 + 25))

    lizard_13.execute_command("ENT")
    lizard_13.execute_command("PUSH 5")
    lizard_13.execute_command("ADD 13")
    lizard_13.execute_command("PUSH CURR")
    lizard_13.execute_command("SUB 1")
    lizard_13.execute_command("BITR")

    lizard_13.execute_command("ENT")
    lizard_13.execute_command("PUSH 16")
    lizard_13.execute_command("ADD 13")
    lizard_13.execute_command("PUSH CURR")
    lizard_13.execute_command("ADD 1")
    lizard_13.execute_command("BITL")

    lizard_13.execute_command("ENT")
    lizard_13.execute_command("MOV 2")
    lizard_13.execute_command("PUSH CURR")
    lizard_13.execute_command("MOV 1")
    lizard_13.execute_command("ISBG CURR")
