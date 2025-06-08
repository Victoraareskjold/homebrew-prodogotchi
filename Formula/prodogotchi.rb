class Prodogotchi < Formula
    desc "CLI tool for managing tasks with fun"
    homepage "https://github.com/victoraareskjold/prodogotchi"
    url "https://github.com/victoraareskjold/prodogotchi/releases/download/v0.1.1/prodogotchi"
    sha256 "02c64cf335dc61787e94fa800c3147ce9cbc87e05b0bec9ad02cee356fe0652d"
    license "MIT"
  
    def install
      bin.install "prodogotchi"
    end
  end
  