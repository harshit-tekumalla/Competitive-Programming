class Solution:
    def interpret(self, command: str) -> str:
        # for i in command:
        #     if "()" in i:
        #         command1 = command.replace("()","o")
        #     if "(al)" in i:
        #         command1 = command.replace("(al)","al")
        # return command1
        command=command.replace("()","o")
        command=command.replace("(al)","al")
        command=command.replace("G","G")      
        return command
