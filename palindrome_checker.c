#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_palindrome(const char *s) {
    int len = strlen(s);
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    // Test cases
    printf("%d\n", is_palindrome("radar"));  // 1 (True)
    printf("%d\n", is_palindrome("hello"));  // 0 (False)
    return 0;
}
