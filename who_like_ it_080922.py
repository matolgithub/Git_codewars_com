def likes(names=["Alex", "Jacob", "Mark", "Max"] ):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        count_users = len(names)
        num_in_text = count_users - 2
        return f"{names[0]}, {names[1]} and {num_in_text} others like this"    


if __name__ == "__main__":
    likes()