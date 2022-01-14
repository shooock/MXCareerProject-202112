def simplifyPath(path: str) -> str:
    #注意空集不能pop
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)
names='/home//aaa/./././.././././home/'
ans = simplifyPath(names)
print(ans)

