use std::io;
use std::net::UdpSocket;
use std::str;

fn main() {
    let (user, password) = read_user_password();

    let socket = UdpSocket::bind("0.0.0.0:0").expect("failed to bind host socket");

    let message = format!("{}:{}", user, password);

    socket
        .send_to(message.as_bytes(), "localhost:12003")
        .expect("Error sending the message");

    let mut buf: [u8; 1024] = [0; 1024];
    let n_bytes = socket.recv(&mut buf).expect("Error Reading Response");

    let response_bytes = &mut buf[..n_bytes];

    let response: &str = str::from_utf8(response_bytes).expect("Invalid UTF-8 Sequence");

    println!("{}", response);
}

fn read_user_password() -> (String, String) {
    println!("Type the Username:");

    let mut user = String::new();

    io::stdin()
        .read_line(&mut user)
        .expect("Failed to read line");


    println!("Type the Password:");
    let mut password = String::new();

    io::stdin()
        .read_line(&mut password)
        .expect("Failed to read line");
    
    (user.replace("\n",""), password.replace("\n",""))
}
