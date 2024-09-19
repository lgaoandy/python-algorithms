class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    END = '\033[0m'

class MadLib:
    def __init__(self) -> None:
        self.special_prompts = {}

    def load_file(self, filename: str) -> list[str]:
        content = []
        file_content = open(filename, 'r')

        for line in file_content:
            content.append(line.strip())
        return content


    def check_a_or_an(self, noun: str) -> str:
        vowels = "aeiou"
        if noun[0].lower() in vowels:
            return "an"
        else:
            return "a"
        

    def check_special_prompt(self, s: str) -> tuple[bool, str]:
        prompt = []
        is_special = False
        for i in s:
            if i.isdigit():
                is_special = True
            else:
                prompt.append(i)
        return (is_special, "".join(prompt))


    def has_prompt(self, s: str) -> bool:
        return "<" in s and ">" in s and s.index("<") < s.index(">")
    

    def add_special_prompt(self, prompt: str, answer: str) -> None:
        self.special_prompts[prompt] = answer


    def ask_user(self, prompt: str) -> str:
        answer = ""
        is_special_prompt, s_prompt = self.check_special_prompt(prompt)

        if is_special_prompt:
            if prompt not in self.special_prompts.keys():
                determiner = self.check_a_or_an(s_prompt)
                answer = input(f"\n{Colors.GREEN}Enter {determiner} {s_prompt}{Colors.END}: ")
                self.add_special_prompt(prompt, answer)
            else:
                answer = self.special_prompts[prompt]
        else:
            determiner = self.check_a_or_an(s_prompt)
            answer = input(f"\n{Colors.GREEN}Enter {determiner} {s_prompt}{Colors.END}: ")
        return answer


    def play(self, filename: str) -> None:
        content = self.load_file(filename)
        
        for k in range(len(content)):
            sentence = content[k].strip()
            
            if len(sentence) > 0:
                completed = [sentence[0]]
                prompt_list = []

                for i in range(1, len(sentence)):
                    if completed[-1] != "<":
                        completed.append(sentence[i])
                    elif sentence[i] == ">":
                        completed.pop()
                        prompt = "".join(prompt_list)
                        prompt_list = []
                        answer = self.ask_user(prompt)     
                        completed.append(answer)
                    else:
                        prompt_list.append(sentence[i])
                content[k] = "".join(completed)
            else:
                content[k] = sentence
            k += 1
        
        print("\n=================================")
        print(f"\n{Colors.CYAN}{content[0]}{Colors.END}")

        for i in range(1, len(content)):
            print(content[i])
        print("\n")


if __name__ == "__main__":
    MadLib().play("mad_libs1.txt")
    # MadLib().play("mad_libs2.txt")
