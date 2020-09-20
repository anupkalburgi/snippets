use std::io;

fn main() {
    println!("Guessing Game");
    
    println!("Input a number, your guess");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("Your guess: {}", guess);
}