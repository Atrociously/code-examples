fn is_palindrome1(input: &str) -> bool {
    for i in 0..input.len() {
        if input.chars().nth(i) != input.chars().nth(input.len() - 1 - i) {
            return false;
        }
    }
    true
}

fn is_palindrome2(input: &str) -> bool {
    input.chars()
        .zip(input.chars().rev())
        .all(|(a, b)| a == b)
}

fn main() {
    println!("{}", is_palindrome2("abcba"));
    println!("{}", is_palindrome2("abc"));
}
