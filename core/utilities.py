class Banner:
    def __init__(self, tool_name, version, author):
        self.tool_name = tool_name
        self.version = version
        self.author = author

    def display(self):
        banner = f"""
╭━╮╭━╮     ╭━━━╮
┃┃╰╯┃┃     ┃╭━━╯
┃╭╮╭╮┣━━┳━━┫╰━━┳╮ ╭┳━━╮
┃┃┃┃┃┃╭╮┃╭╮┃╭━━┫┃ ┃┃┃━┫
┃┃┃┃┃┃╭╮┃╰╯┃╰━━┫╰━╯┃┃━┫
╰╯╰╯╰┻╯╰┫╭━┻━━━┻━╮╭┻━━╯
        ┃┃     ╭━╯┃
        ╰╯     ╰━━╯
        """
        print(banner)
        print(f"[>] Tool      : {self.tool_name}")
        print(f"[>] Version   : {self.version}")
        print(f"[>] Author    : {self.author}\n")
