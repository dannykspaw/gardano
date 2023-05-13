use std::process::Command;

fn main() {
    let repo_path = "";
    Command::new("cd").arg(repo_path).status().unwrap();

    Command::new("git").arg("add").arg(".").status().unwrap();

    let commit_message = "Last Data Update: ";
    Command::new("git").arg("commit").arg("-m").arg(commit_message).status().unwrap();

    Command::new("git").arg("push").status().unwrap();
}

