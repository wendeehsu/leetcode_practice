def isPalindrome(s: str):
    start_ = 0
    end_ = len(s)-1

    if len(s) <= 1:
        return True
    
    while start_ < end_:
        if not s[start_].isalnum():
            start_ += 1
            continue
        elif not s[end_].isalnum():
            end_ -= 1
            continue
        else:
            if s[start_].lower() != s[end_].lower():
                return False
            else:
                start_ += 1
                end_ -= 1
    return True


s_ = " "
print(isPalindrome(s_))
