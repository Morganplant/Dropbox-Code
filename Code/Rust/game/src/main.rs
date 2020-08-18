use std::io;
use std::process;
use rand::Rng;

fn main() {
	for _x in 0..100 {
		println!("");
	}
	static MONSTER_NAMES: [&str; 7] = ["Vampire", "Zombie", "Warewolf", "WarBoar", "Goblin", "Gremlin", "Orc"];

	


	let mut char_achp = 100;
	let  char_attk = rand::thread_rng().gen_range(5, 10);

	let mut kill_counter = 0;
	loop {
		let mon_name = MONSTER_NAMES[rand::thread_rng().gen_range(0, MONSTER_NAMES.len())].to_string();
		let mon_attk = rand::thread_rng().gen_range(5, 10);
		let mut mon_achp = rand::thread_rng().gen_range(0, 100);
		loop {
			if mon_achp <= 0 {
				kill_counter = kill_counter + 1;
				println!("You Killed the {}", mon_name);
				break
			}
			if char_achp <= 0 {
				println!("\t\tYou Lose");
				println!("Monsters Killed: {}", kill_counter);
				process::exit(1);
			}
			println!("\t\tYou : {} : | {} : {}", char_achp, mon_name, mon_achp);
			
			println!("Options:");
			println!("1) Attack");
			println!("2) Run");

			let user_input = input();
			if user_input == 1 {
				for _x in 0..char_attk {
					mon_achp = mon_achp - rand::thread_rng().gen_range(0, 10)
				}
				for _x in 0..mon_attk {
					char_achp = char_achp - rand::thread_rng().gen_range(0, 10)}
			}
			if user_input == 2 {
				for _x in 0..mon_attk {char_achp = char_achp - rand::thread_rng().gen_range(0, 5)}
				break
			}
		}
	}
}

fn input() -> i32 {
	let mut input = String::new();
	io::stdin().read_line(&mut input).unwrap();
	let n: i32 = input.trim().parse().unwrap();
	return n
}