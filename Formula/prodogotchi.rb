class Prodogotchi < Formula
    desc "CLI tool for managing tasks with fun"
    homepage "https://github.com/victoraareskjold/prodogotchi"
    url "https://github.com/victoraareskjold/prodogotchi/releases/download/v0.2.0/prodogotchi"
    sha256 "2253b8b2ec255572ddfc96ba962d1dae0d8749927f6960f42befa5ade27397ac"
    license "MIT"
  
    def install
      bin.install "prodogotchi"
    end
  end
  