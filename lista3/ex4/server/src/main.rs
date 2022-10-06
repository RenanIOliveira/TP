use std::net::UdpSocket;
use std::str;

static ACCEPTED_LOGIN: &str = "user123";
static ACCEPTED_PASSWORD: &str = "pass123";

struct AuthenticationInfo {
    login: String,
    password: String,
}

impl AuthenticationInfo {
    fn new(login: String, password: String) -> Self {
        Self { login, password }
    }

    fn equals(&self, other: &AuthenticationInfo) -> bool {
        self.password == other.password && self.login == other.login
    }
}

fn main() {
    let accepted_auth =
        AuthenticationInfo::new(ACCEPTED_LOGIN.to_string(), ACCEPTED_PASSWORD.to_string());

    let socket = UdpSocket::bind("localhost:12003").expect("Error when trying to bind to Adress");

    let mut buf: [u8; 1024] = [0; 1024];
    loop {
        let (amt, src) = socket
            .recv_from(&mut buf)
            .expect("Error Reading Data from socket");

        let message_bytes = &mut buf[..amt];

        let message: &str = str::from_utf8(message_bytes).expect("Invalid UTF-8 sequence");

        let auth_info = get_login_password(message);

        let is_authorized = auth_info.equals(&accepted_auth);

        let response = match is_authorized {
            true => String::from("Ok"),
            false => String::from("Error"),
        };

        let response_bytes = response.as_bytes();

        socket
            .send_to(response_bytes, &src)
            .expect("Error Writing to Socket");
    }
}

fn get_login_password(message: &str) -> AuthenticationInfo {
    let split_message: Vec<&str> = message.split(":").collect();

    AuthenticationInfo::new(split_message[0].to_string(), split_message[1].to_string())
}
