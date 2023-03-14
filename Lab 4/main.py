print("Durka")

class lizard_13(object):

    def __init__(self, instruction_list):
        #список інструкцій, що надходить в машину
        self.instruction_list = instruction_list

        #регістри
        self.register_a = self.register_b = self.register_t = None

        # Whether to branch
        self.flag = False

        #вказівник коду
        self.pc = 0

    def execute(self):
        while self.pc is not None:
            i = self.instruction_list[self.pc]
            print(self.pc, "\t\t", self.register_a, "\t\t", self.register_b, "\t\t", self.register_t, "\t\t", self.flag, "\t", i)
            instr, rest = i[0], i[1:]
            self.pc += 1 # Don't forget to increment the counter
            getattr(self, 'i_'+instr)(*rest)

    def i_copy(self, register_a, register_b):
        """Duplicates register b in register a"""
        setattr(self, register_a, getattr(self, register_b))

    def i_set(self, register_a, register_b):
        """Sets register a to the value b"""
        setattr(self, register_a, register_b)

    def i_exec(self, reg, op, *args):
        """Calls op and stores the result in reg."""
        setattr(self, reg, getattr(self, 'o_'+op)(*args))

    def i_test(self, op, *rest):
        if getattr(self, 'o_'+op)(*rest):
            self.flag = True
        else:
            self.flag = False

    def i_branch(self, line):
        """Jump to line if flag is set"""
        if self.flag: self.pc = line

    def i_jump(self, line):
        """Jump to line"""
        self.pc = line

    def o_zero(self, reg):
        """Is reg zero?"""
        return getattr(self, reg) == 0

    def o_lt(self, register_a, register_b):
        return getattr(self, register_a) < getattr(self, register_b)

    def o_sub(self, register_a, register_b):
        """reg a - reg b"""
        return getattr(self, register_a) - getattr(self, register_b)

m = lizard_13((
    # If b is zero, then we are done.
    ('test', 'zero', 'register_b'),      # if b == 0
    ('branch', None),           # We're done
    ('copy', 'register_t', 'register_a'),         # t <- a

    # If a < b, then we swap out b and a.
    ('test', 'lt', 'register_t', 'register_b'),   # t < b?
    ('branch', 7),

    # Subtract out b from a.
    ('exec', 'register_t', 'sub', 'register_t', 'register_b'), # t <- t-b
    ('jump', 3),

    ('copy', 'register_a', 'register_b'),         # a <- b
    ('copy', 'register_b', 'register_t'),         # b <- t
    ('jump', 0),
    ))
m.register_a = 56
m.register_b = 12
print("pointer\t register a\t register b\t register t\t flag\t instruction index")
m.execute()
print(m.register_a)