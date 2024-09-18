import re
import typing

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

class MadLib:
    def load_file(self, filename: str) -> typing.TextIO:
        return open(filename, 'r')
    

    def check_a_or_an(self, noun: str) -> str:
        vowels = "aeiou"
        if noun[0].lower() in vowels:
            return "an"
        else:
            return "a"
        
    
    def split_prompts(self, content: typing.TextIO) -> tuple[list[str], list[str]]:
        stripped_content = []
        prompts = []
        for line in content:
            line = line.strip()
            
            if len(line) > 0:
                prompt = []
                stripped_line = [line[0]]
                for i in range(1, len(line)):
                    if stripped_line[-1] != "<":
                        stripped_line.append(line[i])
                    elif line[i] == ">":
                        stripped_line.append(line[i])
                        prompts.append("".join(prompt))
                        prompt = []
                    else:
                        prompt.append(line[i])
                stripped_content.append("".join(stripped_line).split())
        return prompts, stripped_content
    

    def get_user_prompts(self, prompts: list[str]) -> list[str]:
        n = len(prompts)
        substitutions = []
        for i in range(n):
            determiner = self.check_a_or_an(prompts[i])
            i = input(f"\n{Colors.GREEN}Enter {determiner} {prompts[i]}{Colors.END} ({i} of {n}): ")
            substitutions.append(i)
        return substitutions
    

    def play(self, filename: str) -> None:
        content = self.load_file(filename)
        prompts, stripped_content = self.split_prompts(content)
        print(stripped_content)
        substitutions = self.get_user_prompts(prompts)

        # substitute in content
        for i in range(len(stripped_content)):
            for j in range(len(stripped_content[i])):
                if "<>" in stripped_content[i][j]:
                    stripped_content[i][j] = stripped_content[i][j].replace("<>", substitutions.pop())
            line = " ".join(stripped_content[i]) 
            print(line)


if __name__ == "__main__":
    madlibs = MadLib()
    madlibs.play("projects/mad_libs/mad_libs2.txt")
