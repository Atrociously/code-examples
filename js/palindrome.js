export function isPalindrome1(input) {
  for (let i = 0; i < input.length; i++) {
    if (input.charAt(i) != input.charAt(input.length - 1 - i)) {
        return false;
    }
  }
  return true;
}

export function isPalindrome2(input) {
  const reversed = input.toString()
    .split("")
    .reverse()
    .join("");
  return input == reversed;
}

console.log(isPalindrome("abcba"));
console.log(isPalindrome("abc"));
