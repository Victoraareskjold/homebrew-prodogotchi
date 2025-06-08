class Prodogotchi < Formula
    desc "CLI tool for managing tasks with fun"
    homepage "https://github.com/victoraareskjold/prodogotchi"
    url "https://github.com/victoraareskjold/prodogotchi/releases/download/v0.1.0/prodogotchi"
    sha256 "e491514c831e0e51b1769778a687b45b34ed233e8aa9fd457bfdc907c92d51ee"
    license "MIT"
  
    def install
      bin.install "prodogotchi"
    end
  end
  