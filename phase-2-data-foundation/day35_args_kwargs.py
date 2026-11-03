def average(*nums):
    if not nums:
        return None
    return sum(nums) / len(nums)

def make_tag(tag, text, **attrs):
    if not attrs:
        return f"<{tag}>{text}</{tag}>"
    attributes = [f'{key}="{value}"' for key, value in attrs.items()]
    attr_text = " ".join(attributes)
    return f"<{tag} {attr_text}>{text}</{tag}>"
    


if __name__ == "__main__":
    print(average(4, 8, 6))
    print(average())
    scores = [70, 85, 90]
    print(average(*scores))
    link = {"href": "/about", "target": "_blank"}
    print(make_tag("a", "About", **link))
    print(make_tag("p", "Hello"))