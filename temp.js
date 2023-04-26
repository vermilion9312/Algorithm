

function recursion(string, count, strLength) {
    if (count >= strLength) {
        return 1;
    } else if (string[count] != string[strLength]) {
        return 0;
    } else {
        return recursion(string, count + 1, strLength - 1);
    }
}

function isPalindrome(string) {
    let strLength = string.length - 1;
    let count = 0;
    return recursion(string, count, strLength);
}
console.log("fdsfs")