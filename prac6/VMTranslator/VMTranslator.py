class VMTranslator:

    @staticmethod
    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        if segment == 'constant':
            # Push constant value directly onto the stack
            return f"@{offset}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'local':
            # Push value from the local segment onto the stack
            return f"@LCL\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'argument':
            # Push value from the argument segment onto the stack
            return f"@ARG\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'this':
            # Push value from the this segment onto the stack
            return f"@THIS\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'that':
            # Push value from the that segment onto the stack
            return f"@THAT\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'pointer':
            # Push value from the pointer segment onto the stack
            if offset == '0':
                return f"@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            elif offset == '1':
                return f"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'temp':
            # Push value from the temp segment onto the stack
            return f"@R{5 + int(offset)}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == 'static':
            # Push value from the static segment onto the stack
            return f"@{filename}.{offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"

    @staticmethod
    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        if segment == 'local':
            # Pop value from the stack and store it in the local segment
            return f"@LCL\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif segment == 'argument':
            # Pop value from the stack and store it in the argument segment
            return f"@ARG\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif segment == 'this':
            # Pop value from the stack and store it in the this segment
            return f"@THIS\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif segment == 'that':
            # Pop value from the stack and store it in the that segment
            return f"@THAT\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"

    @staticmethod
    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n"

    @staticmethod
    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n"

    @staticmethod
    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        return "@SP\nA=M-1\nM=-M\n"

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        return ""

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        return ""

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        return ""

    @staticmethod
    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n"

    @staticmethod
    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n"

    @staticmethod
    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return "@SP\nA=M-1\nM=!M\n"

    @staticmethod
    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        return f"({label})\n"

    @staticmethod
    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        return f"@{label}\n0;JMP\n"

    @staticmethod
    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        return f"@SP\nAM=M-1\nD=M\n@{label}\nD;JNE\n"


    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        return ""

    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        return ""

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        return ""

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        