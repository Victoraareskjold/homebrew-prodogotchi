class Prodogotchi < Formula
    desc "CLI tool for managing tasks with fun"
    homepage "https://github.com/victoraareskjold/prodogotchi"
    url "https://github.com/victoraareskjold/prodogotchi/releases/download/v0.1.0/prodogotchi"
    sha256 "ca330dcc77c8403d76a87226cb480755e265a27a7660214446baf2a47974f9a4"
    license "MIT"
  
    def install
      bin.install "prodogotchi"
    end
  end
  